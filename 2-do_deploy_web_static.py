#!/usr/bin/python3
"""
Script generates a .tgz archive from web_static folder
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.237.69.6', '54.158.6.195']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers,
    using the function do_deploy
    """
    if exists(archive_path) is False:
        return False

    start = archive_path.find("web_static")
    end = archive_path.find(".tgz")
    # Getting filename withouth extension
    fname_wout_e = archive_path[start:end]
    # Getting filename with extension
    fname_we = archive_path[start:]

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(fname_wout_e))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(fname_we, fname_wout_e))
        run("rm /tmp/{}".format(fname_we))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_sta\
tic/releases/{}/".format(fname_wout_e, fname_wout_e))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(fname_wout_e))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(fname_wout_e))
        return True
    except Exception:
        return False
