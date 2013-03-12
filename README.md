# Autoscaling Chef

Chef repo for the [Stretch Autoscaling][1] project.

# First time setup

## Required environment
1. POSIX environment (only tested on Mac OS for now)
1. Ruby, rubygems, and bundler: [rbenv](https://github.com/sstephenson/rbenv)
   is recommended.
1. The `bundler` and `rake` gems
   directory)
1. Python >= 2.6 ([virtualenv](virtualenv.org) is highly recommended)
1. [pip](https://pypi.python.org/pypi/pip)

Note that this may not be a complete list.

## Required tools
1. [chef](http://wiki.opscode.com/display/chef/Home)
1. [littlechef](https://github.com/tobami/littlechef) >= 1.4.1
1. [librarian](https://github.com/applicationsonline/librarian)

You can run `rake` or `rake update` in the autoscaling-chef root directory to
install these requirements and set up the submodules.

This task just runs:
```
bundle install
pip install -r requirements.txt
librarian-chef install
```

## Required repositories

The two repos that must be checked out in addition to autoscaling chef are the
encrypted data bag repo and the otter (autoscaling code) repo.  These must be
symlinked to `autoscaling-chef/shared/secure` and
`autoscaling-chef/shared/otter`, respectively.

* Encrypted Data Bags:

    To handle Encrypted Data Bags the encrypted data bag secret is checked into
    https://github.com/racker/secure/.

    Follow the instructions there to checkout secure and get access to the
    encrypted_data_bag_secret.txt.  The checkout should then be symlinked to
    `autoscaling-chef/shared/secure`.

* Autoscaling:

    The actual autoscaling code is at https://github.com/racker/otter.
    Checkout the repository, and simply symlink it to
    `autoscaling-chef/shared/otter`.


# Updating the chef repo
1. `git pull origin master` on autoscaling-chef
1. If there has been an update to the `Cheffile`, run `librarian-chef install`
    to set up any new submodules (important: install, not update)
1. If there has been an update to `requirements.txt`, run
    `pip install -r requirements.txt` to update any python package requirements

Alternately, just run `rake` or `rake update` again.


# Dev VM setup

## Requires Tools
1. [Vmware Fusion 5.0](http://www.vmware.com/)
1. [plumbum](https://github.com/tomerfiliba/plumbum)
1. [vmrunwrapper](http://github.com/racker/vmrunwrapper)

VMWare Fusion needs to be installed manually.

To install the other requirements, see below.

## Setting up a new VM

The setup script for the development VM will download a VM image for you,
install chef on it, and run the `dev` role on the VM, provided that the script
is able to locate required repositories and that all the requirements above are
met.

1. Ensure that the [secure][3] repo has been checked out and set up as
    specified above (the appropriate files are decrypted).
1. Ensure that the [otter][2] repo and the [secure][3] repo can are symlinked
    to `autoscaling-chef/shared` as specified above.
1. From the top of the autoscaling-chef repo, run `rake otterdev`, which will:
    1. Download and install the required tools, above.
    1. Run the setup script: `python scripts/setup_vm.py`
    1. Temporarily add the `scripts` directory to the PATH and run `vmwrap up`
        again - cassandra doesn't start on the first setup run, but running
        chef again (by running `vmwrap up`) will get it going.

1. Once that's done, add the `scripts` directory to your PATH more permanently
    so that vmwrap up will work in the future.

To just install/update the dev VM requirements, you can just run `rake
install_dev_requirements`.

To just install the dev VM without the requirements, you can just run `rake
devvm_setup`

## Using vmrunwrapper commands after setup

The setup script will attempt to link `scripts/vmrunwrapper.conf` (which gets
generated during setup) to `~/.vmrunwrapper.conf`.  If this fails, please
either link it manually, or set the environment variable VMRUNWRAPPER_CONF to point to `scripts/vmrunwrapper.conf`.

This is needed in order for vmrunwrapper to know which VM you want to manipulate.  For more information see the README for [vmrunwrapper](http://github.com/racker/vmrunwrapper).

Then, in order to be able to use the command `vmwrap up`, make sure
`scripts/vmwrap-up` is accessible via your PATH (i.e. don't just `alias` it).
This way, `vmwrap up` (run from anywhere) should do approximately the same
thing `vagrant up` would do for a VirtualBox VM.

Put this somewhere in your `.bashrc`, `.zshrc`, or virtualenv's `bin/activate`:
`export PATH=<chef repo>/scripts:$PATH`


## Updating the VM after updating the autoscaling-chef repo
1. If `scripts/requirements.txt` has been updated, run
    `pip install -r scripts/requirements.txt` or
    `rake install_dev_requirements`
1. Run `vmwrap up`


[1]: https://one.rackspace.com/display/Stretch/Home
[2]: https://github.com/racker/otter/
[3]: https://github.com/racker/secure/
