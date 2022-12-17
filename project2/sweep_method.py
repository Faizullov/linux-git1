import numpy as np
# Complex numbers don't need to be initialized

alpha_z_1 = 0
alpha_z_2 = 3
z_c = 5
L_b = 10
L_c = 2
L_z = 10
Lambda = 1
Xi_1 = 1
Xi_2 = 1.5
D_z = -1/(4 * np.pi * Lambda)
beta = -np.pi * Lambda
print("enter tau_r")
t = float(input())
print("enter L_t")
L_t = float(input())
print("enter N_t")
N_t = int(input())
print("enter N_z")
N_z = int(input())
tau = L_t / N_t
w_t = [i * tau for i in range(N_t)]
h = (L_b + L_z) / N_z
w_z = [i * h for i in range(N_z)]
