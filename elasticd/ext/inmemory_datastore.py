__author__ = 'patelm'

import logging
from elasticd.plugins import Datastore
from elasticd.resource import Resource
from sets import Set


class InmemoryDatastore(Datastore):
    """Inmemory implementation of the Datastore.  Will use an in memory list to keep track of all the backends
    """

    resources = []

    def __init__(self, config):
        Datastore.__init__(self, config)

    def add_backend(self, resource):
        Datastore.add_backend(self, resource)
        _backends = self.get_all_backends()
        self.resources.append(resource)

    def remove_backend(self, resource):
        Datastore.remove_backend(self, resource)
        self.resources.remove(resource)

    def remove_all_backends(self):
        self.resources = []

    def get_all_backends(self):
        Datastore.get_all_backends(self)
        return self.resources
