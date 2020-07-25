result = 0 
ten_zeroes = 10000000000
for i in 1..1000
    current = 1
    for j in 1..i do
        current *= i
        current %= ten_zeroes
    end
    result += current
    result %= ten_zeroes
end

puts result
#or
puts ((1..1000).inject(0){|sum,x| sum + x**x})%ten_zeroes