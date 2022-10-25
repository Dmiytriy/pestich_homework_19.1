from app.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()


    def create_user(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, data):
        uid = data.get('id')

        self.session.query(User).filter(User.id == uid).update(data)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()

    def get_user_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).jon_or_none()
        return user
