"""
Binary Search Tree implementation

As described by Sedgewick
"""


class BinarySearchTree:
    """
    A binary search tree (BST) implementation.
    """

    def __init__(self, root = None):
        """
        Initializes a binary search tree
        """

        self.root = root;


    def __repr__(self):
        """
        returns the string representation of the given BST object.
        """

        return "<BST>\n \t-root:{0} \n</BST>".format(self.root);
    
      
    class Node:

        def __init__(self, key, value):
            """
            Initializes a node object with a key and value

            params:
            key - an immutable object that is comparable.
            value - the value associated with the key.
            
            """

            self.key = key;
            self.value = value;
            self.right = None;
            self.left = None;

        def __repr__(self):
            """
            returns a string representation of the current node
            """ 

            return """\n\t<Node({0})>
                        \n\t- key:{0}
                        \n\t- value of {0}:{1}
                        \n\t- left of {0}: {2}
                        \n\t- right of {0}: {3}
                        \n\t</Node({0})>""".format(self.key,
                                              self.value,
                                              self.left,
                                              self.right);

        def __lt__(self, other):
            """
            less than comparison to other node
            """
            #instance comparison
            if isinstance(other, BinarySearchTree.Node):
                return self.key < other.key;
            else:
                raise Exception("""ammm...you are trying to compare
                                against a non-node""");
                

        def __gt__(self, other):
            """
            greater than comparison to other node
            """
            #instance comparison
            if isinstance(other, BinarySearchTree.Node):
                return self.key > other.key;
            else:
                raise Exception("""ammm...you are trying to compare
                                against a non-node""");

        def __eq__(self, other):
            """
            equal to comparison to other node

            params:
            other - another Node object being compared too

            returns:
            bool - returns True, if the two are the same; false, otherwise.
            """
            #instance compare
            if isinstance(other, BinarySearchTree.Node):
                return self.key == other.key;
            elif other == None:
                return other;
            else:
                raise Exception("""ammm...you are trying to compare
                                against a non-node""");




    def insert(self, key, value):
        """
        inserts a key, value pair into the tree
        """

        if self.root == None:
            #set as root
            self.root = BinarySearchTree.Node(key, value);

        else:
            #recursively insert
            self._insert(self.root, key, value);
            
            
    def _insert(self,node, key, value):
        """
        recursively sinks the key and value pair to find an appropriate position
        """

        #base case - i.e. NULL edge
        if node == None:
            return BinarySearchTree.Node(key , value);

        #recusively traverse down to appropariate position
        if key < node.key: #less
            node.left = self._insert(node.left, key, value);
        elif key > node.key: #greater
            node.right = self._insert(node.right, key, value);
        else: #same - Overwrite old value
            node.value = value;

        return node;

    def get(self, key):
        """
        returns the value associated with the key

        params:
        key - key associated with the value

        returns:
        value - value associated with the key
        """

        #set current as root
        node = self.root;
        
        #search
        while node != None:
            #traverse down
            if key < node.key: #less
                node = node.left;
            elif key > node.key:#greater
                node = node.right;
            else: #match - hit
                return node.value;
                
        #key not found - miss
        return None;
        
        


        
bst = BinarySearchTree();
bst.insert(key= 'A', value = 20);
bst.insert(key= 'B', value = 30);
bst.insert(key= 'D', value = 50);
print bst;

print bst.get('D');

