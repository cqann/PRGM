from time import *


def f(x):
    return 3*x**2-.4

def g(x):
    return -f(x)

def plot(res,xmin,xmax):
    framerate = 10
    #setup plotting area
    plt.window(xmin,xmax,xmin/1.5,xmax/1.5)
    plt.cls()
    gscale=5
    plt.pen("thin","solid")
    plt.color(0,0,0)
    plt.labels("abscisse"," ordonnee",6,1)
    plt.pen("medium","solid")
    
    # plot f(x) and g(x)
    dX=(plt.xmax -plt.xmin)/res
    x=plt.xmin
    x0=x

    vx = 1
    vy = 1

    points = [[0,0],[0.1,0],[0.2,0]]
    while True:
        for i in range(len(points)):
            if i == len(points) - 1: break
            plt.color(255,0,0)
            plt.line(x0,f(x0),x,f(x),"")
            x0=x
            x+=dX

        sleep(1/framerate)

    plt.show_plot()

#plot(resolution,xmin,xmax)

plot(30,-1,1)

# Create a graph with parameters(resolution,xmin,xmax)

# After clearing the first graph, press the [var] key. The plot() function allows you to change the display settings (resolution,xmin,xmax).