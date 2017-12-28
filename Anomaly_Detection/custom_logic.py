"""
this will find mean value and standard deviation
    and finds minimum values and maximum values based on those.
any point greater then maximum or lesser then minimum will be an outlier
"""

from matplotlib.pyplot import plot, show
from numpy import mean, std

HEIGHT = [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
          72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
WEIGHT = [115, 117, 120, 123, 126, 129, 132, 135, 139, 142, 146, 150, 154, 159,
          164, 164, 168, 171, 175, 178, 182, 185, 188, 192, 195, 199, 202, 206, 209]

HEIGHT_MEAN = mean(HEIGHT)
HEIGHT_STD = std(HEIGHT)
HEIGHT_UPPER_BOUND = HEIGHT_MEAN + HEIGHT_STD
HEIGHT_LOWER_BOUND = HEIGHT_MEAN - HEIGHT_STD

WEIGHT_MEAN = mean(WEIGHT)
WEIGHT_std = std(WEIGHT)
WEIGHT_UPPER_BOUND = WEIGHT_MEAN + WEIGHT_std
WEIGHT_LOWER_BOUND = WEIGHT_MEAN - WEIGHT_std

for i in range(len(HEIGHT)):
    if((HEIGHT_LOWER_BOUND < HEIGHT[i] < HEIGHT_UPPER_BOUND)or(WEIGHT_LOWER_BOUND < WEIGHT[i] < WEIGHT_UPPER_BOUND)):
        plot(HEIGHT[i], WEIGHT[i], 'bo')
    else:
        plot(HEIGHT[i], WEIGHT[i], 'rx')

show()
