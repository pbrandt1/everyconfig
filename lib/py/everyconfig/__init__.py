import yaml
from easydict import EasyDict as edict
import sys
import inspect, os
import collections

def everyconfig(folder):
    env = os.getenv('CONFIG_ENV', 'default')

    if not os.path.isabs(folder):
        base = os.path.dirname(os.path.realpath(inspect.getmodule(inspect.stack()[1][0]).__file__))
        folder = os.path.join(base, folder)

    if os.path.exists(os.path.join(folder, 'default.yaml')):
        defaults = yaml.load(open(os.path.join(folder, 'default.yaml')).read())
    else:
        defaults = {}

    if os.path.exists(os.path.join(folder, env + '.yaml')):
        envConfig = yaml.load(open(os.path.join(folder, env + '.yaml')).read())
        defaults = _update(defaults, envConfig)
    
    return edict(defaults)

def _update(d, u):
    for k, v in u.iteritems():
        if isinstance(v, collections.Mapping):
            r = _update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d
