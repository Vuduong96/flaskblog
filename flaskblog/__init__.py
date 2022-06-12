from flaskblog import confidential
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail




conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(confidential.dbuser, confidential.dbpass, confidential.dbhost, confidential.dbname)

app = Flask(__name__)
app.config['SECRET_KEY'] = '43b2a30aa627f539c748cda0d7615d6a'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app) #app
bcrypt = Bcrypt(app) #app
login_manager = LoginManager(app)
login_manager.login_view = 'login' #function name of our route
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = confidential.myEmail
app.config['MAIL_PASSWORD'] = confidential.myPassword
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



from flaskblog import routes


