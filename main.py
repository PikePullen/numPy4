import numpy as np

# generate a 2x3 matrix with all zeros
A = np.zeros((2,3))
print(A)

print("***********************")
# generate a 2x3 matrix with all ones
B = np.ones((2,3))
print(B)

print("***********************")
# there is no tens, but can just multiple ones by 10
C = 10 * np.ones((2,3))
print(C)

print("***********************")
# identity matrix, eye is better than using "i" which is awful in programming
D = np.eye(3)
print(D)

print("***********************")
# random number
print(np.random.random())

print("***********************")
# random matrix, this always returns between 0 and 1
E = np.random.random((2,3))
print(E)

print("***********************")
# random matrix, this always returns between -1 and 1
# not a tuple passed in, just has two paramter
F = np.random.randn(2,3)
print(F)

print("***********************")
# massive random matrix with a mean
G = np.random.randn(10000)
print(G.mean())
print(G.var())
print(G.std())

print("***********************")
# massive random matrix with a mean
H = np.random.random(10000)
print(H.mean())
print(H.var())
print(H.std())

print("***********************")
# massive random matrix with a mean
# remeber its col, row
I = np.random.randn(10000, 3)
print(I.mean(axis=0))
print(I.mean(axis=1).shape)

print("***********************")
J = np.random.randint(0, 10, size=(3,3))
print(J)

print("***********************")
K = np.random.choice(10, size=(3,3))
print(K)
