from elasticd.plugins import ResourceLocator
from elasticd.resource import IPResource


class MockResourceLocator(ResourceLocator):
    def __init__(self, config):
        ResourceLocator.__init__(self, config)

    def get_resources(self):
        ResourceLocator.get_resources(self)

        backends = [IPResource('10.0.0.1'), IPResource('10.0.0.2'), IPResource('10.0.0.3')]

        return backends
