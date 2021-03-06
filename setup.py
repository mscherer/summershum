from setuptools import setup

setup(
    name='summershum',
    version='0.0.1',
    description='fedmsg consumer that extracts hashes of source files',
    author='Pierre-Yves Chibon & Ralph Bean',
    author_email='admin@fedoraproject.org',
    url='https://github.com/fedora-infra/summershum',
    install_requires=[
        "fedmsg",
        "sqlalchemy",
    ],
    packages=[
        'summershum',
    ],
    entry_points="""
    [moksha.consumer]
    summershumconsumer = summershum:SummerShumConsumer

    [console_scripts]
    summershum-cli = summershum.cli:main
    """,
)
