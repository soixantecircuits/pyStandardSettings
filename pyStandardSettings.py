#!/usr/bin/env python
import json
import argparse
from dotmap import DotMap
import os
import helpers

settings_files = ["settings/settings.default.json", "settings/settings.json"]
settings = {}

# get available settings from settings.default.json
try:
  with open(settings_files[0]) as settings_file:
      nestedArguments = json.load(settings_file)
except IOError:
  pass

arguments = []
helpers.flatArguments(arguments, nestedArguments)

# init parser
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--settings', help='settings file in json format')
for argument in arguments:
  parser.add_argument(argument)

# parse
args = parser.parse_args()
if args.settings:
  settings_files.append(args.settings)

# get settings from files
for file in settings_files:
  try:
    with open(file) as setting_file:
        helpers.dict_merge(settings, json.load(setting_file))
  except IOError:
    pass

# merge with argv
parsedArgs = helpers.nestArguments(vars(args))
helpers.dict_merge(settings, parsedArgs)

# merge with env
env_lower = dict((k.lower(), v) for k,v in os.environ.iteritems())
parsedEnv = helpers.nestArguments(env_lower, '_')
helpers.dict_merge(settings, parsedEnv)

settings = DotMap(settings)

