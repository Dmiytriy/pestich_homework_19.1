from app.dao.director import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_directors(self):

        return self.dao.get_all()

    def get_director(self, did):

        return self.dao.get_one(did)

    def create_director(self, data):

        return self.dao.create_director(data)

    def update_director(self, data):

        return self.dao.update_director(data)

    def delete_director(self, did):

        self.dao.delete_director(did)
