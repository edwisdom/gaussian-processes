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

### Explanation

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

### Explanation

Whereas the l again controls the length-scale for the Matern kernel, the hyperparameter $v$ seems to control the smoothness. Visually, we can see in Figure 2 that increasing l while holding v constant increases the stability of the function. In other words, two samples that are close in the input space tend to be closer in the output space with higher values of l. 

Conversely, the visual impact of increasing v while holding l constant is that it reduces the jaggedness of the function, thereby eliminating some local extrema. Practically, this means that increasing l can be used to create a model with less variance (but perhaps more bias), while decreasing $v$ gives the model some more freedom to chase outliers. 


## Sampling from a Gaussian Process Posterior


### RBF Kernel

<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_13.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_14.png">
<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_15.png">

Figure 3: 5 samples from a GP posterior for each of 3 hyperparameter settings of an RBF kernel (l = {0.25, 1, 4})

### Explanation

There is a lot less variance in the model with higher values of l at x=0, which we can see in the gray-shaded 95% confidence intervals in Figure 3. Moreover, with higher values of l, the model extrapolates from the surrounding data points and predicts a similar value; on the other hand, with lower values of l, the model does not extrapolate as much and therefore predicts values much closer to the mean. Interestingly, with a low enough value of l as in Figure 3a, the model's uncertainty about its predictions at x=0 is comparable to its uncertainty about regions that are much more distant from its training data (say, at x=15). 
