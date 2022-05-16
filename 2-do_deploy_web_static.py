#!/usr/bin/python3
"""
Script generates a .tgz archive from web_static folder
"""
from fabric.api import local, run, put, env
from datetime import datetime
from os import path


env.hosts = ['35.237.69.6', '54.158.6.195']
env.user = 'ubuntu'


def do_deploy(archive_path):
    '''
    Distributes an archive to your web servers
    '''
    if path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            filename = archive_path[9:]
            no_ext = filename[:-4]
            dir_name = '/data/web_static/releases/' + no_ext + '/'
            run('mkdir -p ' + dir_name)
            run('sudo tar -xzf /tmp/' + filename + ' -C ' + dir_name)
            run('rm -f /tmp/' + filename)
            run('sudo mv ' + dir_name + '/web_static/* ' + dir_name)
            run('rm -rf /data/web_static/current')
            run('ln -s ' + dir_name + ' /data/web_static/current')
            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False
