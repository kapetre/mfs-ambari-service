import sys, os, pwd, signal, time
from resource_management import *
from resource_management.core.base import Fail
from resource_management.core.exceptions import ComponentIsNotRunning
from subprocess import call


import cPickle as pickle

class fileserver(Script):

    def install(self, env):
        import params

        self.install_packages(env)

        # Run Mapr Configure
        import params

        # Run Mapr Configure
        cmd = params.mapr_serv_configure + ' -C ' + params.cldb_master + ' -Z '+ params.mapr_zookeeper_host+':'+params.mapr_zk_client_port + ' -N ' +params.cldb_cluster_name +  ' -D ' + params.mfs_disk
        Execute('echo "Running ' + cmd + '"')
        Execute(cmd)

        self.configure(env)

    def configure(self, env):
        import params
        env.set_params(params)


    #Call start.sh to start the service
    def start(self, env):
        import params

        cmd = 'service mapr-warden start'

        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    def stop(self, env):
        import params

        cmd = 'service mapr-mfs stop '

        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

        cmd = 'service mapr-nfsserver stop'

        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)


    def status(self, env):
        import params
        pid_file = params.mapr_pid
        check_process_status(pid_file)



if __name__ == "__main__":
    fileserver().execute()
