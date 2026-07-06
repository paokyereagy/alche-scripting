#!/usr/bin/env ruby
input = ARGV[0]

if input.nil?
  puts "Usage: ruby script.rb <string>"
  exit
end

# Regex: ^hbt{2,5}n$ ensures the structure is exact
regex = /^hbt{2,5}n$/

if input.match?(regex)
  puts "#{input}"
else
  puts ""
end
