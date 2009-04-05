#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import wsgiref.handlers
import os
import logging
import math
from google.appengine.api import users
from datetime import datetime
from datetime import timedelta

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class HomePage(webapp.RequestHandler):
    def get(self):
        template_file = 'index.html'
        template_values = {
            'greetings': 'ciao'
        }
        logging.info(template_file)
        '''path = os.path.join(os.path.dirname(__file__), os.path.join('site', template_file))'''
        path = os.path.join(os.path.dirname(__file__), os.path.join('templates', 'find_me.html'))
        self.response.out.write(template.render(path, template_values))

def main():
  application = webapp.WSGIApplication([('/', HomePage)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
