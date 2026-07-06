#!/usr/bin/env ruby
input = ARGV[0].to_s
match = input.scan(/School/).join

if match.empty?
  puts ""
else
  puts "#{match}"
end
