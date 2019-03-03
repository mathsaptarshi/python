m= [[1,2],[3,4],[5,6]]
for row in m:
	print(row)
res = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in res:
	print(row)
	
'''Using zip: Zip returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. In this example we unzip our array using * and then zip it to get the transpose.
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
    print(row)
print("\n")
t_matrix = zip(*matrix)
for row in t_matrix:
    print row'''

'''	
# You need to install numpy in order to import it
# Numpy transpose returns similar result when 
# applied on 1D matrix
import numpy 
matrix=[[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))'''