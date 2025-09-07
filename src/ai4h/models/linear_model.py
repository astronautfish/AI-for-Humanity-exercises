from pathlib import Path
import numpy as np
from numpy.typing import NDArray

def test():
    project_root = Path(__file__).resolve().parents[3]
    relative_path = Path(__file__).resolve().relative_to(project_root)
    print(f"Hello from `{relative_path}` <3")

def sigmoid_function(y):
    return np.exp(y) / (1 + np.exp(y))



def generat_logreg_data(
        n: int,
        beta: NDArray[np.float64],
        seed: int = 0,
) -> tuple[NDArray[np.float64], NDArray[np.int64]]:
    
    #1 Compute the number of covariates from the length of the beta vector
    beta_len = beta.shape[0]
    
    return beta_len
    #2 Craete a random number generator called 'rng'
    #3 Simulate a matrix X with shape (N, p+1).
        #3.1 First column is all 1.
        #3.2 The others are drawn from a uniform dist ~Unif(-1,1)
    #4 Draw y by using rng.binomial with n=1 and prob param = p (not num of covariates)
    #