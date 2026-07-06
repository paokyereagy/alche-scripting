#!/usr/bin/env ruby

# Join all command-line arguments into one string to handle cases 
# where quotes might be missing or broken by the shell
log_entry = ARGV.join(' ')

# Regex to capture content from [from:], [to:], and [flags:]
# We use \d to match digits, and [^\]]+ to match any character except a closing bracket
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Match the regex against the log entry
match_data = log_entry.match(regex)

if match_data
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]

  # Output in the exact format required: [SENDER],[RECEIVER],[FLAGS]
  puts "#{sender},#{receiver},#{flags}"
else
  # Debugging help: print what the script actually received if no match is found
  # puts "No match found in input: #{log_entry}"
end
