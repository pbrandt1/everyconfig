var yaml = require('js-yaml');
var fs = require('fs');
var debug = require('debug')('everyconfig')
var _ = require('lodash')
var path = require('path');

module.exports = function(folder) {
  var env = process.env.CONFIG_ENV || 'default';
  debug('env is %s', env)
  debug('folder specified: "%s"', folder)
  if (typeof folder !== 'string') {
    debug('js-yaml input file not recognized, defaulting to "./config" directory');
    throw new Error('Invalid configuration directory passed to everyconfig')
  }

  folder = path.resolve(path.dirname(module.parent.filename), folder);
  debug('resolved folder to %s', folder);

  try {
    fs.statSync(folder);
  } catch (e) {
    throw new Error('Could not find everyconfig folder ' + folder);
  }

  var defaultFile = path.join(folder, 'default.yaml');
  var envFile = path.join(folder, env + '.yaml');

  try {
    var defaults = yaml.safeLoad(fs.readFileSync(defaultFile));
  } catch (e) {
    debug('could not load default file %s', defaultFile);
    defaults = {};
  }

  if (env === 'default') { return defaults }

  try {
    var envconfig = yaml.safeLoad(fs.readFileSync(envFile));
  } catch (e) {
    debug('could not load env file %s', envFile);
    throw new Error('Could not load configuration for env ' + env);
  }

  return _.merge({}, defaults, envconfig);
}

