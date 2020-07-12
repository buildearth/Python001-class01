import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# python解释器增加路径查找
sys.path.append(BASE_PATH)


# log文件存放地址
LOG_DIR = os.path.join(BASE_PATH, 'log')

standard_format = '[%(levelname)s][%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  ':%(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(BASE_PATH, 'log', 'error_log.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
