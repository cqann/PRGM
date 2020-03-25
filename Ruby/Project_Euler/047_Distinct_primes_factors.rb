require 'Prime'
require 'set'
require 'time'

def find_pfact(n)
    facts = Set.new()
    nc = n
    Prime.each(n) do |pr|
        break if pr > nc
        while nc % pr == 0
            facts.add(pr)
            nc /= pr
        end
    end

    return facts
end

t0 = Time.now

i = 2
p1 = Set.new([2])
p2 = Set.new([3])
p3 = Set.new([2])
p4 = Set.new([5])

while true
    i += 1
    p1 = p2
    p2 = p3
    p3 = p4
    p4 = find_pfact(i+3)
    if p1.length() != 4 || p2.length() != 4 || p3.length() != 4 || p4.length() != 4
        next
    end
    common = p1 & p2 & p3 & p4
    
    break if common.empty?()
end


puts i
puts Time.now - t0