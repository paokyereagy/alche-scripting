#!/usr/bin/env ruby
input = ARGV[0]

if input.nil?
  puts "Usage: ruby script.rb <string>"
  exit
end

regex = /t{2,5}/

if input =~ regex
  puts "Match found!"
else
  puts "No match found."
end
