Jenkins master example.

An appropriate `.ssh/chef-config` entry was made, so that is used for the "name" value.  The file will reside in `nodes/mywidget-jenkins-master.json`

	{
	    "ipaddress": "10.10.10.10",
	    "name": "mywidget-jenkins-master",
	    "run_list": [
	        "role[base]",
	        "role[jenkins_master]"
	    ]
	}

Jenkins slave example #1.

No FQDN or `.ssh/chef-config` exists, so the IP is used for the "name".  The file will reside in `nodes/10.10.10.11.json`

	{
	    "ipaddress": "10.10.10.11",
	    "name": "10.10.10.11",
	    "run_list": [
	        "role[base]",
	        "role[jenkins_slave]"
	    ]
	}
	
Jenkins slave example #2.

A FQDN exists, and is used for the "name".  The file will reside in `nodes/mywidget-jenkins-slave02.example.com.json`

	{
	    "ipaddress": "10.10.10.11",
	    "name": "mywidget-jenkins-slave02.example.com",
	    "run_list": [
	        "role[base]",
	        "role[jenkins_slave]"
	    ]
	}