require 'Prime'
require 'set'
require 'time'


t0 = Time.now


i = 2
not_four = true 

#this works but had faster verision before, aja jag lär mig
#dab dab dab 

while true
    i += 1
    if not_four
        p1 = Prime.prime_division(i).to_h.keys.uniq
        p2 = Prime.prime_division(i+1).to_h.keys.uniq
        p3 = Prime.prime_division(i+2).to_h.keys.uniq
        p4 = Prime.prime_division(i+3).to_h.keys.uniq
        not_four = false
    else
        p1 = p2
        p2 = p3
        p3 = p4
        p4 = Prime.prime_division(i+3).to_h.keys.uniq
    end 
    
    l = [p1,p2,p3,p4]
    ctrl = false
    for j in 0..4
        c = l[3-j]
        if c.length() != 4
            i += 3-j
            not_four = true
            ctrl = true
            break
        end
    end 

    next if ctrl
    common = p1 & p2 & p3 & p4

    if common.empty?()
        break
    end
end


puts i
puts Time.now - t0