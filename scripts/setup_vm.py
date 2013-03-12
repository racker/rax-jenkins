import os
import time

import littlechef
from littlechef import runner
from plumbum import cli, local, FG

# github.com/racker/vmrunwrapper
import vmrunwrapper

image_url = "http://04dc1fe0f852314a412a-59cce4bc2c52fb076478833b4d47755d.r41.cf1.rackcdn.com/stretch.tar.gz"

script_location = os.path.dirname(os.path.abspath(__file__))


def parse_littlechef_config(wrapper, path=None):
    """
    Parse littlechef "config.cfg"
    """
    littlechef.CONFIGFILE = path or os.path.join(os.path.dirname(__file__),
                                                                 'config.cfg')
    runner._readconfig()
    wrapper.username = runner.env.user


def download_vm(download_to):
    """
    Downloads the VM image
    """
    if os.path.exists(download_to):
        print "VMware image already downloaded."
    else:
        # download the image
        print "Downloading VM image..."
        local['curl']['-o', download_to, image_url] & FG


def get_vm(wrapper):
    """
    Downloads the VM image, copies it to the right location, and takes a
    snapshot.

    If a VM image already exists at the target, shuts that VM down, takes a
    snapshot, and moves it to a backup location before setting up the new VM
    image.
    """
    download_to = os.path.join(script_location, 'stretch.tar.gz')
    download_vm(download_to)

    # make sure the image can be moved into the vmware image directory
    target = os.path.dirname(wrapper.image_location)

    if not os.path.exists(vmrunwrapper.image_locations):
        print "- Making {0} directory.".format(vmrunwrapper.image_locations)
        os.makedirs(vmrunwrapper.image_locations)

    if os.path.exists(target):
        backup = 'stretch.{0}.backup.vmwarevm'.format(time.time())
        print "! stretch.vmwarevm already exists - moving it to {0}".format(
            backup)

        # shut down the old vm
        if wrapper.is_running():
            wrapper.snapshot("Pre_retiring_image")
            wrapper.down()

        # move the vm to a different location
        os.rename(target, os.path.join(vmrunwrapper.image_locations, backup))

    # move the image to the vmware images directory
    print "* Extracting {0} to {1}".format(download_to,
                                         vmrunwrapper.image_locations)
    local['tar']('-C', vmrunwrapper.image_locations, '-xzf', download_to)

    wrapper.snapshot("Post_download")


def save_config(wrapper):
    config_path = os.path.join(script_location, "vmrunwrapper.conf")
    link_path = os.path.expanduser('~/.vmrunwrapper.conf')
    wrapper.save_config(config_path)
    if os.path.exists(link_path):
        if os.path.realpath(link_path) != config_path:
            print "!!"
            print "~/.vmrunwrapper.conf already exists - can't link it."
            print ("Either you should manually link it, or you should set in "
                   "an .bashrc file or a .virtualenv/bin/activate file the "
                   "environment variable $VMRUNWRAPPER_CONF to point to {0}"
                   ).format(config_path)
            print "!!"
    else:
        os.symlink(config_path, link_path)


def initialize_vm(wrapper):
    """
    The VM should have already been downloaded.  This generates SSH keys for
    the user, copies them over, starts the VM, and uses littlechef to bootstrap
    chef solo and required packages.

    Also, it links whatever directories are specified.
    """
    wrapper.generate_ssh_key()

    save_config(wrapper)

    wrapper.start()
    wrapper.copy_ssh_key(password=runner.env.password)
    wrapper.ssh_config(comment=False)

    runner.env.host_string = wrapper.host
    runner.env.host = wrapper.host

    # deploy chef
    runner.plugin("install_omnibus_chef")

    wrapper.snapshot("Post_Chef-Solo_Install")

    # run chef-solo and otherwise set up the node
    local.env["VMRUNWRAPPER_CONF"] = os.path.join(
        script_location, "vmrunwrapper.conf")
    local.env["PATH"] += ":{0}".format(script_location)

    local['vmwrap']['up'] & FG

    # take a snapshot
    wrapper.snapshot("Post_Littlechef_Bootstrap")


class AutoscaleDevSetupCLI(cli.Application):
    """
    Command line arguments pointing to the relevant secure git repo and the
    autoscale repo must be provided, if there are no links in the parent
    directory.
    """

    DESCRIPTION = (
        "Sets up the autoscale development VMware VM.  Also takes additional "
        "space-separated share arguments in the form of: \n\n"
        "\t<path to directory to be shared>:<share name>\n\n"
        "or\n\n"
        "\t<path to directory to be shared>")

    def main(self, *args):
        wrapper = vmrunwrapper.VmrunWrapper("stretch", host='vmware')
        # The littlechef parser will set up littlechef correctly, but if the
        # .ssh config file doesn't already exist, there will be an error.
        # Therefore, create one if specified and if it doesn't exist.
        if not os.path.exists(wrapper.ssh_config_path):
            with open(wrapper.ssh_config_path, 'wb') as f:
                f.write('');

        parse_littlechef_config(wrapper)

        get_vm(wrapper)
        initialize_vm(wrapper)


if __name__ == "__main__":
    AutoscaleDevSetupCLI.run()
