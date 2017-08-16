# CodeFights - Useful Numbers
___
> A number **i** is considered to be useful to number **k** if `(i + k) = (i | k)` , where `|` is the bitwise OR operation. 
> Given a positive integer *k*, calculate the **number of integers** useful to k within the range **0...k**.
>
> ### Example:
> 
> For k = 10, the output should be
> usefulNumbers(k) = 4.
> 
> The useful numbers are 0, 1, 4, and 5. Here's why:
> 
> (0 + 10) = (0 | 10) = (02 | 10102) = 10102 = 10
> (1 + 10) = (1 | 10) = (12 | 10102) = 10112 = 11
> (4 + 10) = (4 | 10) = (1002 | 10102) = 11102 = 14
> (5 + 10) = (5 | 10) = (1012 | 10102) = 11112 = 15
> 
> Thus, the answer is 4.
> ___
> ### Input/Output:
> > 
> > [input] integer k
> > 
> > Guaranteed constraints
> > 1 ≤ k < 231.
> > 
> > [output] integer
> > The number of integers useful to k within the range 0...k.
