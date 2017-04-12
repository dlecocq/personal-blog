#!/sw/bin/ruby

usage = "lru.rb \"trace\" stack_size"

string = ARGV[0]
if string.class != String
  puts usage
  exit 1
end

m = ARGV[1]
if m == nil
  puts usage
  exit 2
elsif (m = m.to_i) == 0
  puts usage
  exit 3
end

page_fault_count = 0

stack = Array.new(0)
for i in 0...string.size
  if stack.include?(string[i,1])
    # resort the stack
    stack.unshift(stack.delete_at(stack.index(string[i,1])))
    puts "#{string[i,1]}   #{stack.join("\t")}"
  else
    page_fault_count += 1
    if stack.size() == m
      stack.pop
    end
    stack.unshift(string[i,1])
    puts "#{string[i,1]} * #{stack.join("\t")}"
  end
end

puts "Page faults: #{page_fault_count} / #{string.size}"