from flaskblog import confidential


class Config:
    conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(confidential.dbuser, confidential.dbpass, confidential.dbhost, confidential.dbname)
    SECRET_KEY = confidential.Secret_key
    SQLALCHEMY_DATABASE_URI = conn
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = confidential.myEmail
    MAIL_PASSWORD = confidential.myPassword
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
