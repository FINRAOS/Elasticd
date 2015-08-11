from elasticd.plugins import ResourceLocator
from elasticd.resource import IPResource
import boto



class AWSinstanceLocator(ResourceLocator):
    def __init__(self, config):
        ResourceLocator.__init__(self, config)

    def get_resources(self):
        ResourceLocator.get_resources(self)
        ec2 = boto.connect_ec2()
        #search for the backend servers

        # Build set of filters for instance lookup
        configItems = self._get_all_config_items()
        filterDict = {}

        # Add tag filters from config
        for item in configItems:
            if (item[0].startswith('aws_tag')):
                tagKey = "tag:" + item[0].split('_')[2] 
                filterDict[tagKey] = item[1] 
        

        # Add instance state filter
        filterDict['instance-state-name'] = 'running'
        reservations = ec2.get_all_instances(filters = filterDict)
        instances = [i for reservation in reservations for i in reservation.instances]
        backends = []
        for server in instances:
            ip_address = IPResource(server.private_ip_address)
            backends.append(ip_address)

        return backends


