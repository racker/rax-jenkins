
search(:node, '*:*').each do |n|
  if n['network'] && n['network']['ipaddress_eth2']
    hostsfile_entry n['network']['ipaddress_eth2'] do
      hostname "#{n['hostname']}.int #{n['hostname']}"
      comment 'Appended by otter::hosts'
      action :create
    end
  end
end

