task :test_json_files do
  require "find"
  require "json"

  JSON.create_id = nil # Disables json_class serialization
  Find.find("data_bags", "roles", "nodes") do |path|
      if path[-4..-1] == "json"
          begin
              JSON.parse(File.read(path))
          rescue JSON::ParserError => e
              puts "Error in #{path}: #{e.message}"
              exit(1)
          end
      else
          next
      end
  end
end

task :test_cookbooks do
  unless system("knife cookbook test -a") then
    puts "Knife tests failed, exiting"
    exit 1
  end
end

desc "Validate JSON and Cookbook syntax"
task :test => [:test_json_files, :test_cookbooks]


desc "Installs/updates the python and ruby requirements, and sets up/updates the git submodules"
task :update do
  system("bundle install")
  system("pip install -r requirements.txt")
  system("librarian-chef install")
end


desc "Install the requirements necessary to set up an otter development VM"
task :install_dev_requirements do
  system("pip install -r scripts/requirements.txt")
end

desc "Sets up the otter development VM - assume requirements are installed"
task :devvm_setup do
  path_update = "PATH=#{Dir.pwd}/scripts:$PATH"
  system("python scripts/setup_vm.py")
  system("#{path_update} vmwrap up")
end

desc "Installs requirements necessary for, and also sets up, the otter development VM"
task :otterdev => [:install_dev_requirements, :devvm_setup]

desc "runs rake update"
task :default => [:update]
