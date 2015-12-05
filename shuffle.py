import numpy as np;

def shuffle(A):
    """
    Uniformly shuffles the element of a given array.

    Shuffles the elements in a given array by a method presented by Segdewick
    on the Algorithms courseware on cousera.
    Available at: (https://class.coursera.org/algs4partI-009/lecture)

    args:
    A - array of elements.

    returns:
    A - Shuffled elements.
    
    
    """

    #get len
    N = len(A)-1;
    
    #shuffle-upperbound 
    hi = N;
    
    #shuffle
    for i in range(0, len(A)-2):
        #shuffle lower bound
        lo = i + 1;

        # Swap operation:
        #generates index (j) with upper and lower bounds
        j = np.random.randint(lo, hi +1);
        #swap element at i with j.
        temp = A[i];
        A[i] = A[j];
        A[j] = temp;


    
    return A;

        

A = range(1,50);
print shuffle(A);
        
        
    
        

    
