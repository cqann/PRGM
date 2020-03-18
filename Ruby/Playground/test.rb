require 'ruby2d'

set title: "yeeet", width: 600, height: 600

def f1(a,b)
    return Math.sin(a+b * Math.cos(a*b))
end

def f2(a,b)
    return Math.sin(Math.cos(a*b)-Math.sin(b*b))
end

res = 0.05

for y in 0..600
    puts y
    ny = (y-300) * -res 
    for x in 0..600
        nx = (x-300) * res 

        if ( f1(nx,ny) - f2(nx,ny) ).abs < 0.1
            Square.new(
                x: x, y: y,
                size: 2,
                color: 'aqua'
              )
        end
        

    end 
end




show