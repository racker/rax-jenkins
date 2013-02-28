import os

from littlechef import chef

from vmrunwrapper import VmrunWrapper, get_config


def execute(node):
    """
    Uses vmrunwrapper to get the IP fo the vm - assumes that the config file
    is all set up and it is either in ~/.vmrunwrapper.conf or the environment
    variable VMRUNWRAPPER_CONF points to it
    """
    wrapper = VmrunWrapper(get_config())
    ip = None

    try:
        ip = wrapper.update_ssh_config()
    except:
        pass

    if ip is None:
        print "Warning: could not get IP address from node {0}".format(
            node['name'])

    print "Node {0} has IP {1}".format(node['name'], ip)

    # Update with the ipaddress field in the corresponding node.json
    node['ipaddress'] = ip
    os.remove(chef.save_config(node, ip))
