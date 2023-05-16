# Import library
import numpy as np
import math

# Array creation
a = np.array([1, 2, 3])
print(a)
# Print the dimension of a list
print(a.ndim)

b = np.array([[1, 2, 3], [4, 5, 6]])
b

a.dtype

c = np.array([2.2, 5, 1.1])
c.dtype.name

c

# create zeros and ones
d = np.zeros((2, 3))
print(d)

e = np.zeros((2, 3))
print(e)

# Create random number with dimension in np
np.random.rand(2, 3)

# Using np arange to create an array 1D from 10 to 50 with even number
f = np.arange(10, 50, 2)
f

# Using np linspace to create an array 1D with float, for example
f = np.linspace(0, 2, 15)
f

# Array Operation

# Only notation, for reinformance we will come back later

# reshape example
b = np.arange(1, 16, 1).reshape(3, 5)
b

# Image manipulation (yeah each pixel is just a color code :D)
from PIL import Image
from IPython.display import display

# let's import and view the image
im = Image.open("./data/chris.jpg")
# display(im)
im.show()

# Convert the image to array
array_im = np.array(im)
# print(array.shape)
# array.max()
array_im

# The maximum is 255 which is good for this exercise (8 bit, 2^8 values possible)
# Let's invert the image
full = np.full(array.shape, 255)
full

# Subtract elementwise
invert_array = full - array_im
invert_array

invert_array = invert_array.astype(np.uint8)
invert_array

# display(Image.fromarray(invert_array))
Image.fromarray(invert_array).show()

# some reshape
reshape_invert_array = np.reshape(invert_array, (250, 1476))

# display(Image.fromarray(invert_array))
Image.fromarray(reshape_invert_array).show()

# Mechanic of Numpy
a = np.array([[1, 2], [3, 4], [5, 6]])

print(a > 5)
print(a[a > 5])

a[1, 1]

# Take each element and pack to row/col
np.array([a[0, 0], a[1, 1], a[2, 1]])

# Zip list by using matrix indexing
print(a[[0, 1, 2], [0, 1, 1]])

# Slicing
a = np.array([0, 1, 2, 3, 4, 5])
print(a[:3])

print(a[2:4])

# Multi dimensional slicing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[:2])

sub_array = a[:2, 1:3]
print("sub array index [0,0] value before change:", sub_array[0, 0])
sub_array[0, 0] = 50
print("sub array index [0,0] value after change:", sub_array[0, 0])

# Trying numpy with Datasets
# Wine quality
wines = np.genfromtxt("./data/winequality-red.csv", delimiter=";", skip_header=1)
cols = np.genfromtxt("./data/winequality-red.csv", dtype="str", delimiter=";")[0]
# wines
# cols

# Print the first row only
print(wines[:, 0])
# or to preserve the row_col relationship
print(wines[:, 0:1])

#
wines[0, 0:3]

# Non-consecutive columns
wines[:, [0, 2, 4]]

# some general statistic
# for last columns
wines[:, -1].mean()

wines[:, -1]

# Graduate School Admission
cols = np.genfromtxt("./data/graduate_admission.csv", dtype="str", delimiter=",")[0]
# cols
# In here the name of the columns in numpy matrix can only be used by tuple
graduate_admission = np.genfromtxt(
    "./data/graduate_admission.csv",
    dtype=None,
    delimiter=",",
    skip_header=1,
    names=(tuple(cols)),
)
graduate_admission

# Check shape
graduate_admission.shape

# only CGPA col
graduate_admission["CGPA"][0:5]

# the GPA is from 1 to 10, let's change it to 1 to 4
graduate_gpa = graduate_admission["CGPA"] / 10 * 4
graduate_gpa[0:5]

# Check numbers of students has research experience
len(graduate_admission[graduate_admission["Research"] == 1])

# Check if the students with high chance of admission (>0.8) on average has
# higher GRE score than those with lower change
gre_mean_high = graduate_admission[graduate_admission["Chance_of_Admit"] >= 0.8][
    "GRE_Score"
].mean()
print("GRE of high change", gre_mean_high)
gre_mean_low = graduate_admission[graduate_admission["Chance_of_Admit"] < 0.8][
    "GRE_Score"
].mean()
print("GRE of low change", gre_mean_low)
