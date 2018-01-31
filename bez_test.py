import math
import matplotlib.pyplot as plt
x = [0,1,2,3]
y = [0,1,2,3]
new_x = []
new_y = []

#Generate the bezire curve
def gen_bez(x, y, t):
    for i in range(0,len(x)):
        x = (math.pow((1-t),3)) * x[0] + 3 * (math.pow((1-t),2)) * t * x[1] + 3 * (1-t) \
                * math.pow(t, 2) * x[2] + \
                (math.pow(t,3)) * x[3]
        y = (math.pow((1-t),3)) * y[0] + 3 * (math.pow((1-t),2)) * t * y[1] + 3 * (1-t) * (math.pow(t,2)) * y[2] + (math.pow(t,3)) * y[3]

for i in range(0,20):
    gen_bez(x,y,i)

plt.plot(new_x, new_y)
