from random import randint
import numpy as np


data = []
d = []
N = 100
for i in range(N):
    offset = round(np.random.normal(scale = 1.0),2)
    data.append(2*i - 2 + offset)

def calc_L2(y,dy):
    return (y-dy)**2

step_size0 = 0.01
step_size1 = 0.01
w1 = 0
w0 = 0

for i in range(10000):

    loss_sum = 0
    loss_sum0 = 0
    loss_sum1 = 0

    for p in range(N):
        dy = w1 * p + w0
        loss_sum += calc_L2(data[p],dy)

        dy0 = w1 * p + (w0+0.01)
        loss_sum0 += calc_L2(data[p],dy0)

        dy1 = (w1 + 0.01) * p + w0
        loss_sum1 += calc_L2(data[p],dy1)


    
    avg_loss = loss_sum / (2*N)
    avg_loss0 = loss_sum0 / (2*N)
    avg_loss1 = loss_sum1 / (2*N)

    w0 += (1 if avg_loss > avg_loss0 else -1) * step_size0
    w1 += (1 if avg_loss > avg_loss1 else -1) * step_size1

print(round(w1,2),"* x +", round(w0,2))














