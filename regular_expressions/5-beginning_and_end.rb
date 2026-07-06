#!/usr/bin/env ruby

input = ARGV[0]

if input.nil?
  puts "Usage: ruby script.rb <string>"
  exit
end

regex = /^h.n$/

if input.match?(regex)
  puts "#{input}"
else
  puts ""
end
