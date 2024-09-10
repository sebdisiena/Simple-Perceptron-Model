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
- Single-layer perceptron model: ![Equation](https://latex.codecogs.com/svg.latex?\color{White}y%20%3D%20w_1%28x_1%29%20%2B%20w_2%28x_2%29%20%2B%20%5Ctext%7Bbias%7D)
- Sigmoid activation function: *p = (1/(1+e^-y))* 
- Cross entropy error: *E = -(1/nrows) * (ln(p)*z + ln(1 - p)*(1 - z)) where z is the actual class and p is the probability of that class*
- *Gradient descent:*

## Demo Results
Insert gif:
