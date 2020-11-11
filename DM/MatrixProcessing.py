'''
Design and implement a matrix processing library that would be used in a stream processing pipeline. The library will
consume an integer MxN matrix  at start up time and it need to support 2 operations:

void update(int i, int j, int value) : this method will update matrix[j] with the new “value”
long sum(int i, int j, int x, int y) : this method will return the sum of all element of the submatrix where the top
left of the sub matrix is [i,j] and the bottom right of the sub matrix is [x, y].

Requirement: This library expect sum(int i, int j, int x, int y) operation to be called very frequent
(thousands of time per second) and update(int i, int j, int value) operation to be called very infrequent
(once every hour(s)) so sum() implementation should be as fast as possible.
'''