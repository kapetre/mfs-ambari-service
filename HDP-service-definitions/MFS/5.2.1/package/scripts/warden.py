import sys, os, pwd, signal, time
from resource_management import *
from resource_management.core.base import Fail
from resource_management.core.exceptions import ComponentIsNotRunning
from subprocess import call


import cPickle as pickle

class warden(Script):

    def install(self, env):
        import params

        #self.install_packages(env)
        # no op
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

        cmd = 'service mapr-warden stop'

        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)



    def status(self, env):
        import params
        pid_file = params.warden_pid
        check_process_status(pid_file)



if __name__ == "__main__":
    warden().execute()
