__author__ = 'patelm'

import logging
from elasticd.datastore import Datastore


class InmemoryDatastore(Datastore):
    def __init__(self, config):
        Datastore.__init__(self, config)

    def add_backend(self):
        Datastore.add_backend(self)
