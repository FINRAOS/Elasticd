from elasticd.locator import ResourceLocator
import boto


class AWSinstanceLocator(ResourceLocator):
    def __init__(self, config):
        ResourceLocator.__init__(self, config)

    def get_resources(self):
        ResourceLocator.get_resources(self)
        ec2 = boto.connect_ec2()
        #search for the backend servers
        #todo read the filter from configuration
        reservations = ec2.get_all_instances(filters={'tag:AGS': 'fnrw',
                                                      'tag:SDLC': 'DEV',
                                                      'tag:Purpose': 'finra.org_drupal',
                                                      'instance-state-name': 'running'})
        instances = [i for reservation in reservations for i in reservation.instances]
        backends = []
        for server in instances:
            ip_address = server.private_ip_address
            backends.append(ip_address)

        return backends


