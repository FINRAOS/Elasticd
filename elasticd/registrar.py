__author__ = 'patelm'

import logging


class Registrar():
    datastore = None
    driver = None

    def __init__(self, datastore, driver):
        self.datastore = datastore
        self.driver = driver

    def set_datastore(self, datastore):
        self.datastore = datastore

    def register(self):
        logging.debug('do register')


    def deregister(self):
        logging.debug('do deregister')

