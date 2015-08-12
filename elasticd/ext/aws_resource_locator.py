from elasticd.plugins import ResourceLocator
from elasticd.resource import IPResource
import boto
import yaml
import os

class AWSinstanceLocator(ResourceLocator):
    _dataMap = None

    def __init__(self, config):
        ResourceLocator.__init__(self, config)
        fpath = os.path.dirname(__file__) + "/" + self._get_config_value('aws_config')
        f = open(fpath)
        self._dataMap = yaml.safe_load(f)
        # todo: error handling of this file loading
        # todo: move to file loading utility
        f.close()
        
    def get_resources(self):
        ResourceLocator.get_resources(self)
        ec2 = boto.connect_ec2()
        #search for the backend servers

        # Build set of filters for instance lookup
        configItems = self._get_all_config_items()
        filterDict = {}

        # Add tag filters from config
        for ignore, kvmap in self._dataMap['aws_tags'].items():
            print kvmap['key'] + "=>" + kvmap['value']
            tagKey = "tag:" + kvmap['key']
            filterDict[tagKey] = kvmap['value']

        # Add instance state filter
        filterDict['instance-state-name'] = 'running'
        reservations = ec2.get_all_instances(filters = filterDict)
        instances = [i for reservation in reservations for i in reservation.instances]
        backends = []
        for server in instances:
            ip_address = IPResource(server.private_ip_address)
            backends.append(ip_address)

        return backends


