import numpy as np
import random
import pandas
import matplotlib.pyplot as plt


omega = 50000
Scan = 4
Num_of_simulations = 3
N = 500
I = [[],[],[]]

for sim in range(0, Num_of_simulations):
    Comp_infected = 0
    curr_val = np.ones(omega)
    for i in range(N//10):
        for j in range(1,11):
            curr_val[1000*i + j] = 0

    new_status = curr_val
    ip = 2010
    curr_val[ip] = 1
    new_val = curr_val
    Comp_infected +=1
    I[sim].append(Comp_infected)
    for i in range(0, N):
        for j in range(0, Comp_infected):
            for k in range(Scan):
                ip = random.randrange(omega)
                if not curr_val[ip]:
                    new_val[ip] = 1
                    Comp_infected +=1
        I[sim].append(Comp_infected)
        curr_val = new_val
        if Comp_infected == N:
            break


print("Time ticks for simulation 1: ", len(I[0]))
print("Time ticks for simulation 2: ", len(I[1]))
print("Time ticks for simulation 3: ", len(I[2]))


graph1 = pandas.DataFrame(I).T
graph1.rename(columns = {0:'SIM1', 1:'SIM2', 2:'SIM3'}, inplace = True) 
graph1.plot(style=['-','--','*'])
plt.title("Propogation of Worms through Random Scan")
plt.xlabel("Time")
plt.ylabel("I(t)")
plt.show()





