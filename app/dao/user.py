from app.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_name):
        return self.session.query(User).filter(User.username == user_name).one()

    def delete_user(self, user_name):
        user = self.get_one(user_name)

        self.session.delete(user)
        self.session.commit()

    def update_user(self, data, username):
        self.session.query(User).filter(User.username == username).update(data)
        self.session.commit()

    def get_all(self):
        users = self.session.query(User).all()
        return users

    def create_user(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user



