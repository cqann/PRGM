require 'set'
name_file = File.open("names.txt")
names = name_file.readlines.map(&:chomp)
#names = names.map {|x| x.split(" ")[0] if x.split("").length == 3}
new_names = []
for name in names
    cur = (name.split(" ")).to_a
    if cur.length == 3
        new_names << cur[1]
    end
end

set_names = new_names.to_set

a = ('a'..'z').to_a << 'å' 
a << 'ä'
a << 'ö'

for i in a
    for j in a 
        for k in a
            cur = "o" + i + "r" + j + k
            if set_names.include?(cur)
                puts cur
            end
        end
    end
end