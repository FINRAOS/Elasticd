__author__ = 'patelm'

import logging
from elasticd.datastore import Datastore


class InmemoryDatastore(Datastore):
    """Inmemory implementation of the Datastore.  Will use an in memory list to keep track of all the backends
    """

    backend_ip_addresses = []

    def __init__(self, config):
        Datastore.__init__(self, config)

    def add_backend(self, ip_address):
        Datastore.add_backend(self, ip_address)
        self.backend_ip_addresses.append(ip_address)

    def remove_backend(self, ip_address):
        Datastore.remove_backend(self, ip_address)
        self.backend_ip_addresses.remove(ip_address)

    def get_all_backends(self):
        Datastore.get_all_backends(self)




