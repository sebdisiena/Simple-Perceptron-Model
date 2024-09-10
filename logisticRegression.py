import numpy as np
import matplotlib.pyplot as plt

# function to plot regression line
def draw(x1, x2):
    ln = plt.plot(x1, x2, '-')
    plt.pause(0.001)
    # remove previous line for animation
    ln[0].remove()

# function for sigmoid equation 
def sigmoid(score):
    return 1 / (1 + np.exp(-score))

# function to calculate the cross entropy for error
def calculate_error(line_parameters, points, y):
    # touple of arrays dimensions, 0  for rows
    m = points.shape[0]
    # calculate the probability that the point is positive i.e. below the line
    p = sigmoid(points * line_parameters)
    # cross entropy function
    cross_entropy = - (1 / m) * (np.log(p).T * y + np.log(1 - p).T * (1 - y))
    return cross_entropy

# gradient descent function used to reduce error taking line parameter data (x1, x2, bias = 0), labelled data and learning rate
def gradient_descent(line_parameters, points, y, learning_rate):
    m = points.shape[0]
    # 500 iterations to reduce error
    for i in range(500):
        p = sigmoid(points * line_parameters)
        # gradient descent equation
        gradient = (points.T * (p - y)) * (learning_rate / m)
        # update linear model 
        line_parameters = line_parameters - gradient
        # extract linear model gradients and bias
        w1 = line_parameters.item(0)
        w2 = line_parameters.item(1)
        b = line_parameters.item(2)
        # update start and end point of line 
        x1 = np.array([points[:, 0].min(), points[:, 0].max()])
        x2 = - b / w2 + x1 * (- w1 / w2)
        # draw the line of the smallest error
        draw(x1, x2)
        print(calculate_error(line_parameters, points, y))

n_pts = 100
# keep the same random numbers
np.random.seed(0)
# bias value of 1 for every point
bias = np.ones(n_pts)
# return random normally distributed values (bell shaped curve) - normal(mean/center value, standard deviation/spread, number of points in distribution)
top_region = np.array([np.random.normal(10, 2, n_pts), np.random.normal(12, 2, n_pts), bias]).T
# bottom region points
bottom_region = np.array([np.random.normal(5, 2, n_pts), np.random.normal(6, 2, n_pts), bias]).T
# stack top_region vertically above bottom_region
all_points = np.vstack((top_region, bottom_region))
# transpose for matrix multiplication against points
line_parameters = np.matrix(np.zeros(3)).T
# find the leftmost and rightmost points on the plot
# x1 = np.array([bottom_region[:, 0].min(), top_region[:, 0].max()])
# # rearrange w1x1 + w2x2 + b = 0 to get vertical position for left and rightmost points
# x2 = - b / w2 + x1 * (- w1 / w2)
# label top points as 0 and bottom points as 1
y = np.array([np.zeros(n_pts), np.ones(n_pts)]).reshape(n_pts * 2, 1)

# subplots to plot more than one point and 4 inches x 4 inches in figsize
_, ax = plt.subplots(figsize=(4, 4))
# plot first and second columns of data i.e. x1, x2
ax.scatter(top_region[:, 0], top_region[:, 1], color = 'r')
ax.scatter(bottom_region[:, 0], bottom_region[:, 1], color = 'b')
# draw(x1, x2)
gradient_descent(line_parameters, all_points, y, 0.06)
plt.show()