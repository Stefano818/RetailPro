from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db


    def create(
        self,
        user: User,
    ) -> User:

        self.db.add(user)

        self.db.flush()

        return user



    def get_all(
        self,
    ) -> list[User]:

        statement = (
            select(User)
            .order_by(User.name)
        )

        return list(
            self.db.scalars(statement).all()
        )



    def get_active(
        self,
    ) -> list[User]:

        statement = (
            select(User)
            .where(
                User.is_active.is_(True)
            )
            .order_by(User.name)
        )

        return list(
            self.db.scalars(statement).all()
        )



    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:

        statement = (
            select(User)
            .where(
                User.id == user_id
            )
        )

        return self.db.scalar(statement)



    def get_by_email(
        self,
        email: str,
    ) -> User | None:

        statement = (
            select(User)
            .where(
                User.email == email
            )
        )

        return self.db.scalar(statement)



    def get_by_dni(
        self,
        dni: str,
    ) -> User | None:

        statement = (
            select(User)
            .where(
                User.dni == dni
            )
        )

        return self.db.scalar(statement)



    def search(
        self,
        search_term: str,
    ) -> list[User]:

        statement = (
            select(User)
            .where(
                or_(
                    User.name.ilike(
                        f"%{search_term}%"
                    ),
                    User.email.ilike(
                        f"%{search_term}%"
                    ),
                    User.dni.ilike(
                        f"%{search_term}%"
                    ),
                )
            )
            .order_by(User.name)
        )


        return list(
            self.db.scalars(statement).all()
        )



    def get_by_role(
        self,
        role: str,
    ) -> list[User]:

        statement = (
            select(User)
            .where(
                User.role == role,
                User.is_active.is_(True),
            )
            .order_by(User.name)
        )


        return list(
            self.db.scalars(statement).all()
        )



    def update(
        self,
        user: User,
    ) -> User:

        self.db.flush()

        return user



    def delete(
        self,
        user: User,
    ) -> User:

        user.is_active = False

        self.db.flush()

        return user



    def restore(
        self,
        user: User,
    ) -> User:

        user.is_active = True

        self.db.flush()

        return user



    def exists_email(
        self,
        email: str,
    ) -> bool:

        return (
            self.get_by_email(email)
            is not None
        )



    def exists_dni(
        self,
        dni: str,
    ) -> bool:

        return (
            self.get_by_dni(dni)
            is not None
        )



    def count(
        self,
    ) -> int:

        statement = select(
            func.count(User.id)
        )

        return (
            self.db.scalar(statement)
            or 0
        )