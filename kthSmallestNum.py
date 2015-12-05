def findkth_min(lst,k):
    """
    finds and returns the kth smallest 
    """
    if k > len(lst):
        raise Exception("Sorry k cant be bigger than the length of the list");
    
    lst.sort();
    
    return lst[k-1];
            
import random;
lst = [2,4,22,7,90 ];
print lst;
kth = findkth_min(lst, 3);
print kth;
