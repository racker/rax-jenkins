action :create do
  name = new_resource.name
  domain = name.gsub(/\.+/, "_")
  dbag_name = new_resource.data_bag
  cert = new_resource.certificate
  gd = new_resource.gd_bundle

  # TODO: This will need to be moved to support the delete action
  dbag = Chef::EncryptedDataBagItem.load("ssl_certs", domain)

  file "#{node[:ssl_certs][:base_path]}/certs/#{name}.crt" do
    owner "root"
    group "root"
    mode 0644
    content dbag["certificate"]
  end
  file "#{node[:ssl_certs][:base_path]}/certs/#{name}_bundle.crt" do
    owner "root"
    group "root"
    mode 0644
    content dbag["gd_bundle"]
  end

  file "#{node[:ssl_certs][:base_path]}/private/#{name}.key" do
    owner "root"
    group "root"
    mode 0600
    content dbag["private_key"]
  end

  file "#{node[:ssl_certs][:base_path]}/certs/#{name}_chain.crt" do
    owner "root"
    group "root"
    mode 0644
    content [dbag["certificate"], dbag["gd_bundle"]].join("\n")
  end
end

action :delete do
end
