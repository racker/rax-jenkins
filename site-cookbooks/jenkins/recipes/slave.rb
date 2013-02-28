
include_recipe "java"

user "jenkins" do
  home "/home/jenkins"
  shell "/bin/bash"
  supports :manage_home => true
end

dbag = Chef::EncryptedDataBagItem.load("ssh_keys", "jenkins")

directory "/home/jenkins/.ssh" do
  owner "jenkins"
  group "jenkins"
  mode 0755
end
cookbook_file "/home/jenkins/.ssh/known_hosts" do
  owner "jenkins"
  group "jenkins"
  mode 0600
end
file "/home/jenkins/.ssh/id_rsa" do
  owner "jenkins"
  group "jenkins"
  content dbag["private"]
  mode 0600
end
file "/home/jenkins/.ssh/id_rsa.pub" do
  owner "jenkins"
  group "jenkins"
  content dbag["public"]
  mode 0644
end
file "/home/jenkins/.ssh/authorized_keys" do
  owner "jenkins"
  group "jenkins"
  content dbag["public"]
  mode 0644
end
