maintainer       "Rackspace"
maintainer_email "cooks@lists.rackspace.com"
license          "Apache 2.0"
description      "Firewall rules for common services."
long_description "Firewall rules for common services, so we can use pristine upstream cookbooks"
version          "1.0.0"
depends          "firewall"

recipe "firewall-rules::default", "Firewall rules for the most common services."

