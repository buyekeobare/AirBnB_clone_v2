#!/usr/bin/python3
"""
A script that generates a .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime
from time import strftime 


def do_pack():
    """Generate a tar gzipped archive of the directory web_static"""

     filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None

