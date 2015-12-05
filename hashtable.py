class HashTable:

    """
    A Hash table class
    
    """
    
    #CONSTANTS
    __LINEAR_PROBING= 1;
    
    
    
    def __init__(self, size, hashfn= None, collisionHandler = None):
        """
        Constructor for the Hash table

        Args:
        table_size (int) - size of hash table

        Returns:
        HashTable (Obj) - Hash table object with the given size
        
        """
            
        #set size and table 
        self.size = size;
        self.table = None;
        self.conflict_count = 0;

        #assign handler
        if collisionHandler != None:
            self.collisionHandler = __LINEAR_PROBING;

        #assign hash function
        if hashfn != None:
            self.hashfn = hashfn;
        else:
            self.hashfn = self.__hashfn2;

        #create table
        self.createTable();

    def __hashfn1(self, value):
        """
        Default hash function - Remainder method (Only for int)

        Args:
        value (int) - Value to be hased

        Returns:
        key (int) - Integer index for the table
        """

        #hash item
        key = value % self.size;
        
        return key;

    def __hashfn2(self, value):
        """
        Hash function - Using pythons built in hash function

        Args:
        value (Obj) - A 'Hashable' object

        Returns:
        key (int) - Integer index for the table
        """

        key = hash(value) * 31;
        return key % self.size;

    def createTable(self):
        """
        Creates the given table 
        """
        N = self.size;
        self.table = [None for item_i in range(0, N)];

        #asset its the required size
        assert len(self.table) == self.size;
        #assert table item 0 is intialized to None
        assert self.table[0] == None;


    def insert(self, item):

        """
        Inserts the item into the Hash table.

        Args:
        item (Obj) - The item to be inserted
        """

        #hash the value to get the key
        key = self.hashfn(item);

        
            
        #store item at key
        if self.table[key] != None:
            self.table[key] = item;
        else:
            self.conflict_count += 1;
            

    def search(self, item):
        """
        Search for an return the given item if its in the table, and None otherwise.

        Args:
        item (Obj) - item to be searched

        Returns:
        item (Obj) - item (if its found) or None otherwise.
        
        """

        #hash the item to get the key
        key = self.hashfn(item);
    
        #check the table
        found_item = self.table[key];

        
        return found_item;

    

        

        
        

    def __repr__(self):
        """
        String representation of Hash table
        """

        return "< HashTable \n-size:{0}\n-items:{1} >".format(self.size, self.table);

        


c = HashTable(256);

#print sorted([1,2, 0, 9, 2,29]);
       


