import socket
hostname = socket.gethostname()

config = {
    # This is just a key to tell the fedmsg-hub to initialize us.
    'summershum.enabled': True,
    'summershum.sqlalchemy.url': 'sqlite:////var/tmp/summershum.sqlite',

    # Here is where we will publish our status
    'endpoints': {
        'summershum.%s' % hostname: [
            "tcp://127.0.0.1:99887",
        ],
    },
    'logging': {
        'loggers': {
            'summershum': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False
            },
        },
    },
}
