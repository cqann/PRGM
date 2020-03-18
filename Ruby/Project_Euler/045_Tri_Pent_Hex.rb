require 'set'

tri = Set.new()
pen = Set.new()
hex = Set.new()

c = 1

while true

    tr = c * (c + 1) / 2
    pe = c * (3 * c - 1) / 2 
    he = c * (2 * c - 1)

    if pen.include?(tr) && hex.include?(tr) && tr != 40755
        p tr
        p c
        break
    end

    tri.add(tr)
    pen.add(pe)
    hex.add(he)
    
    c += 1
end







