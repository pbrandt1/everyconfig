#!/usr/bin/env python
import sys
sys.path.append('../../lib/py')
from everyconfig import everyconfig

c = everyconfig('../config')

print c

print c.mongodb
