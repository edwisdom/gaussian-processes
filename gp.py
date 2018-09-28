import itertools

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, kv
from sklearn.metrics.pairwise import euclidean_distances


######################## MEAN AND COVARIANCE FUNCTIONS ###################


def zero_mean(x):
	"""Mean function that returns an array of 0's, one per test point in x"""
	return np.zeros((x.shape)[0])


def rbf_kernel(x_1, x_2, l):
	"""
	Returns an A x B sized kernel matrix using the RBF kernel

	Arguments:
	- x_1: A vector (Numpy array) with size A
	- x_2: A vector (Numpy array) with size B
	- l: A hyperparameter (float) that controls the length-scale of the kernel
	"""

	assert l > 0, "The hyperparameter l must be > 0"
	dist = euclidean_distances(x_1.reshape(-1,1), x_2.reshape(-1,1))
	return np.exp(dist**2 / -(2*l**2))


def matern_kernel(x_1, x_2, l, v):
	"""
	Returns an A x B sized kernel matrix using the Matern kernel

	Arguments:
	- x_1: A vector (Numpy array) with size A
	- x_2: A vector (Numpy array) with size B
	- l: A hyperparameter (float) that controls the length-scale of the kernel
	- v: Another hyperparameter (float) controlling the kernel's smoothness
	"""

	assert l > 0 and v > 0, "The hyperparameters l and v must be > 0"
	dist = euclidean_distances(x_1.reshape(-1,1), x_2.reshape(-1,1))
	dist[dist == 0.0] += 1e-10
	z = np.sqrt(2*v) * dist / l
	return (2**(1-v)/gamma(v)) * (z**v) * kv(v, z) 


def kernel_test(l, v):
	"""
	A simple visual test of the RBF and Matern kernels on some synthetic data.
	Takes as arguments two hyperparameters l and v.
	"""
	"Testing RBF and Matern kernels with: "
	x = np.array([1,2,3,4])
	y = np.array([2,4,6])
	print(x)
	print(y)
	print("RBF Kernel with l= " + str(l) + ": ")
	print(rbf_kernel(x,y,l))
	print("Matern Kernel with l= " + str(l) + " and v= " + str(v) + ": ")
	print(matern_kernel(x,y,l, v))


#------------------------------------------------------------------------#
########################   SAMPLING FUNCTIONS   ##########################


def sample_GP_prior(x_test, mean_func, cov_func, kernel_params, 
					seed=42, n_samples=5):
    """ 
    Draw sample from GP prior given mean and covariance functions.

    Arguments:
    - x_test: A vector (Numpy array) of test points
    - mean_func: Vector --> Vector, function that computes a mean
    	value for each test point and returns the result as a 1D Numpy array 
    - cov_func: Vector (size A), Vector (size B) --> Matrix (size AXB),
    	Function that computes covariance (kernel) for each pair of inputs.
    - seed: int for the random number generator, for reproducibility
    - n_samples: An int, the number of samples to draw from the prior

    Returns:
    - sample: 2D Numpy array, n_samples x size(x_test)
        Contains sampled function values at each point of x_test
    """
    m = mean_func(x_test)
    k = cov_func(x_test, x_test, *kernel_params)
    prng = np.random.RandomState(int(seed))
    sample = prng.multivariate_normal(m, k, n_samples)
    return sample


def sample_GP_posterior(x_train, y_train, x_test, mean_func, cov_func,
					    kernel_params, sigma=0.1, seed=42, n_samples=5):
    """ 
    Draw sample from GP posterior given training data, test data, 
    and mean and covariance functions.

    Arguments:
    - x_train: A Numpy array of N training examples 
    - y_train: A Numpy array of N observed values at points from x_train
    - sigma: A float specifying the standard deviation of the likelihood.
   
    Other args are the same as earlier function: sample_GP_prior

    Returns:
    - sample: 2D Numpy array of n_samples x size(x_test) with sampled values
    - f_star: 1D Numpy array with size(x_test), mean value at each test point
    - diag(V_f): 1D Numpy array with size(x_test), variance at each test point
    """
    K = cov_func(x_train, x_train, *kernel_params)
    L = np.linalg.cholesky(K + sigma**2 * np.identity((x_train.shape)[0]))
    K_star = cov_func(x_train, x_test, *kernel_params)
    alpha = np.linalg.solve(np.transpose(L), np.linalg.solve(L, y_train))
    f_star = np.dot(np.transpose(K_star), alpha)
    v = np.linalg.solve(L, K_star)
    K_star_star = cov_func(x_test, x_test, *kernel_params)
    V_f = K_star_star - np.dot(np.transpose(v), v)
    prng = np.random.RandomState(int(seed))
    sample = prng.multivariate_normal(f_star, V_f, n_samples)
    return sample, f_star, np.diag(V_f)


#------------------------------------------------------------------------#
########################     PLOTTING FUNCTIONS     ######################


def make_plot(x, y):
	"""
	Creates a Matplotlib plot of 5 lines given some x and y data.

	Arguments:
	- x: A 1D Numpy array
	- y: A 2D Numpy array of size n_samples x size(x), sampled values
	"""

	plt.figure()
	styles = ['b-', 'g-', 'r-', 'm-', 'y-']
	for i in range(5):
		plt.plot(x, y[i], styles[i])


def combine_params(param_list):
	"""
	Takes a list of lists of parameter values and returns all possible
	combinations of those parameters as another list of lists.
	"""

	if sum(isinstance(l, list) for l in param_list) > 1:
		return list(map(list, list(itertools.product(*param_list))))
	else:
		return [[p] for p in param_list]


def plot_prior(x_test, kernel, params):
	"""
	Plots a GP prior on x_test with a specific kernel and parameters
	and saves a PNG file of it.
	
	Arguments:
	- x_test: A 1D Numpy array of test points
	- kernel: A kernel function to compute covariance (returns 2D array)
	- params: A list (of lists) of kernel parameter values to try
	"""

	params = combine_params(params)
	for p in params:
		y = sample_GP_prior(x_test, zero_mean, kernel, p)
		make_plot(x_test, y)
		plt.savefig('gp_plot_' + str(plt.gcf().number) + str('.png'),
					bbox_inches='tight')
   

def plot_posterior(x_train, y_train, x_test, kernel, params):
	"""
	Plots a GP posterior given some training data, testing data,
	a kernel, and some parameters, and saves a PNG file of it.
	
	Arguments:
	- x_train: A 1D array of N test points
	- y_train: A 1D array of N observations
	
	Other arguments are same as function above: plot_prior
	""" 

	params = combine_params(params)
	for p in params:
		y, mu, sigma_sq = sample_GP_posterior(x_train, y_train, x_test, 
											  zero_mean, kernel, p)
		make_plot(x_test, y)
		plt.plot(x_train, y_train, 'ko')
		plt.gca().fill_between(x_test.flat, mu-2*sigma_sq, 
							   mu+2*sigma_sq, color="#dddddd")
		plt.savefig('gp_plot_' + str(plt.gcf().number) + str('.png'),
					bbox_inches='tight')


#------------------------------------------------------------------------#


# Initialize training data, testing data, and hyperparameter values
x_train = np.asarray([-2.,    -1.8,   -1.,  1.,  1.8,     2.])
y_train = np.asarray([-3.,  0.2224,    3.,  3.,  0.2224, -3.])
x_test = np.linspace(-20,20,250)
l_values = [0.25, 1, 4]
v_values = [0.5, 2, 8]


# Plot prior and posterior for both kernel types
plot_prior(x_test, rbf_kernel, l_values)
plot_prior(x_test, matern_kernel, [l_values, v_values])
plot_posterior(x_train, y_train, x_test, rbf_kernel, l_values)
plot_posterior(x_train, y_train, x_test, matern_kernel, [l_values, v_values])

