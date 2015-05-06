__author__ = 'patelm'

import logging


class Registrar():
    """Responsible for registering/deregistering backends and informing the Driver with the latest information

        Uses the datastore to keep track of known backends
        Call the driver with the latest known state of the backends
    """

    datastore = None
    driver = None

    def __init__(self, datastore, driver):
        """
        Args:
            datastore (Datastore): Datastore plugin to use when storing backend ip addresses.
            driver (Driver): Driver plugin to use to update the frontend config.
        """
        self.datastore = datastore
        self.driver = driver

    def register(self, ip_address):
        """Register a new backend
        Args:
            ip_address (String): ip address of the backend.
        """
        self.datastore.add_backend(ip_address)
        logging.debug('do register')

    def deregister(self, ip_address):
        """remove a backend from the registry
        Args:
            ip_address (String): ip address of the backend.
        """
        self.datastore.remove_backend(ip_address)
        logging.debug('do deregister')

    def process(self):
        """Inform the driver of the current state of the backends

        """
        print 'informing the driver'
        backends = self.datastore.get_all_backends()
        self.driver.update(backends)

