sudoers = Array.new

search(:users, "*:*") do |u|
  if u.has_key?('dev') and not node.roles.include?('dev')
    next
  end

  dir = "/home/#{u['id']}"

  group u['id'] do
    gid u['gid']
  end

  user u['id'] do
    uid u['uid']
    gid u['gid']
    shell u['shell']
    comment u['comment']
    supports :manage_home => true
    home dir
  end

  directory "#{dir}/.ssh" do
    owner u['uid']
    group u['gid']
    mode "0700"
  end

  if u['ssh_keys'].any?
    template "#{dir}/.ssh/authorized_keys" do
      source "authorized_keys.erb"
      owner u['id']
      group u['gid']
      mode "0600"
      variables :ssh_keys => u['ssh_keys']
    end
  end

  sudoers << u['id'] if u['groups'].include?("sudo")

end

group "sudo" do
  gid 27
  members sudoers.sort
end

template "/etc/sudoers" do
  source "sudoers.erb"
  owner "root"
  group "root"
  mode 0440
end
