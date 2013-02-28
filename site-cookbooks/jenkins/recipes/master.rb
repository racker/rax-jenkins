
include_recipe "jenkins::default"

dbag = Chef::EncryptedDataBagItem.load("ssh_keys", "jenkins")

package "jenkins" do
  action :install
end

# Github keys
directory "/var/lib/jenkins/.ssh" do
  owner "jenkins"
  mode 0755
end
cookbook_file "/var/lib/jenkins/.ssh/known_hosts" do
  owner "jenkins"
  mode 0600
end
file "/var/lib/jenkins/.ssh/id_rsa" do
  owner "jenkins"
  content dbag["private"]
  mode 0600
end
file "/var/lib/jenkins/.ssh/id_rsa.pub" do
  owner "jenkins"
  content dbag["public"]
  mode 0644
end

