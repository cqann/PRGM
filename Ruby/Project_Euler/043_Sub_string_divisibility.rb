result = 0
divs = [2,3,5,7,11,13,17]
digits = [0,1,2,3,4,5,6,7,8,9]

for i in digits.permutation(10)
    add = true
    for j in 1..7
        cur = (i[j,3].join("")).to_i
        if cur % divs[j-1] != 0
            add = false
            break
        end
    end
    add ? result += i.join("").to_i : result += 0   
end

puts result
