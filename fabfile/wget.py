from fabric.api import *
from fabric.decorators import task

@task
def install_wget():
    sudo('yum install -y wget')
