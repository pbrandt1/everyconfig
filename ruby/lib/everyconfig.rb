require 'yaml'
require 'pathname'

class Everyconfig
  def self.load(folder)
    folder = Pathname.new folder
    env = ENV['CONFIG_ENV'] || 'default'

    begin
      defaults = YAML.load_file(File.join(folder, 'default.yaml'))
    rescue
      defaults = Hash.new
    end
    envConfig = YAML.load_file(File.join(folder, env + '.yaml'))
    return self.deep_merge(defaults, envConfig)
  end

  def self.deep_merge(first, second)
      merger = proc { |key, v1, v2| Hash === v1 && Hash === v2 ? v1.merge(v2, &merger) : v2 }
      first.merge(second, &merger)
  end

end
