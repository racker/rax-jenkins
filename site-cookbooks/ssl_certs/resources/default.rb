
actions :create, :delete

attribute :name, :kind_of => String, :name_attribute => true
attribute :data_bag, :kind_of => String, :default => nil
attribute :certificate, :kind_of => String, :default => nil
attribute :private_key, :kind_of => String, :default => nil
attribute :gd_bundle, :kind_of => String, :default => nil

def initialize(name, run_context=nil)
  super
  @action = :create
end
