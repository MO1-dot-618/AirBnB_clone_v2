#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["52.201.186.156", "52.3.240.185"]
env.user = "ubuntu"


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

def do_deploy(archive_path):
    """ Deploying files """
    if os.path.exists(archive_path):
        archive_name = os.path.basename(archive_path)
        new_path  = "/data/web_static/releases/" + archive_name[:-4]
        tmp_path = "/tmp/" + archive_name

        """Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/")

        """Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server"""
        run("sudo mkdir -p {}".format(tmp_path))
        run("sudo tar -xzf {} -C {}/".format(file_path, new_path))

        """Delete the archive from the web server"""
        run("sudo rm {}".format(tmp_path))

        """Delete the symbolic link /data/web_static/current from the web server"""
        run("sudo rm -rf /data/web_static/current")

        """Create a new the symbolic link """
        run("sudo ln -s {} /data/web_static/current".format(new_path))

        print("New version deployed!")
        return True

    return False

def deploy():
    """Full deployment"""
    creat_arch = do_pack()
    if creat_arch is None:
        return False
    return do_deploy(creat_arch)
