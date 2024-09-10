# Simple Perceptron Model

## Objective
- Project to learn about the simple single-layer perceptron neural network model and supervised learning
- Labelled dataset is produced through 2 seperate normally distributed data points
- **Aim:** Seperate the data into 2 discrete classes through linear regression

## Method
- Model utilises the **sigmoid activation function** to determine the probability for a data point to be placed within the positive region
- The **cross entropy error** is calculated to determine the error of the regression line
- **Gradient Descent** is implemented to iterate through the line parameters (i.e. weight 1, 2, and bias) to produce a linear model with minimal error

## Mathematical Equations
- Single-layer perceptron model: *y = w1(x1) + w2(x2) + bias*
- Sigmoid activation function: *p = (1/(1+e^-y))* 
- Cross entropy error: *E = -sum yln(p) + (1-y)(ln(1-p))* (1 / m) * (ln(p) * y + np.log(1 - p).T * (1 - y))
- *Gradient descent:*

## Demo Results
Insert gif:
