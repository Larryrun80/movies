import os

from flask import Flask, g

# override default flask json encoder if necessary
# write your code in your_app/models/jsonencoder.py
from .models.framework.jsonencoder import FlaskJSONEncoder

app_name = __name__
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
try:
    # read enviroment settings, see code in distribute/start.sh
    # run source ./distribute/start.sh in your flask dir
    # you can also set enviroment variables manually insttand of run start.sh
    app.config.from_envvar('APP_CONFIG_FILE')
except:
    pass
app.basedir = os.path.abspath(os.path.dirname(__file__))
app.json_encoder = FlaskJSONEncoder

# open this if your app need markdown support
# see detail and install from https://pythonhosted.org/Flask-Markdown/
# from flaskext.markdown import Markdown
# Markdown(app)

# open this if your app need send mail support
# see detail and install from https://pythonhosted.org/Flask-Mail/
# from flask_mail import Mail
# mail = Mail(app)

# open this if your app need a profile support to find bottlenecks
# see detail and install from https://github.com/fengsp/flask-profile
# maybe https://github.com/muatik/flask-profiler is better
# from flask.ext.profile import Profiler
# Profiler(app)

# open this if your app need DebugToolbar support
# see detail and install from
# https://flask-debugtoolbar.readthedocs.io/en/latest/
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

# # bcrypt
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt(app)


# Blueprint
from .views.movies import movies

app.register_blueprint(movies, url_prefix='/movies')

# # error page
# @app.errorhandler(404)
# def file_not_found(error):
#     return render_template('error/404.html'), 404

# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('error/500.html'), 500

# error log
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    # if mail infomation is set
    if 'MAIL_USERNAME' in app.config.keys()\
            and 'MAIL_PASSWORD' in app.config.keys():
        credentials = (app.config['MAIL_USERNAME'],
                       app.config['MAIL_PASSWORD'])
        mail_handler = SMTPHandler((app.config['MAIL_SERVER'],
                                    app.config['MAIL_PORT']),
                                   app.config['MAIL_DEFAULT_SENDER'],
                                   app.config['ADMIN_MAIL'],
                                   '{} failure'.format(app_name),
                                   credentials)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    from logging.handlers import TimedRotatingFileHandler
    log_file = '{dir}/{file}'.format(dir=app.basedir,
                                     file=app.config['ERROR_LOG'])
    if not os.path.exists(os.path.split(log_file)[0]):
        os.makedirs(os.path.split(log_file)[0])
    file_handler = TimedRotatingFileHandler(log_file,
                                            when='midnight',
                                            interval=1,
                                            backupCount=0)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('{} startup'.format(app_name))
