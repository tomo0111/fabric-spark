from fabric.api import *
from fabric.contrib.files import append
from fabric.decorators import task

@task
def install_spark():
    sudo('wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz -P /tmp')
    sudo('tar xf /tmp/spark-2.0.0-bin-hadoop2.7.tgz')
    sudo('mkdir /usr/local/spark')
    sudo('cp -r /tmp/spark-2.0.0-bin-hadoop2.7/* /usr/local/spark')

def setup_spark():
    append('~/.bash_profile',
           'SPARK_EXAMPLES_JAR=/usr/local/spark/examples/jars/spark-examples_2.11-2.0.0.jar',
           use_sudo=True
    )

    append('~/.bash_profile',
           'PATH=$PATH:$HOME/bin:/usr/local/spark/bin',
           use_sudo=True
    )
    sudo('source .bash_profile')