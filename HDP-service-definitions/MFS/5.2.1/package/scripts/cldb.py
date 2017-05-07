#import status properties defined in -env.xml file from status_params class
import sys, os, pwd, signal, time
from resource_management import *
from resource_management.core.base import Fail
from resource_management.core.exceptions import ComponentIsNotRunning
from subprocess import call
import cPickle as pickle

class cldb(Script):

  #Call setup.sh to install the service
  def install(self, env):

    import params
    # Install packages listed in metainfo.xml
    self.install_packages(env)

    # Run Mapr Configure
    #cmd = params.mapr_serv_configure + params.cldb_master + ' -Z '+ params.zookeeper_host+':'+params.zk_client_port + ' -N ' +params.cldb_cluster_name +  ' -D ' + params.mfs_disk
    #Execute('echo "Running ' + cmd + '"')
    #Execute(cmd)


    self.configure(env)

  def configure(self, env):
    import params

    env.set_params(params)



  def start(self, env):
    import params

    cmd = 'systemctl start mapr-cldb'

    Execute('echo "Running cmd: ' + cmd + '"')
    Execute(cmd)


  def stop(self, env):
    import params

    cmd = 'systemctl stop mapr-cldb'

    Execute('echo "Running cmd: ' + cmd + '"')
    Execute(cmd)

  def status(self, env):
    import params

    import params
    pid_file = params.cldb_pid
    check_process_status(pid_file)

if __name__ == "__main__":
  cldb().execute()
