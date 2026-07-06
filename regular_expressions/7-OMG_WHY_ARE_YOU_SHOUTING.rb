#!/usr/bin/env ruby
input = ARGV.join(" ")

if input.empty?
  puts "Usage: ruby script.rb <string with words>"
  exit
end

regex = /\b[A-Z]+\b/

matches = input.scan(regex)

if matches.any?
  puts "#{matches.size}"
  puts matches.join(", ")
else
  puts ""
end
