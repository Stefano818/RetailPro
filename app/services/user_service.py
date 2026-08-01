from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all(self) -> list[User]:
        return self.repository.get_all()

    def get_by_id(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)

        if not user:
            raise ValueError("User not found.")

        return user

    def get_by_email(self, email: str) -> User | None:
        email = email.strip().lower()

        return self.repository.get_by_email(email)

    def create(
        self,
        name: str,
        dni: str,
        email: str,
        password_hash: str,
        role: str = "employee",
    ) -> User:

        name = name.strip()
        dni = dni.strip()
        email = email.strip().lower()
        role = role.strip().lower()

        if not name:
            raise ValueError("User name is required.")

        if not dni:
            raise ValueError("User DNI is required.")

        if not email:
            raise ValueError("User email is required.")

        if not password_hash:
            raise ValueError("Password hash is required.")

        allowed_roles = {
            "admin",
            "manager",
            "employee",
        }

        if role not in allowed_roles:
            raise ValueError(
                "Invalid user role."
            )

        if self.repository.get_by_email(email):
            raise ValueError(
                "A user with this email already exists."
            )

        if self.repository.get_by_dni(dni):
            raise ValueError(
                "A user with this DNI already exists."
            )

        user = User(
            name=name,
            dni=dni,
            email=email,
            password_hash=password_hash,
            role=role,
        )

        return self.repository.create(user)

    def deactivate(self, user_id: int) -> User:
        user = self.get_by_id(user_id)

        user.is_active = False

        return self.repository.update(user)

    def activate(self, user_id: int) -> User:
        user = self.get_by_id(user_id)

        user.is_active = True

        return self.repository.update(user)