#!/usr/bin/env ruby

# 1. Join all arguments to ensure the full string is captured
log_entry = ARGV.join(' ')

# 2. Use a more flexible regex
# \[from:([^\]]+)\]  : Matches [from: followed by everything except ']'
# \s*                : Allows for any amount of spaces
# \[to:([^\]]+)\]    : Matches [to:
# \s*                : Allows for any amount of spaces
# \[flags:([^\]]+)\] : Matches [flags:
regex = /\[from:([^\]]+)\]\s*\[to:([^\]]+)\]\s*\[flags:([^\]]+)\]/

# 3. Match and output
if (match = log_entry.match(regex))
  puts "#{match[1]},#{match[2]},#{match[3]}"
else
  # Print to STDERR so you know why it's failing
  $stderr.puts "Debug: Regex failed to match input: #{log_entry}"
end
