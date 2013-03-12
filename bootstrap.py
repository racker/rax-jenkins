#!/usr/bin/env python

from optparse import OptionParser
from littlechef import runner as lc
from ssh.config import SSHConfig as _SSHConfig
import os

def main():
    parser = OptionParser()
    parser.add_option("-u", "--username", default="root",
        help="username for new server, defaults to %default")
    parser.add_option("-p", "--password", dest="password",
        help="password for new server")
    parser.add_option("-H", "--hostname", dest="hostname",
        help="hostname or ip of new server")

    (options, args) = parser.parse_args()

    # begin hackery to load config file until littlechef gets fixed (04DEC2012)

    ssh_config = "~/.ssh/chef.config"
    lc.env.use_ssh_config = True
    lc.env.ssh_config = _SSHConfig()
    lc.env.ssh_config_path = os.path.expanduser(ssh_config)

    lc.env.user = options.username
    lc.env.password = options.password
    lc.env.host_string = options.hostname
    lc.env.host = options.hostname
    lc.env.node_work_path = "/tmp/chef-solo"
    lc.env.encrypted_data_bag_secret = "/etc/chef/data_bag_secret_key"
    lc.env.follow_symlinks = False

    # We need the ohai plugins installed before running Chef
    lc.plugin("install_omnibus_chef")
    lc.node(options.hostname)

if __name__=="__main__":
    main()
