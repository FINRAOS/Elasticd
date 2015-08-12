import logging

from elasticd.plugins import Datastore


class SqliteDatastore(Datastore):
    def __init__(self, config):
        Datastore.__init__(self, config)
        logging.debug('sqlite datasource started')

    def add_backend(self, ip_address):
        Datastore.add_backend(self, ip_address)

