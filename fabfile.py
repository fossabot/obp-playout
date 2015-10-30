#!/usr/bin/env python
import sys
from fabric.api import local, settings, abort, run, cd, env, put, hide
from fabric.colors import green, red
from fabric.contrib import files

import urllib2

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
    env.user = 'root'

def deploy():

    print(green('*' * 72))
    print(green('deploying %s' % ' - '.join(env.hosts)))
    print(green('*' * 72))

