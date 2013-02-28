# Autoscaling Chef

Chef repo for the [Stretch Autoscaling][1] project.

# Required Tools
1. [chef](http://wiki.opscode.com/display/chef/Home)
2. [littlechef](https://github.com/tobami/littlechef) >= 1.4.0
3. [librarian](https://github.com/applicationsonline/librarian) - once
   librarian is installed, then run ``librarian-chef install`` in the main
   repo directory

# Required repositories

The two repos that must be checked out in addition to autoscaling chef are the
encrypted data bag repo and the otter (autoscaling code) repo.  These must be
symlinked to `autoscaling-chef/shared/secure` and
`autoscaling-chef/shared/otter`, respectively.

## Encrypted Data Bags:

To handle Encrypted Data Bags the encrypted data bag secret is checked into
https://github.com/racker/secure/.

Follow the instructions there to checkout secure and get access to the
encrypted_data_bag_secret.txt.  The checkout should then be symlinked to `autoscaling-chef/shared/secure`.

## Autoscaling:

The actual autoscaling code is at https://github.com/racker/otter.  Checkout
the repository, and simply symlink it to `autoscaling-chef/shared/otter`.

# Dev VM setup

**Requires**: [Vmware Fusion 5.0](http://www.vmware.com/)

The setup script for the development VM will download a VM image for you,
install chef on it, and run the `dev` role on the VM, provided that the script
is able to locate required repositories and that all the requirements above are
met.

**Instructions**:

1. Download and install the required tools, above.
1. Download the latest [vmrunwrapper](http://github.com/racker/vmrunwrapper)
    and install it.
1. Ensure that the [secure][3] repo has been checked out and set up as
    specified above (the appropriate files are decrypted).
1. Ensure that the [otter][2] repo and the [secure][3] repo can are symlinked
    to `autoscaling-chef/shared` as specified above.
1. From the top of the autoscaling-chef repo, run: `python scripts/setup_vm.py`


[1]: https://one.rackspace.com/display/Stretch/Home
[2]: https://github.com/racker/otter/
[3]: https://github.com/racker/secure/
