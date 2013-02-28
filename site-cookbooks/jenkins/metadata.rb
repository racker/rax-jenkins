maintainer       "Rackspace"
maintainer_email "phil.kates@rackspace.com"
license          "Apache 2.0"
description      "Installs/Configures Jenkins-CI"
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          "0.0.1"

depends "apt"
depends "nginx"
depends "firewall"
depends "ssl_certs"
