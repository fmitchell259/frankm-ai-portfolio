# We initialise our application here.
from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
mail = Mail()

app = Flask(__name__)
csrf.init_app(app)

SECRET_KEY = '18de3ad64bc23690b114ee8ebb1a35a0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site123.db'

data_base = SQLAlchemy(app)

# We need to import our routes after the app.
# This is due to the package structure and to
# avoid circular imports.

from showcase_site import routes

# Set up image folder variable to display images on HTML pages.

img_folder = os.path.join('static', 'images')
anim_folder = os.path.join('static', 'animations')
cv_folder = os.path.join('static/client', 'doc')

app.config['IMG_FOLDER'] = img_folder
app.config['ANIM_FOLDER'] = anim_folder
app.config['CV_FOLDER'] = cv_folder
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'harrybarrysally12345678@gmail.com'
app.config['MAIL_PASSWORD'] = 'HarryBarrySally123'
app.config['MAIL_USE_TLS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site_x.db'


mail.init_app(app)


