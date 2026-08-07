from app.database.database import SessionLocal

from app.repositories.user_repository import UserRepository

from app.services.user_service import UserService
from app.services.auth_service import AuthService



def test_auth():

    db = SessionLocal()


    try:

        user_repository = UserRepository(
            db
        )


        user_service = UserService(
            db,
            user_repository,
        )


        auth_service = AuthService(
            user_repository,
        )


        print("\n" + "=" * 50)
        print("AUTHENTICATION TEST")
        print("=" * 50)



        email = "test.user@retailpro.com"



        existing_user = (
            user_repository
            .get_by_email(email)
        )


        if existing_user:

            print(
                "Test user already exists."
            )

            user = existing_user


        else:

            user = user_service.create(

                name="Test User",

                dni="99999999",

                email=email,

                password="test_password",

                role="employee",

            )


            print(
                "User created successfully."
            )



        print(
            f"User ID: {user.id}"
        )

        print(
            f"Name: {user.name}"
        )

        print(
            f"Role: {user.role}"
        )



        print("\nTesting login...")



        logged_user = auth_service.login(

            email=email,

            password="test_password",

        )


        print(
            "Login successful."
        )


        print(
            f"Authenticated user: {logged_user.name}"
        )


        print(
            f"Role: {logged_user.role}"
        )



        print("\nTesting invalid password...")


        try:

            auth_service.login(

                email=email,

                password="wrong_password",

            )


        except ValueError as error:

            print(
                "Invalid password rejected."
            )

            print(
                error
            )



        print("\nTesting role...")


        if auth_service.has_role(
            logged_user,
            "employee",
        ):

            print(
                "Role validation successful."
            )


        print("\n" + "=" * 50)
        print("AUTH TEST COMPLETED SUCCESSFULLY")
        print("=" * 50)



    finally:

        db.close()



if __name__ == "__main__":

    test_auth()