
include_recipe "chef_handler::default"

chef_gem "chef-gelf" do
    action :install
end

require 'chef/gelf'

chef_handler "Chef::GELF::Handler" do
	source "chef/gelf"
	arguments({
		:server => node["graylog2"]["syslog_listen_address"],
		:host => node.hostname
	})
	supports :exception => true, :report => true
end.run_action(:enable)
