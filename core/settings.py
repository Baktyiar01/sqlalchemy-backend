import os

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:user@localhost/db_sqlalchemy_backend'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'z%)5g$t3e48ex2a^a*yg!m-xlqm3_0en*)n!_f*8lua@1ykvq^'

EXCEL_FILE_DIRECTORY = os.getenv('EXCEL_FILE_DIRECTORY')