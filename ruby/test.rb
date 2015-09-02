#require 'yaml'

require 'everyconfig'

#defaults = YAML.load_file('../config/default.yaml')
#puts defaults.inspect

c = Everyconfig.load('../config')

puts c
puts c['mongodb']
