import numpy as np

# Numpy is for creating 1-2-3 dimentional arrays.It's faster than lists.
# It allocates lesser bytes than lists.Also there's no type checking
# Furthermore,numpy arrays are sorted contiguous in the memory
# SIMD Vector Processing and Effective Cache Utilization are other benefits.

# Create 1 dim array
a = np.array([1,2,3])
print(a)

# Create 2 dim array
b = np.array([[1.2,4.5,5.6],[5.42,5.67,7.89]])
print(b)

# Get Shape
print(a.ndim) #1
print(b.ndim) #2

# Get Type
print(a.dtype) #int32
print(b.dtype) #float32

# specifying array's dtype
a = np.array([1,2,3,4,5,6],dtype="int16")
print(a.dtype) #int16

# Get Size (length in bytes)
print(a.itemsize)
print(b.itemsize)

# Get size
print(a.size * a.itemsize)
print(b.size * b.itemsize)
# Get Size also
print(a.nbytes)
print(b.nbytes)

######################################################
#ACCESSING SPECIFIC ELEMENTS AND COLUMNS

a = np.array([[1,2,3,4,5,6,7],[11,22,33,44,55,66,77]]) #2 x 7 array
print(a)

#Get a specific element [r,c]

print(a[0,4]) #5
print(a[1,6]) #77

# backwards with "-"
print(a[0,-4]) #4
print(a[1,-6]) #22

# GET A SPECIFIC ROW
print(a[1:])

# GET A SPECIFIC ROW
print(a[:,4])   #returns column as array

# Pacing through the array[START_INDEX : END_INDEX : STEP_SIZE]
print(a[0,0:6:2]) #from the first row,print the columns between 0 and 6 by skipping 2 elements.
print(a[0,0:-3:2])  

#Changing the values of an element
a[1,5] = 20
print(a[1,5])

a[:,2] = [5,10]
print(a)

print("------------------------------------------------------")

# 3-D EXAMPLE 
b = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(b)

# Get specific element in 3D
print(b[0,0,2]) #3
print(b[1,:,2]) # [9,12]

#Change specific element in 3D
b[1,:,2] = [100,200]
print(b[1,:,2])


print("------------------------------------------------------")
# INITIALIZING DIFFERENT TYPE OF ARRAYS - MATRIXES

#creates zeros vector with length of 2 
a = np.zeros(2) 

#creates zeros matrix with the shape of 3x4 
a = np.zeros((3,4),dtype="int16")
print(a)

#creates zeros matrix with the shape of 2x3x4
a = np.zeros(((2,3,4)))
print(a)

#creates zeros vector with length of 2 
a = np.ones(2,dtype="int32") 

#creates zeros matrix with the shape of 3x4 
a = np.ones((3,4))     
print(a)

#creates zeros matrix with the shape of 2x3x4
a = np.ones(((2,3,4)))
print(a)

#Matrix by any other numbers
a = np.full((2,3), 99)
print(a)

#copying an existed matrix's shape
c = np.ones(((4,5,6)))
d = np.full_like(c, 10)
print(d)
print(d.shape)

# Random decimal numbers between 0-1
a = np.random.rand(4,3)
print(a)

# Random decimals with given shape
a = np.random.random_sample(b.shape)
print(a)


# Random int number   
a = np.random.randint(7)
print(a)

# Random array given shape   
a = np.random.randint(7,size=(2,3))
print(a)

print("--------------------------------------")

# Random array in given limits and given shape   
a = np.random.randint(3,7,size=(2,3))
print(a)

# Identity matrix  (axa)
a = np.identity(5)   
print(a)

#repeating vector
arr = np.array([1,2,3])
r1 = np.repeat(arr, 3)
print(r1)

#repeating 2 dim array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3,axis=0)
print(r1)

#sample
sample = np.ones(shape=(5,5))
sample2 = np.zeros((3,3))
sample3 = np.array([9])

sample[1:4,1:4] = sample2
sample[2,2] = sample3
print(sample)

#Copying warning
a = np.array([1,2,3])
b = a
b[0] = 100
print(a)  # a[0] is also changed because when we set b equal a,b will point out a's allocated memory

# in order to fix this:
d = np.array([1,2,3])
c = d.copy()
c[0] = 100
print(d)

print("-----------------------")

#Mathematics

a = np.array([1,2,3,4,5,6])

# math operators will be applied every element in array
print(a + 2)
print(a * 2)
print(a / 2)
print(a**2)

#take the sin-cos
b = np.cos(a)
print(b)
c = np.sin(a)
print(c)


#LINEAR ALGEBRA OPERATIONS

a = np.ones((2,3))
print(a)
b = np.full((3,2), 2)
print(b)

#MATRIX MULTIPLICATION
c = np.matmul(a,b)
print(c)

#Find the determinant
c = np.identity(3)
d =np.linalg.det(c)
print(d)

print("------------------------")

#STATISTICS

stats = np.array([[1,2,3],[1,2,3]])
a=np.min(stats,axis=1) #axis=1: columns axis=0: rows
x=np.min(stats,axis=0)
b=np.max(stats)
c = np.min(stats)

print(a) #[1,1]
print(b) # [1]
print(c) # [3]
print(x) #[1,2,3]

#Sum
a=np.sum(stats,axis=0)
print(a)  #add up all the colummns each other to create one row (like a vector),since the axis=0 

print("--------------------------")

#REORGANIZING ARRAYS

before = np.array([[1,2,3,4,],[5,6,7,8]])
print(before.shape) #(2,4)

after = before.reshape((8,1))
print(after)
after = before.reshape((4,2))
print(after)

# VERTICALLY STACKING VECTORS

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

c = np.vstack([v1,v2,v2,v1]) #vertically stacking the arrays.always places next array under the one before
print(c)

# HORIZONTALLY STACKING VECTORS

v1 = np.array([[1,2,3,4],[5,6,7,8]])
v2 = np.array([[5,6,7],[1,2,3]])

c = np.hstack([v1,v2,v2,v1]) #horizontally stacking the arrays.always places next array next to the one before
print(c)

# MISCELLANEOUS

#Load data from file
filedata = np.genfromtxt(".venv\data.txt",delimiter=",")
#print(filedata)
print(filedata.astype("int32"))

print("-----------------------------")

# Bool Masking and And Advanced Indexing

print(filedata >2) #masks with true-false

c = filedata[filedata>2] # it filters and returns an array with given filter
print(c) 

d = np.any(filedata > 2,axis=0)
print(d) # returns true-false vector

d = np.all(filedata > 2,axis=1)
print(d) # returns true-false vector
print("-------------------------------------------")
print( ( (filedata > 1) & (filedata <5) ) )  #FILTER-returns true-false array  

