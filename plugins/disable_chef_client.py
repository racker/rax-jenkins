from fabric.api import sudo, hide


def execute(node):
    "Stops and disables chef-client from starting up"

    with hide('everything'):
        sudo('/etc/init.d/chef-client stop')
        sudo('update-rc.d chef-client disable')
