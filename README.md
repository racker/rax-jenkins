#rax-jenkins

##Introduction
This is a fork of the autoscale-chef repo, with many large parts removed from that repo to focus on bringing up Jenkins master/slave machines.

##Servers
You'll need to spin up at least two Linux (Ubuntu) servers, one to act as master and one to act as a slave to run the actual jobs.  Obviously you can have more than one slave machine.

Create a local `.ssh/chef.config` file (NOT on the remote servers where you're going to install Jenkins) and put your servers in it.  It's a good idea to separate out Chef related SSH entries from the standard ones in your `.ssh/config`.

Example:

	Host 10.10.10.10
		user root
		IdentityFile /Users/ltorvalds/.ssh/id_rsa
		
	Host project-foobar-jenkins-master
		user root
		IdentityFile /Users/gvanrossum/.ssh/id_rsa
		Hostname 10.10.10.10

**Highly Recommended**

Add an SSH public key to the root user on the remote servers, in `.ssh/authorized_keys`, so you do not have to continually provide a password when running the bootstrapper.

##Set Up
1. You will need to create a Github `racker/secure` entry for the rax-jenkins folder.  Follow the instructions in the README at [https://github.com/racker/secure](https://github.com/racker/secure)

2. Once you have access, from within the `secure` repo:

		$ ./handler.py -d -s rax-jenkins
		
	The `data_bag_secret_key.txt` will be decrypted to the `rax-jenkins/` directory.  Move it to some location outside of the repo on your local machine (i.e. `/etc/chef/`)

3. Checkout the `racker/rax-jenkins` repo

4. Change the `bootstrap.py` to reflect where you put the `data_bag_secret_key.txt`

5. Follow the README instructions in the `nodes` directory for creating node JSON file

## Run
Simply run `./bootstrap.py`

	$ ./bootstrap.py -H 10.10.10.10
	
	or
	
	$ ./bootstrap.py -H mywidget-jenkins-master








