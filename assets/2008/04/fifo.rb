#!/sw/bin/ruby

usage = "fifo.rb \"trace\" queue_size"

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

queue = Array.new(0)
for i in 0...string.size
  if queue.include?(string[i,1])
    # do nothing - it's in the queue
    puts "#{string[i,1]}   #{queue.join("\t")}"
  else
    page_fault_count += 1
    if queue.size() == m
      queue.shift
    end
    queue << string[i,1]
    puts "#{string[i,1]} * #{queue.join("\t")}"
  end
end

puts "Page faults: #{page_fault_count} / #{string.size}"