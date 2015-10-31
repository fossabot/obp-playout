#!/usr/bin/env python
import sys
from fabric.api import local, settings, abort, run, cd, env, put, hide, sudo
from fabric.colors import green, red, yellow, cyan, blue
from fabric.contrib import files
from fabric.operations import prompt
import urllib2
from contextlib import contextmanager as _contextmanager

env.warn_only = True
env.debug = False
env.supervisor = '/etc/supervisor/conf.d'

"""
definition instances
"""
def pypo():
    env.hosts = [
        'pypo-dev',
    ]
    env.git_url = 'https://github.com/hzlf/pypo.git'
    env.git_branch = 'development'
    env.path = '/home/playout/pypo'
    env.virtualenv_path = '/home/playout/env/pypo'
    env.user = 'root'
    env.sudo_user = 'playout'

def deploy():

    print(green('*' * 72))
    print(green('deploying to %s on %s' % (env.path, ' - '.join(env.hosts))))
    print(green('repository: %s' % env.git_url))
    print(green('branch: %s' % env.git_branch))
    print(green('*' * 72))

    print
    if not prompt('ARE YOU 100% SURE TO CONTINUE?: [y/N]', default='n').lower() == 'y':
        print(red('Deployment aborted by user'))
        print
        sys.exit(1)

    check_connection()

    if not files.exists(env.path):
        print(red('*' * 72))
        print(red('Target directory %s does not exist.' % env.path))
        print(red('Did you already run "fab pypo init"?'))
        print(red('*' * 72))
        print
        sys.exit(1)

    with cd(env.path):
        sudo('whoami', user=env.sudo_user)

    with cd(env.path):

        try:
            sudo('rm -Rf src_new', user=env.sudo_user)
        except Exception, e:
            pass

        sudo('mkdir src_new', user=env.sudo_user)


    with cd(env.path + '/src_new'):
        print green('repository checkout. %s on %s' % (env.git_branch, env.git_url))
        sudo('git init', user=env.sudo_user)
        sudo('git remote add -t %s -f origin %s' % (env.git_branch, env.git_url), user=env.sudo_user)
        sudo('git fetch', user=env.sudo_user)
        sudo('git checkout %s' % (env.git_branch), user=env.sudo_user)



        sudo('ls -hal', user=env.sudo_user)




    with cd(env.path):
        try:
            print green('creating virtualenv at: %s' % env.virtualenv_path)
            if not files.exists('%s' % env.virtualenv_path):
                sudo('virtualenv %s' % env.virtualenv_path, user=env.sudo_user)
            else:
                print yellow('virtualenv exists')
        except Exception, e:
            print red('unable to create virtualenv: %s' % e)

        print green('installing requirements')
        sudo('%s/bin/pip install --upgrade -r %s' % (env.virtualenv_path, 'src_new/pypo/requirements.txt'))






    with cd(env.path):
        print green('swap directories')
        try:
            sudo('mv src src_old', user=env.sudo_user)
        except Exception, e:
            print red('unable to move directories: %s' % e)
        try:
            sudo('mv src_new src', user=env.sudo_user)
        except Exception, e:
            print red('unable to move directory: %s' % e)



    try:
        print green('linking supervisord config')
        if not files.exists('%s/playout.supervised.conf' % (env.supervisor)):
            run('ln -s %s/src/conf/playout.supervised.conf %s/playout.supervised.conf' % (env.path, env.supervisor))

    except Exception, e:
        print e
        pass


    with cd(env.path):
        print green('remove old source')
        try:
            run('rm -R src_old')
        except Exception, e:
            print red('unable to remove directory: %s' % e)







def init():

    print(green('*' * 72))
    print(green('Initial Installation to %s ' % (env.path)))
    print(green('*' * 72))
    print

    if not prompt('ARE YOU 100% SURE TO CONTINUE?: [y/N]', default='n').lower() == 'y':
        sys.exit(1)

    try:
        print green('creating project directory: %s' % env.path)
        if not files.exists(env.path):
            sudo('mkdir -p %s' % env.path, user=env.sudo_user)
        else:
            print red('directory exists: %s' % env.path)
            if not prompt('do you want to continue and overwrite the directory?', default='n').lower() == 'y':
                sys.exit()

    except Exception, e:
        print red('unable to create project directory: %s' % e)




"""
helper functins
"""
def check_connection():

    print(cyan('Checking connection'))
    try:
        run('uname -r')
    except Exception, e:
        print(red('*' * 72))
        print(red('Unable to run remote command. Connected??'))
        print(red('*' * 72))
        sys.exit()