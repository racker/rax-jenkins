This directory contains some scripts for working with a VMware Fusion dev vm.


# Setting up a VMWare image for use

* Download the base ubuntu 12.04 server image and install with whatever user
  and password has been configured in `scripts/config.cfg`

* The base ubuntu 12.04 server image is missing curl.  These tools need curl.

* Remove some network config files, or when someone uses the image networking
  will fail: `sudo rm /etc/udev/rules.d/*-persistent-net.rules`.

  TL;DR reason why, as far as I understand it, from reading [this thread](http://communities.vmware.com/thread/46069?start=0&tstart=0):
  Lucid seems to tie the ethernet address to a MAC address - when this image is
  copied/moved around, a new UUID is generated and the MAC address changes,
  and the distro doesn't know where to find the interface because the eth0
  device that is loaded by the driver differs in MAC address from the device
  listed in the configuration (remembered by Udev). If you remove the
  persistent net rules, when someone copies this image and uses it, a new
  device entry for eth0 with the new MAC address should be generated.

  @jayofdoom says that the persistent net rules is pretty common, so this
  applies to future versions of ubuntu as well and can be expected to do so
  for a long time.

* Shutdown the vm immediately.  `sudo shutdown -h now`.  If the VM gets
  restarted again, the previous instruction will probably have to be run again
  from inside the vm.

* From the host machine, go into the vmware image directory (e.g.
  `~/Documents/Virtual\ Machines.localized/[vm name].vmwarevm`) and
  `rm -rf *.lck` to remove all lock files

* Tar up the vmware image directory for distribution.

* Update the setup script to download the new vmware image.
