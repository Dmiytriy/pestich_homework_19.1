from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.services.authentification import AuthentificaionService
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService
from setup_db import db
from dao.user import UserDAO
from services.user import UserService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthentificaionService(user_service)
