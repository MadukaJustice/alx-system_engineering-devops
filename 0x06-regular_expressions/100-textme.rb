#!/usr/bin/env ruby
# Parse fields and return [SENDER], [RECIEVER], [FLAGS]

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
