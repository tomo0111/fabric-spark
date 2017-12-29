from fabric.api import *
from fabric.contrib.files import append
from fabric.decorators import task

@task
def install_scala():
    sudo('wget http://www.scala-lang.org/files/archive/scala-2.10.1.tgz -P /tmp')
    sudo('tar tar xvf /tmp/scala-2.10.1.tgz')
    sudo('mv /tmp/scala-2.10.1 /usr/lib')
    sudo('ln -s /usr/lib/scala-2.10.1 /usr/lib/scala')
    sudo('export PATH=$PATH:/usr/lib/scala/bin')

def setup_scala():
    append('~/.bash_profile', 'PATH=$PATH:/usr/lib/scala/bin', use_sudo=True)