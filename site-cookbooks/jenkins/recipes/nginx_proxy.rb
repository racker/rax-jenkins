
include_recipe "nginx"
include_recipe "ssl_certs"

ssl_certs node["jenkins"]["cert_name"]

template "/etc/nginx/sites-available/jenkins" do
  source "jenkins.nginx.erb"
  notifies :reload, "service[nginx]", :delayed
end

nginx_site "jenkins" do
  action :enable
end

firewall_rule "nginx_http" do
  port 80
  protocol :tcp
  action :allow
end

firewall_rule "nginx_https" do
  port 443
  protocol :tcp
  action :allow
end

