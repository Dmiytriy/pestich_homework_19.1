from app.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create_director(self, data):
        director_created = Director(**data)
        self.session.add(director_created)
        self.session.commit()
        return director_created

    def delete_director(self, did):
        director = self.get_director(did)
        self.session.delete(director)
        self.session.commit()

    def update_director(self, data):
        did = data.get('id')
        self.session.query(Director).filter(Director.id == did).update(data)
        self.session.commit()