#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/apachetest/")
sys.path.insert(0,"/var/www/apachetest/apachetest/")

import logging
logging.basicConfig(stream=sys.stderr)

from apachetest import app as application
