current_dir = File.dirname(__FILE__)
user = ENV['CHEF_USER'] || ENV['USER']

log_level                :info
log_location             STDOUT
cache_type               "BasicFile"
readme_format            "md"
cookbook_copyright       "Rackspace"
cookbook_license         "apachev2"

cookbook_path [ "#{current_dir}/../cookbooks", "#{current_dir}/../site-cookbooks" ]
data_bag_path "#{current_dir}/../data_bags"

knife[:data_bag_secret_file] = "/etc/chef/data_bag_secret_key"
