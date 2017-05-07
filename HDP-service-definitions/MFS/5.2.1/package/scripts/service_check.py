"""
Gracefully inspired by the apache license over on
https://github.com/apache/ambari/blob/branch-2.4.0/ambari-server/src/main/resources/common-services/KERBEROS/1.10.3-10/package/scripts/service_check.py


"""

from resource_management import *
import sys
import ambari_simplejson as json # simplejson is much faster comparing to Python 2.6 json module and has the same functions set.
import re
import subprocess
from ambari_commons import os_utils
from ambari_commons import OSConst
from ambari_commons.os_family_impl import OsFamilyImpl
from resource_management.libraries.functions import StackFeature
from resource_management.libraries.functions.stack_features import check_stack_feature
from resource_management.libraries.functions.get_user_call_output import get_user_call_output
from resource_management.core.exceptions import Fail
from resource_management.core.logger import Logger



class ServiceCheck(Script):
    def service_check(self, env):

        import params
        env.set_params(params)


        # warden_satus = "# warden status command?"
        #try:
         #   Execute(warden_status)
        pass



if __name__ == "__main__":
    ServiceCheck().execute()
