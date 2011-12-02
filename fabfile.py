from __future__ import with_statement
from fabric.api import *

path = '/webserver/buildouts/www.fhnw.ch'

def sync():
    with cd(path):
        sudo('bin/sync www.dev.fhnw.ch', user='zope')
