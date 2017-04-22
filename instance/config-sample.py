# secret keys
# itsdangerous will use SECRET_KEY to safely serialize user token
# set SECRET_KEY enough complex and enough long
# you can keep SALTs as default or change to anything you like
# SECRET_KEY = 'your-secret-key'
# CONFIRM_SALT = 'email-confirm-key'
# RECOVER_SALT = 'password-recover-key'
# CODE_SALT = 'code-salt'

# email settings password
# corresponding to sms settings in config file
MAIL_PASSWORD = 'your-email-password'

# mysql settings
# remove it if you do not use mysql
HOST = 'mysql-host'
PORT = '3306'
USER = 'mysql-user'
PASSWD = 'mysql-password'
DB = 'mysql-database'
CHARSET = 'utf8'

# mongodb settings
# remove it if you do not use mongodb
HOST = 'mongodb-host'
USER = 'mongodb-user'
PASSWD = 'mongodb-password'
PORT = '27017'
DB = 'mongodb-database'

# sms settings password
# corresponding to sms settings in config file
SMS_PWD = 'your-sms-password'
