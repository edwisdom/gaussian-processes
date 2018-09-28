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

<figure>
	<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_1.png">
	<font size="2">
    <figcaption> RBF Kernel with l = 0.25
    </figcaption>
    </font>
</figure>
<figure>
	<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_2.png">
	<font size="2">
    <figcaption> RBF Kernel with l = 1
    </figcaption>
    </font>
</figure>
<figure>
	<img align="left" width="275" height="300" src="https://github.com/edwisdom/gaussian-processes/blob/master/gp_plot_3.png">
	<font size="2">
    <figcaption> RBF Kernel with l = 4
    </figcaption>
    </font>
</figure>

Figure 1: 5 samples from a Gaussian process prior for each of 3 hyperparameter settings of an RBF kernel

### Explanation

The l hyperparameter of a radial-basis function (RBF) or squared-exponential (SE) kernel controls its "length-scale." Visually and geometrically, we see from Figure 1 that higher values of l lead to sample functions that are smoother. Mathematically, higher values of l bring down the variance of the model but likely increase the bias. Practically, higher values of $l$ give us a simpler model, that is less prone to overfitting (though of course, it might instead underfit the data).

## Matern Kernel




