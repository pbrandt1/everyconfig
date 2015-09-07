#!/bin/bash
source ./everyconfig.sh

# you should use an absolute path for the directory that holds your config files
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
everyconfig "$DIR"/../config CONFIG_

echo $CONFIG_mongodb_url
