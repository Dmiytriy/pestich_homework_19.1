from app.config import Config

PWD_HASH_SALT = b'secret'
PWD_HASH_ITERATIONS = 1000
algo = 'HS256'
secret = Config().SECRET_WERE
