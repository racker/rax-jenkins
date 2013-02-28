import subprocess
import os
import json

from fabric.api import env, sudo, abort, hide

from littlechef import chef, lib

def execute(node):
  "Uses ohai to get cloud info and save to the node"

  with hide('everything'):
    ohai = json.loads(sudo('ohai'))
  if not len(ohai):
    print("Not a cloud node, skipping")
    return
  node['cloud'] = ohai['cloud']
  del node['name']
  os.remove(chef.save_config(node, True))
