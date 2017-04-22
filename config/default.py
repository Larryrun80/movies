DEBUG = False
BCRYPT_LEVEL = 12

# service mail
# used to receive user mail or crash mail, not necessary
SERVICE_MAIL = 'service@77tech.biz'
ADMIN_MAIL = 'service@77tech.biz'

# email service settings
# MX settings if your app needs send mail
# crash report, user register mail, etc.
# service mail
MAIL_SERVER = 'hwsmtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_MAX_EMAILS = None

MAIL_USERNAME = "service@77tech.biz"
MAIL_DEFAULT_SENDER = "service@77tech.biz"

# Debug tools
# using Flask-DebugToolbar
# see https://flask-debugtoolbar.readthedocs.io/en/latest/
# need pip install flask-debugtoolbar
# not necessary
DEBUG_TB_INTERCEPT_REDIRECTS = False

# error info dir
ERROR_LOG = 'logs/error.log'
