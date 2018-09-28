# Gaussian Processes

## Getting Started

These instructions will allow you to run this project on your local machine.

### Install Requirements

Once you have a virtual environment in Python, you can simply install necessary packages with: `pip install requirements.txt`

### Clone This Repository

```
git clone https://github.com/edwisdom/gaussian-processes
```

### Run Models

Run the script with:

```
python gp.py
```

## Sampling from a Gaussian Process Prior

### RBF Kernel

<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_1.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_2.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_3.png">

Figure 1: 5 samples from a GP prior for each of 3 hyperparameter settings of an RBF kernel (l = {0.25, 1, 4})

#### Explanation

The l hyperparameter of a radial-basis function (RBF) or squared-exponential (SE) kernel controls its "length-scale." Visually and geometrically, we see from Figure 1 that higher values of l lead to sample functions that are smoother. Mathematically, higher values of l bring down the variance of the model but likely increase the bias. Practically, higher values of $l$ give us a simpler model, that is less prone to overfitting (though of course, it might instead underfit the data).

### Matern Kernel


<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_4.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_5.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_6.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_7.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_8.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_9.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_10.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_11.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_12.png">

Figure 2: 5 samples from a GP prior for each of 9 hyperparameter settings of a Matern kernel (l = {0.25, 1, 4}, v = {0.5, 2, 8})

#### Explanation

Whereas the l again controls the length-scale for the Matern kernel, the hyperparameter $v$ seems to control the smoothness. Visually, we can see in Figure 2 that increasing l while holding v constant increases the stability of the function. In other words, two samples that are close in the input space tend to be closer in the output space with higher values of l. 

Conversely, the visual impact of increasing v while holding l constant is that it reduces the jaggedness of the function, thereby eliminating some local extrema. Practically, this means that increasing l can be used to create a model with less variance (but perhaps more bias), while decreasing $v$ gives the model some more freedom to chase outliers. 


## Sampling from a Gaussian Process Posterior


### RBF Kernel

<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_13.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_14.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_15.png">

Figure 3: 5 samples from a GP posterior for each of 3 hyperparameter settings of an RBF kernel (l = {0.25, 1, 4})


#### Explanation

There is a lot less variance in the model with higher values of l at x=0, which we can see in the gray-shaded 95% confidence intervals in Figure 3. Moreover, with higher values of l, the model extrapolates from the surrounding data points and predicts a similar value; on the other hand, with lower values of l, the model does not extrapolate as much and therefore predicts values much closer to the mean. Interestingly, with a low enough value of l as in Figure 3a, the model's uncertainty about its predictions at x=0 is comparable to its uncertainty about regions that are much more distant from its training data (say, at x=15). 


### Matern Kernel

<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_16.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_17.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_18.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_19.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_20.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_21.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_22.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_23.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_24.png">

Figure 4: 5 samples from a GP posterior for each of 9 hyperparameter settings of a Matern kernel (l = {0.25, 1, 4}, v = {0.5, 2, 8})

### Explanation

The average value predicted on a sample at x=18 as seen in Figure 4 is 0, because that's the value of our chosen mean function. At x=100, the predicted values would also be around 0, because if Gaussian processes don't have training data sufficiently close to some test point, they default to predicting the mean. If we wanted to change this prediction, we could either try to give it some training data close to the test point, or we could change our mean function. 

The standard deviation on a sample at x=18 as seen in Figure 4 is roughly 1, since the gray-shaded confidence intervals cover two standard deviations above and below the mean and the total shaded length equals 4. At x=100, the standard deviation would also be around 1, because the value we chose for our prior was 1. If we wanted to change the standard deviation of posterior samples at these distant points, say to 42.0, we could just use a standard deviation of 42.0 for our prior.


## Future Work

In the future, I would like to explore the following:

1. Applying Gaussian process prediction to real-time civil war data in order to uncover new patterns in armed conflict, which has only recently spawned [preliminary work](http://journals.sagepub.com/doi/abs/10.1177/0022002710371669).
2. Using new kernels, including INK-spline kernels, which [have been shown](http://geza.kzoo.edu/~erdi/IJCNN2013/HTMLFiles/PDFs/P154-1444.pdf) to work significantly better in practice than RBF kernels

## Credits

A huge thanks to Prof. Michael Hughes, who supervised this work.