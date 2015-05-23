'''
This is a program for Assignment 7
Sarah Welt
'''

import numpy as np
import sys
import json
import matplotlib.pyplot as plt

#2A
sys.argv

#2B
for elem in positons:
	print (elem)

for elem in positions:
	a.append(1000./elem)

def main(argv):
    assert len(argv) == 3
    positions = json.loads(argv[1])
    num_trial = int(argv[2])
    print(positions)
    print(num_trial)

    position_value = map(lambda x: 1000 / x, positions)

    chance = np.random.binomial(1, 0.51)
    outcome = position_value * 2 if chance == 1 else 0

if __name__ == '__main__':
    main(sys.argv)


#2C
cumu_ret [trial]

for i in range(100):
	k.append(np.random.binomial (1,0, .51))

map(lambda x:x*2000, k)

#2D
for i in range (num_trials):


#3A
x = np.random.randn(100)
y = np.random.rand(100) * 10

plt.hist(daily_ret, 100, range=[-1,1])

plt.show()


#3B and 3-C
x = np.random.randn(100)
y = np.random.rand(100) * 10

plt.hist(x, 100, range=[-1,1])

plt.show()

x = np.random.rand(1000,)
print(x.mean())
print(x.std())


a.mean

x = np.random.rand(1000,)
print(x.mean())
print(x.std())

x= [1,2,3,4,5]
x= np.array(x)

x

y= 5*x


plt.plot(x,y)

plt.show()

#Q4
np.savetxt


