def is_penta(x)
    ret_val = 0.5/3 + Math.sqrt((0.5/3)**2  + x/1.5)
    return ((ret_val - ret_val.round).abs < 0.00000001 ? true : false)
end

pentagons = []
n = 1
running = true
ans = []
while running
    c = ((n*0.5)*(3*n-1)).to_i
    for other in pentagons
        diff = c - other 
        if is_penta(diff)
            sum = c + other
            if is_penta(sum)
                ans = [c,other]
                running = false
                break
            end
        end
    end
    pentagons.append(c)
    n += 1 
end

puts (ans[0]-ans[1]).abs