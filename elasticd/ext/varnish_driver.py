from elasticd.plugins import Driver

from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader

import os

import logging

class VarnishDriver(Driver):
    def __init__(self, config):
        Driver.__init__(self, config)

    def update(self, current_state):
        Driver.update(self, current_state)

        #loader = jinja2.FileSystemLoader(os.path.realpath(__file__) + '/../templates/')
        env = Environment(loader=FileSystemLoader('/Users/k24042/Sites/elasticd_github/templates'))
        # @todo - Ben - Make a config param for this.
        template = env.get_template('backend.vcl')
        #template = Template('Hello {{ name }}!')

        template_values = {
            'name': 'Ben'
        }

        rendered_result = template.render(template_values)

        # Save to file.
        # @todo - Ben - Make a config param for where to save to.

        print rendered_result
