#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """script that generates a .tgz archive """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_" + date + ".tgz"
    arv_path = local("tar -cvzf {} web_static".format(name))
    if arv_path.failed:
        return None
    return arv_path
