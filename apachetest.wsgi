#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/apache_test/")
sys.path.insert(0,"/var/www/apache_test/apache_test/")

import logging
logging.basicConfig(stream=sys.stderr)

from apache_test import app as application
