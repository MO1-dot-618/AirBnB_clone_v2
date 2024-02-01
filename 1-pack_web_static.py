#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        local("mkdir -p versions")
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        local(f"tar -cvzf versions/{archive_name} web_static")
        return os.path.join("versions", archive_name)

    except Exception as e:
        return None

