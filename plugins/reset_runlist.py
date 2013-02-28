import subprocess
import os
import json

from fabric.api import env, sudo, abort, hide

from littlechef import chef, lib

def execute(node):
  node['run_list'] = ["role[base]"]
  del node['name']
  os.remove(chef.save_config(node, True))

