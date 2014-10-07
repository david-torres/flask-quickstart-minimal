class Config(object):
    DEBUG = False
    SECRET_KEY = ''

class ProductionConfig(Config):
    SECRET_KEY = 'N\xdc\xeb\x17\x9a\x16\x91\\\x16\xc0u\x8b\xd2n\xc5\xfe!\xf2\x8723\xd3\x90\t'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'i\x96\xce\x0b\x1f\x8a\xa5\xab\x86\x7f\x0f\xeb\xe4\x04P\xb9Z\xee\xff\xfd\xb4#\xb9\x19'
