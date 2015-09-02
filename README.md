# everyconfig
Use the same .yaml config files in every programming language

## motivation
Have you ever had to use javascript AND python AND ruby and talk to the same db?  Yeah, it's really annoying to keep track of all your configuration changes across all your files in all your languages.  So now you can just have one folder with `default.yaml`, `test.yaml`, and `production.yaml` or whatever you want to call your environments.

## usage
* Make a folder called `config` or something.
* Create a file `default.yaml` in that foldera. ex:
```yaml
mongodb:
  url: localhost
  db: test
  port: 27017
```
* Create some more environment configs, for example `production.yaml`
* Set the `CONFIG_ENV` env variable to your preferred env
* Use the module for the language you want and point to the relative path to the config folder you created

## js
```javascript
var config = require('everyconfig')('./config')
console.log(config.mongodb.url)
```
(note that you can use `NODE_ENV` instead of `CONFIG_ENV` if you want)

## python
```python
from everyconfig import everyconfig
config = everyconfig('./config')
print config.mongodb.url
```

## ruby
```ruby
require 'everyconfig'
config = Everyconfig.load('./config')
puts c['mongodb']
```
