# everyconfig
Use the same .yaml config files in every programming language

## usage
Set up your config files in a directory like this:
```
.
├── config
|   ├── default.yaml
|   ├── production.yaml
|   └── test.yaml
├── foo
|   ├── foo.js
|   └── blue.js
└── bar
    ├── something.py
    └── post.py
```
Then set `CONFIG_ENV` to one of the names of your yaml files, like so: `CONFIG_ENV=production node app.js`

The best part is that all of your configs inherit the default values from default.yaml.

_default.yaml_:
```yaml
db:
  url: 'localhost'
  port: 27017
```

_production.yaml_:
```yaml
db:
  url: 'some.internal.dns'
```
resulting config for `CONFIG_ENV=production`:
```yaml
db:
  url: 'some.internal.dns'
  port: 27017
```

## node.js
```javascript
var config = require('everyconfig')('./config')
console.log(config.mongodb.url)
```
(note that you can use `NODE_ENV` instead of `CONFIG_ENV` with node.js if you want)

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
puts c['mongodb']['url']
```

## bash
*from https://gist.github.com/pkuczynski/8665367 (note that if you use four space indents, your variables will be separated by two underscores instead of one)*

```bash
everyconfig <config dir> <variable prefix>
```

```bash
source $path_to_everyconfig/bash/everyconfig.sh

# you should use an absolute path for the directory that holds your config files
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

#           directory        prefix
everyconfig "$DIR"/../config CONFIG_
echo $CONFIG_mongodb_url
```
## contact me
Send me a pr or an email 😀
