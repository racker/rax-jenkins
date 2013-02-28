#
# Author:: Joshua Timberman (<joshua@opscode.com>)
# Copyright:: Copyright (c) 2011 Opscode, Inc.
# License:: Apache License, Version 2.0
# Modified:: Phil Kates (<phil.kates@rackspace.com>)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

provides "network"

require "open-uri"

require_plugin "hostname"
require_plugin "#{os}::network"

ip_providers = %w{
  http://icanhazip.com
  http://ip.appspot.com
  http://ifconfig.me/ip
}

begin
  provider = ip_providers.pop
  ip = open(provider).read.chomp
  if ip.match(/\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/)
    network["ipaddress_nat"] = ip
    Ohai::Log.debug("Using #{network["ipaddress_nat"]}} as the external IP address")
  else
    raise "Not a valid IP format"
  end
rescue
  retry unless ip_providers.empty?
  Ohai::Log.debug("Could not determine external IP via #{provider}")
end

network
