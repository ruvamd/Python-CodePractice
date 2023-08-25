from models import Session, User
from sqlalchemy.exc import IntegrityError

class UserManager:
    def create_user(self, username, password):
        session = Session()
        
        new_user = User(username=username, password=password)
        session.add(new_user)
        
        try:
            session.commit()
            print(f"User '{username}' created successfully.")
        except IntegrityError:
            session.rollback()
            print(f"Username '{username}' already exists. Please choose a different username.")
        finally:
            session.close()

    def login(self, username, password):
        session = Session()

        user = session.query(User).filter_by(username=username, password=password).first()

        if user:
            print(f"Welcome, {username}!")
            return user  # Return the User object
        else:
            print("Invalid credentials. Please check your username and password.")
            return None

