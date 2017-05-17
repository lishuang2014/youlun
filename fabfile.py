from __future__ import with_statement
from fabric.api import run, env, cd

env.hosts = '127.0.0.1'
env.password = 'web'
env.user = 'web'
env.port = 11235

PROJECT_DIR = 'workspace/youlun'


def pull_code():
    with cd(PROJECT_DIR):
        run('git pull origin master')


def update_virtualenv():
    with cd(PROJECT_DIR):
        run('pip install -r requirements.txt')


def collectstatic():
    with cd(PROJECT_DIR):
        run('echo "python manage.py collectstatic"')


def migrations():
    with cd(PROJECT_DIR):
        run('python manage.py migrate')


def reload_service():
    run('touch web-uwsgi.ini')
