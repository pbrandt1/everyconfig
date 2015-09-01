#!/usr/bin/env python
from everyconfig import everyconfig

c = everyconfig('../../config')

print c

print c.mongodb.url
