# (a) Matrix Representation of the DFT:
import numpy as np
import matplotlib.pyplot as plt

def dft_matrix(N):
    # Create a 1xN matrix with entries ranging from 0 to N-1
    n = np.arange(N)
    
    # Create a Nx1 matrix with entries ranging from 0 to N-1
    k = n.reshape((N, 1))
    
    # Calculate the DFT matrix
    W = np.exp(-2j * np.pi * k * n / N)
    
    return W

# Create the DFT matrix for N=4
N = 4
W = dft_matrix(N)
    
# Define a simple sequence
x = np.array([1, 2, 3, 4])

# Compute the DFT of the sequence using the DFT matrix
X = np.dot(W, x)

print("DFT of the sequence using the DFT matrix: ", X)

# Compute the DFT of the sequence using numpy's fft function
X_np = np.fft.fft(x)

print("DFT of the sequence using numpy's fft function: ", X_np)

# (b) Properties of the DFT:

# Define two sequences
x1 = np.array([1, 2, 3, 4])
x2 = np.array([5, 6, 7, 8])

# Compute the DFT of the sum of the sequences
X1_plus_X2 = np.fft.fft(x1 + x2)

# Compute the DFTs of the individual sequences
X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)

print("DFT of the sum of the sequences: ", X1_plus_X2)
print("Sum of the DFTs of the sequences: ", X1 + X2)


# Shift sequence x1 by 1
x1_shifted = np.roll(x1, 1)

# Compute the DFT of the shifted sequence
X1_shifted = np.fft.fft(x1_shifted)

# Compute e^(-j2pi/N) times the DFT of x1
X1_times_exp = np.exp(-1j * 2 * np.pi / N) * X1

print("DFT of the shifted sequence: ", X1_shifted)
print("e^(-j2pi/N) times the DFT of x1: ", X1_times_exp)







