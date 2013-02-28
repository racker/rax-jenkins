import subprocess
import os
import json

from fabric.api import env, sudo, abort, hide

from littlechef import chef, lib

def execute(node):
  "Uses ohai to get cloud info and save to the node"

  with hide('everything'):
    ohai = json.loads(sudo('ohai -d /etc/chef/ohai_plugins'))
  if not len(ohai):
    print("No network? This is wrong")
    return
  del(ohai['network']['interfaces'])
  node['network'] = ohai['network']
  del node['name']
  os.remove(chef.save_config(node, True))

