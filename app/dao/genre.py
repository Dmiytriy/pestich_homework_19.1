from app.dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre_created = Genre(**data)
        self.session.add(genre_created)
        self.session.commit()
        return genre_created

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, data):
        gid = data.get('id')
        self.session.query(Genre).filter(Genre.id == gid).update(data)
        self.session.commit()
