from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(
        self,
        db: Session,
        user_repository: UserRepository,
    ):
        self.db = db
        self.user_repository = user_repository


    def get_all(
        self,
    ) -> list[User]:

        return self.user_repository.get_all()



    def get_active(
        self,
    ) -> list[User]:

        return self.user_repository.get_active()



    def get_by_id(
        self,
        user_id: int,
    ) -> User:

        user = (
            self.user_repository
            .get_by_id(user_id)
        )


        if not user:

            raise ValueError(
                "User not found."
            )


        return user



    def search(
        self,
        search_term: str,
    ) -> list[User]:

        return (
            self.user_repository
            .search(search_term)
        )



    def get_by_role(
        self,
        role: str,
    ) -> list[User]:

        return (
            self.user_repository
            .get_by_role(role)
        )

    def create(
        self,
        name: str,
        dni: str,
        email: str,
        password: str,
        role: str = "employee",
    ) -> User:


        name = name.strip()

        dni = dni.strip()

        email = email.strip().lower()



        if not name:

            raise ValueError(
                "User name is required."
            )


        if not dni:

            raise ValueError(
                "DNI is required."
            )


        if not email:

            raise ValueError(
                "Email is required."
            )


        if not password:

            raise ValueError(
                "Password is required."
            )



        if self.user_repository.exists_email(
            email
        ):

            raise ValueError(
                "Email already registered."
            )



        if self.user_repository.exists_dni(
            dni
        ):

            raise ValueError(
                "DNI already registered."
            )



        self._validate_role(
            role
        )



        user = User(

            name=name,

            dni=dni,

            email=email,

            password_hash=
                hash_password(password),

            role=role,

            is_active=True,
        )



        try:

            self.user_repository.create(
                user
            )

            self.db.commit()

            self.db.refresh(
                user
            )

            return user


        except Exception:

            self.db.rollback()

            raise


    def update(
        self,
        user_id: int,
        name: str | None = None,
        email: str | None = None,
        role: str | None = None,
    ) -> User:


        user = self.get_by_id(
            user_id
        )


        if name:

            user.name = name.strip()



        if email:

            email = email.strip().lower()


            existing = (
                self.user_repository
                .get_by_email(email)
            )


            if (
                existing
                and existing.id != user.id
            ):

                raise ValueError(
                    "Email already registered."
                )


            user.email = email



        if role:

            self._validate_role(
                role
            )

            user.role = role



        try:

            self.user_repository.update(
                user
            )

            self.db.commit()

            self.db.refresh(
                user
            )

            return user


        except Exception:

            self.db.rollback()

            raise


    def change_password(
        self,
        user_id: int,
        new_password: str,
    ) -> User:


        if not new_password:

            raise ValueError(
                "Password is required."
            )


        user = self.get_by_id(
            user_id
        )


        user.password_hash = (
            hash_password(new_password)
        )


        try:

            self.user_repository.update(
                user
            )

            self.db.commit()

            self.db.refresh(
                user
            )

            return user


        except Exception:

            self.db.rollback()

            raise




    def deactivate(
        self,
        user_id: int,
    ) -> User:


        user = self.get_by_id(
            user_id
        )


        try:

            self.user_repository.delete(
                user
            )

            self.db.commit()

            self.db.refresh(
                user
            )

            return user


        except Exception:

            self.db.rollback()

            raise


    def activate(
        self,
        user_id: int,
    ) -> User:


        user = self.get_by_id(
            user_id
        )


        try:

            self.user_repository.restore(
                user
            )

            self.db.commit()

            self.db.refresh(
                user
            )

            return user


        except Exception:

            self.db.rollback()

            raise


    def _validate_role(
        self,
        role: str,
    ) -> None:


        allowed_roles = {

            "admin",

            "manager",

            "employee",

        }


        if role not in allowed_roles:

            raise ValueError(
                "Invalid user role."
            )