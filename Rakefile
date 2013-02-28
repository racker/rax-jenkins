
require "find"
require "json"

task :test_json_files do
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
