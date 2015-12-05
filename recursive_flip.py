"""
Implementations of
- stacked reverse
- recursive reverse
- recurssive flip
- Delicate flip
- Anagram
"""

def stacked_reverse(S):
    """
    Reverses the elements of a string

    This approach uses a stack to reverse the elements of a string
    and is a helper function fro the recursive flip algorithm described
    by Jon in Programming pearls. BigO Complexity O(2n) - copy operations.

    args:
    S (String) - String to be reversed.

    returns:
    reversed form of the string S.
    """
    
    #populate stack
    stack = [si for si in S];

    #depopulate stack
    reverse = [stack.pop() for _ in xrange(len(stack))];
    
    return  ''.join(reverse);


def generator_reverse(S):
    """
    Reverses the elements of a string

    This approach uses a generator to reverse the elemtns of a string, and
    is a helper function for the recursive flip algorithm described by Jon
    in Programming Pearls. BigOComplexity O(n) - copy operators.

    args:
    S(String)- String to be reversed.

    returns:
    reversed form of the string
    """
    
    reverse_gen = (S[i] for i in xrange(len(S)-1,-1,-1));
    
    return  ''.join(reverse_gen);

def recursive_reverse(S, i, j):
    """
    Reverses the elements of a string

    Tihs approach uses a recursive approach to reverse the elements of the string, and
    is a helper function for the recursive flip algorithm described by Jon in Programming
    Pearls. BigOComplexity O(n) stack space.

    args:
    S(String) - Stringto be the reversed

    returns:
    reversed form of the string
    """

    str_len = len(S[i:j]);
    
    #Base case
    if str_len == []:
        return;
    elif i < j:
        #swap ends
        temp = S[i];
        S[i] = S[j];
        S[j] = temp;

        #recurse
        recursive_reverse(S , i + 1 , j - 1 );
        
    return ''.join(S);


def move_to_end_delicate(S,i):
    """
    Moves first i elements of S to the back of the array i

    This approach uses the approach expressed in Programming pearls. BigOComplexity of O(n) swap operations.

    args:
    S (String) - String
    i (int) - index of the cut-off point from which the elements should be moved.

    returns:
    returns the string with the elements moved
    """

    for j in xrange(0,i):

        #copy to temporary position.
        temp = S[i];

        #move elements
        
            
def move_to_end_reverse(S, i):
    """
    Moves the first i elements of S to the back of the array i.

    This approach uses the approach expressed in Programming Pearls. BigOComplexity of O(n) - stack space.

    args:
    S (String) - String
    i (int) - index of the cut-off from which the elements should be moved.
    """


    S = recursive_reverse(list(S), 0, i);
    
    S = recursive_reverse(list(S), i+1, len(S)-1);
    S = recursive_reverse(list(S), 0, len(S)-1);

    return S;


        
#TESTS        
        
s = "ABCDEF";
s_reversed = move_to_end_reverse(list(s), 2);
print s_reversed;
assert s_reversed == "DEFABC";

                    
a0 = recursive_reverse(list(s), i = 0, j = len(s)-1);
print a0;

a =  stacked_reverse("ABC");
a2 = generator_reverse("ABC");

print a2;
print a;

assert a == "CBA"

    

