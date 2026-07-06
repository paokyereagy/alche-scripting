#!/usr/bin/env ruby

input = ARGV[0]

regex = /^hbt+n$/

if input && input.match?(regex)
  puts "#{input}"
else
  puts ""
end
