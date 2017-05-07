from ambari_commons import OSCheck

import os

from resource_management.libraries.functions import format
from resource_management.libraries.functions.version import format_stack_version
from resource_management.libraries.functions.default import default
from resource_management.libraries.functions.stack_features import check_stack_feature
from resource_management.libraries.functions import get_kinit_path
from resource_management.libraries.functions import StackFeature
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions.expect import expect

from resource_management.libraries.functions.format import format

import commands
import os.path

config = Script.get_config()
tmp_dir = Script.get_tmp_dir()

# cldb props
cldb_master = config['clusterHostInfo']['cldb_hosts'][0]
cldb_cluster_name =config['configurations']['mfs-site']['mfs.cluster.name']


mapr_pid = '/opt/mapr/pid/warden.pid'


# mfs disks
mfs_disk = config['configurations']['mfs-site']['mfs.datanode.dir']


# Mapr installer strings
mapr_serv_configure = '/opt/mapr/server/configure.sh -C '

# Zookeeper properties
zookeeper_host = config['clusterHostInfo']['zookeeper_hosts'][0]
zk_client_port = config['configurations']['zoo.cfg']['clientPort']


# node excludes
exclude_packages = ["mapr-cldb", "mapr-webserver", "mapr-zookeeper"]