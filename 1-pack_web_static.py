#!/usr/bin/python3
"""
A script that generates a .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime
from time import strftime 


def do_pack():
    """Generate a tar gzipped archive of the directory web_static"""
    current = datetime.current().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(current)

    local("mkdir -p versions")

    archived = local("tar -cvzf {} web_static".format(archive))

    if archived.return_code != 0:
        return None
    else:
        return archive


