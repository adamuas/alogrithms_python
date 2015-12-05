class BinaryTreeNode():
    """
    Binary tree node
    """

    def __init__(self, value = None, parent = None, left =None, right = None):

        self.left = left;
        self.right = right;
        self.value = value;
        self.parent = parent;


    def getParent(self):
        """
        returns the parent of the node
        """
        
        return self.parent;
    
    def getLeftChild(self):
        """
        returns the left child of the node
        """
        return self.left;

    def getRightChild(self):
        """
        returns the right child of the node
        """
        
        return self.right;

    def setNodeValue(self,value):
        """
        sets the node value

        params:
        value - the value to be associated with the node
        """
        self.value = value;

    def getNodeValue(self):
        """
        returns the node's value
        """
        
        return self.value;
    

    def insertLeftChild(self, n):
        """
        inserts a left child to the node

        params:
        n - another binary tree node
        """
        self.left = n;

    def insertRightChild(self, n):
        """
        inserts a right child to the ndoe

        params:
        n - another binary tree node
        """
        self.right = n;

    def __repr__(self):
        """
        returns the string representation of the node
        """
        return "\n<Tree Node value: {0}\n lchild of {0}:{1}\n rchild of {0}: {2}>".format(self.getNodeValue(),
                                                                                self.getLeftChild(),
                                                                                self.getRightChild());


class BinaryTree:

    def __init__(self, rootNode = None):
        """
        Initializes a simple binary tree
        """

        self.rootnode = rootNode;
        


    def insert(self, item):
        """
        Inserts into the binary tree
        """

        if self.rootnode == None:
            self.rootnode = BinaryTreeNode(item);
            
        else:
            self._put(self.rootnode, item);

        print "inserted {0}".format(item);


    def _insert(self, node, item):
        """
        Helper function for the insert
        """

        #compare
        if item < node.getNodeValue():      
            
            if node.getLeftChild() == None: #has no left child
                #insert
                new_child = BinaryTreeNode(item);
                node.insertLeftChild(new_child);
                new_child.parent = node;
                
            else:
                #recursively look for a place to put it
                node = node.getLeftChild();
                self._insert(node, item);
        elif item > node.getNodeValue():
            if node.getRightChild() == None: #has no left child
                #insert
                new_child = BinaryTreeNode(item);
                node.insertRightChild(new_child);
                new_child.parent = node;
            else:
                #recursively look for a place to put it
                node = node.getRightChild();
                self._insert(node, item);
        else:
            node.setNodeValue(item);
    
        return;


    def _put(self, node, item):
        """
        #segwick implementation
        puts a new item into the binary tree
        """

        #base case
        if node == None:
            return BinaryTreeNode(item);

        #get node value
        value = node.getNodeValue();
        
        if item < node.value: #less
            #set left child recursively
            node.insertLeftChild(self._put(node.getLeftChild(), item));

        elif item > node.getNodeValue(): #greater
            # set right child recursively
            node.insertRightChild(self._put(node.getRightChild(), item));


        return node;

        
        
    def get(self, item):
        """
        returns a specific item from the binary tree
        """
        node = self.rootnode;
        
        while node != None:

            if item < node.getNodeValue(): #less
                node = node.getLeftChild();

            elif item < node.getNodeValue(): #greater
                node = node.getRightNode();

            else:
                return node.getNodeValue();


        return None;
                

        
    

    def remove(self,item):
        """
        Removes item form the tree
        """
        node = self.rootnode;
        
        while node != None and node.getNodeValue() != item:
            prev_node = node;
            if item < node.getNodeValue():
                if node.getLeftChild() != None:
                    node = node.getLeftChild();
                    print "going left";
            elif item < node.getNodeValue():
                if node.getRightChild() != None:
                    node = node.getRightChild();
                    print "going right";

        if node.parent.getRightChild().getNodeValue() == item:
            node.parent.insertRightChild(None);
            node.parent = None;
        else:
            node.parent.insertLeftChild(None);
            node.parent = None;
        
        print "deleted node";
        
        
    
    def traverse_inorder(self, current_node):
        """
        Traverse the tree in-order
        """

        if current_node.getLeftChild():
            self.traverse_preorder(current_node.getLeftChild());
        print "visted:{0} - ".format(current_node.getNodeValue());    
        if current_node.getRightChild():
            self.traverse_preorder(current_node.getRightChild());
        

        
        

    def traverse_postorder(self, current_node):
        """
        Traverse the tree post-order
        """

    
        if current_node.getRightChild():
            self.traverse_preorder(current_node.getRightChild());
        if current_node.getLeftChild():
            self.traverse_preorder(current_node.getLeftChild());

        print "visted:{0} - ".format(current_node.getNodeValue());

    
    def traverse_preorder(self, current_node):
        """
        Traverse the tree post-order
        """

        
        print "visted:{0} - ".format(current_node.getNodeValue());
        
        if current_node.getLeftChild():
            self.traverse_preorder(current_node.getLeftChild());
        if current_node.getRightChild():
            self.traverse_preorder(current_node.getRightChild());

    def inorder(self):
        """
        returns list of inorder nodes in the tree
        """
        lst = [];
        lst = self._inorder(self.rootnode, lst);
        return lst;
        
    def _inorder(self, node, q):
        """
        performs an inorder traversal from a given node 
        """

        #bas case
        if node == None: return;

        self._inorder(node.getLeftChild(), q);
        q.append(node.getNodeValue());
        self._inorder(node.getRightChild(), q);


        return q;
        
            
        

    def getPreorder(self):

        self.traverse_preorder(self.rootnode);
        print self.nodeHistory;

    def clearHistory(self):
        """
        clears node history
        """
        self.nodeHistory = [];

    def __repr__(self):
        """  returns string representation of the tree"""

        return "Binary Tree\nRoot Node: {0}".format(self.rootnode);

    

#Some basic tests
    
tree = BinaryTree();
tree.insert(5);
tree.insert(6);
tree.insert(2);
tree.insert(1);

tree.insert(20);
tree.insert(10);
print tree;

##print "\n * pre-order";
##tree.traverse_preorder(tree.rootnode);
##print "\n * post-order";
##tree.traverse_postorder(tree.rootnode);
##print "\n * in-order";
##tree.traverse_inorder(tree.rootnode);
##        
##print "get:", tree.get(2);
##print tree;

print tree.inorder();
assert tree.inorder() == [1, 2, 5, 6, 10, 20];



    
