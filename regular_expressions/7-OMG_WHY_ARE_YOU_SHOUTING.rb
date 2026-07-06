#!/usr/bin/env ruby

# The input string
input = "i Hope Bobby eaTs Nutella - no one ever said"

# Scan for sequences of 1 or more uppercase letters
# We use [A-Z]+ to find groups like 'H', 'B', 'T', 'N'
matches = input.scan(/[A-Z]+/)

# Join the found matches into one string (H + B + T + N)
result = matches.join

# Output the result and length
puts result
