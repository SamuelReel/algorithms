# algorithms
Algorithms that I have coded for some of my classes


/*************************/
/   Matrix Chain Order    /
/*************************/
Matrix chain order takes an array of p values that represent arrays such that:

A1 = p0 x p1
A2 = p1 x p2
...
An = p(n-1) x pn

And prints out two tables. 
The first table represents the number of scalar multiplications
required to complete the multiplication of the arrays A[i,j], where i is the y-axis and
j is the x-axis.
The second table is used to calculate the correct parenthesisation of the matrix chain.



/*************************/
/          LMIS           /
/*************************/
LMIS takes an array of integers and prints the length of the longest monotonically increasing
subsequence from that array.
