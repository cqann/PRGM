require 'Prime'

i = 1

while true
    i += 2
    p i
    p i
    next if Prime.prime?(i)
    
    j = 0
    ctrl = true
    while ctrl
        j += 1 
        break if 2*j*j >= i

        Prime.each(i-2*j*j) do |pr|
            ctrl = false if i == 2*j*j + pr
        end

    end

    break if ctrl 

end

puts "---------------------------------------------"
puts "Answer: #{i}" 