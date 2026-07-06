#!/usr/bin/env ruby

# The input is the first command-line argument
log_entry = ARGV[0]

if log_entry.nil?
  puts "Usage: ruby 8-textme.rb '<log_entry>'"
  exit
end

# Regex to capture content from [from:], [to:], and [flags:]
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Match the regex against the log entry
match_data = log_entry.match(regex)

if match_data
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]

  # Print formatted output
  puts "#{sender},#{receiver},#{flags}"
else
  puts ""
end
