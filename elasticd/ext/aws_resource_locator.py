from elasticd.locator import ResourceLocator


class AWSinstanceLocator(ResourceLocator):
    def __init__(self, config):
        ResourceLocator.__init__(self, config)

    def get_resources(self):
        ResourceLocator.get_resources(self)
        return ['192.168.0.1', '192.168.0.2']

