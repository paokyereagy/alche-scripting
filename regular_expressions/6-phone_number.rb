#!/usr/bin/env ruby
phone_number = ARGV[0]

if phone_number.nil?
  puts "Usage: ruby script.rb <10_digit_number>"
  exit
end

regex = /^\d{10}$/

if phone_number.match?(regex)
  puts "#{phone_number}"
else
  puts ""
end
