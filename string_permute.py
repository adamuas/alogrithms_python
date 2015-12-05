def swap(lst, i, j):
    """ returns list after swap"""
    temp = lst[i];
    lst[i] = lst[j];
    lst[j] = temp;

    return lst;


def string_permutations(string,i,permutations,
                        curr_cycle):

    print "i: {0} string: {1} permtuations: {2} curr_cycle: {3}".format(i,
                                                                        string,
                                                                        permutations,
                                                                        curr_cycle);
    if curr_cycle == 0:
        print "Base case reached!"
        return permutations;

    
    if (i == 0):
        #cycle swap
        print "cycle swap"
        i = len(string)-1;
        curr_cycle = curr_cycle -1;
        string = swap(string, i, --0);
        permutations.append(list(string));
        string_permutations(string,i,permutations,curr_cycle);
    else:
        print "left swap"
        string = swap(string,i, i - 1);
        
        permutations.append(list(string));
        #call again
        string_permutations(string,i-1,permutations,curr_cycle);
        
        

a = [1,2,3];
##print a;
##swap(a,1,0);
##print a;
#print a[--0]
string = 'abc';
lst_permutations = [list(string)];
final = string_permutations(list(string),
                          i = len('abc') -1,
                          permutations = lst_permutations, curr_cycle = len('abc') -1);
print "final: {0}".format(lst_permutations);
