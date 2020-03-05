import os
from loguru import logger

basedir = os.path.abspath(os.path.dirname(__file__))
logger.add(f"{basedir}/logs/stdout.log",
           format="{time:MM-DD HH:mm:ss} {level}-{name}-{module}-{line} {message}")

# DATABASE_URL=sqlite:///test.sqlite
# DATABASE_URL=postgresql://scott:tiger@localhost/mydatabase
# DATABASE_URL=mysql://scott:tiger@localhost/mydatabase
DATABASE_URL = 'postgresql+psycopg2://procloud:procloud@db/postgres'
SECRET_KEY = 'dRTsWNwlG0pbtPABjYoExQXZHu53DFz4'
UPLOAD_FOLDER = f'{basedir}/uploads/'
MAX_CONTENT_LENGTH = 1024 * 1024 * 1024

# mail settings
receiver = 'xx@xx.com'
sender = 'xx@xx.com'
password = 'password'
smtp_server = 'smtp.xx.com'

dev = True
