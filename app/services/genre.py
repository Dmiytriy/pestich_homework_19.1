from app.dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_genres(self):

        return self.dao.get_all()

    def get_genre(self, gid):

        return self.dao.get_one(gid)

    def create_genre(self, data):

        return self.dao.create(data)

    def update_genre(self, data):

        return self.dao.update(data)

    def delete_genre(self, gid):

        self.dao.delete(gid)
