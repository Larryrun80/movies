class AppError(Exception):

    # General Error
    TYPE_ERROR = {
        'code': 100001,
        'msg': 'param type error, "{param}" should be "{expect_type}"'
    }

    # Databases
    DB_INIT_ERROR = {
        'code': 200001,
        'msg': 'init database error: {reason}'
    }

    def __init__(self, name, **kargs):
        if name not in dir(self):
            raise RuntimeError('Undefined App Error found: {}'.format(name))

        self.error = getattr(self, name)
        if kargs:
            self.error['msg'] = str.format(self.error['msg'], **kargs)

    def __str__(self):
        return repr(self.error.msg)
