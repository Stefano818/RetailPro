from app.auth.password import verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:

    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository



    def login(
        self,
        email: str,
        password: str,
    ) -> User:


        email = email.strip().lower()



        if not email:

            raise ValueError(
                "Email is required."
            )


        if not password:

            raise ValueError(
                "Password is required."
            )



        user = (
            self.user_repository
            .get_by_email(email)
        )



        if not user:

            raise ValueError(
                "Invalid credentials."
            )



        if not verify_password(
            password,
            user.password_hash,
        ):

            raise ValueError(
                "Invalid credentials."
            )



        if not user.is_active:

            raise ValueError(
                "User account is inactive."
            )



        return user


    def has_role(
        self,
        user: User,
        role: str,
    ) -> bool:

        return user.role == role



    def has_any_role(
        self,
        user: User,
        roles: list[str],
    ) -> bool:

        return user.role in roles