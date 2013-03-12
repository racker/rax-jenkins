include_recipe "firewall"

firewall "ufw" do
  action :enable
end

firewall_rule "ssh" do
  port 22
  action :allow
end

if node["network"]["interfaces"]["eth2"]
  firewall_rule "cloud_network" do
    interface "eth2"
    action :allow
  end
end
