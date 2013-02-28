from optparse import OptionParser
from littlechef import runner as lc

parser = OptionParser()
parser.add_option("-u", "--username", default="root",
    help="username for new server, defaults to %default")
parser.add_option("-p", "--password", dest="password",
    help="password for new server")
parser.add_option("-H", "--hostname", dest="hostname",
    help="hostname or ip of new server")

(options, args) = parser.parse_args()

lc.env.user = options.username
lc.env.password = options.password
lc.env.host_string = options.hostname
lc.env.host = options.hostname
lc.env.node_work_path = "/tmp/chef-solo"

# We need the ohai plugins installed before running Chef
lc.plugin("install_omnibus_chef")
lc.role("bootstrap")
lc.plugin("save_network")
lc.plugin("save_cloud")
lc.plugin("reset_runlist")
lc.node(options.hostname)
