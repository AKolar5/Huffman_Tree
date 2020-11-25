from Heap import Heap

# BASE STRUCTURE TO HOLD NODES/OTHER TREES
class Tree:
    def __init__(self, root, left, right):
        self.__root = root
        self.__left = left
        self.__right = right

    def get_freq(self):
        return self.__root

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_value(self):
        return self

    # DEFINE EQUALITY/INEQUALITIES TREES CAN BE USED IN HEAPS
    # FREQ IS SIZE

    def __eq__(self, other):
        return self.get_freq() == other.get_freq()

    def __gt__(self, other):
        return self.get_freq() > other.get_freq()

    def __lt__(self, other):
        return self.get_freq() < other.get_freq()

    def __ge__(self, other):
        return self.get_freq() >= other.get_freq()

    def __le__(self, other):
        return self.get_freq() <= other.get_freq()

    def __ne__(self, other):
        return self.get_freq() != other.get_freq()

    # String method for testing
    def __str__(self):
        return str(self.__left) + ',' + str(self.__root) + ',' + str(self.__right) 
        

# NODE CLASS THAT STORES BASE LETTERS AND FREQUENCIES
class Huffman_Node:
    def __init__(self, val, frequency):
        self.__value = val
        self.__freq = frequency

    # DEFINE EQUALITY/INEQUALITIES TREES CAN BE USED IN HEAPS
    # FREQ IS SIZE
    
    def __eq__(self, other):
        return self.get_freq() == other.get_freq()

    def __gt__(self, other):
        return self.get_freq() > other.get_freq()

    def __lt__(self, other):
        return self.get_freq() < other.get_freq()

    def __ge__(self, other):
        return self.get_freq() >= other.get_freq()

    def __le__(self, other):
        return self.get_freq() <= other.get_freq()

    def __ne__(self, other):
        return self.get_freq() != other.get_freq()
    
    def get_value(self):
        return self.__value

    def get_freq(self):
        return self.__freq

    def get_left(self):
        return None

    def get_right(self):
        return None

    # String method for testing
    def __str__(self):
        return str(self.__value)


# TURNS A GIVEN STRING AN ALPHABATIZED ARRAY OF HUFFMAN NODES
def create_Nodes(string):
    lst = []
    # Add unique letters into lst
    for i in string:
        if i not in lst:
            lst.append(i)
    
    lst.sort()

    Nodes = []
    # New array 'Nodes' holds Huffman nodes based on lst
    for i in lst:
        Nodes.append(Huffman_Node(i, string.count(i)))

    return Nodes

# Takes a list of Huffman Nodes and makes a Huffman Tree 
# Uses Heap implementation
def create_huffman_tree(list_of_nodes):
    heap = Heap()

    # Initial Huffman Nodes are inserted into a heap
    for i in list_of_nodes:
        heap.insert_element(i)

    while len(heap) != 1:
        # Takes the top two Nodes in the heap, combines them into
        # tree and inserts the tree back into the Heap
        r1 = heap.remove_element()
        r2 = heap.remove_element()
        t = Tree(r1.get_freq()+r2.get_freq(), r1, r2)
        
        heap.insert_element(t)


    # The final tree element is the huffman tree
    huffman_tree = heap.remove_element()
    
    return huffman_tree

# Turns a Huffman Tree into a dictionary with the optimal binary as the keys
# and the letters as their values
def get_binary(tree, vals, binary = ''):
    
    # Base Case
    if tree.get_left() is None and tree.get_right() is None: 
        
        vals[binary] = tree.get_value()
        
    # Recursive case, go left, add 0 to binary representation    
    if tree.get_left() is not None:
        
        get_binary(tree.get_left(), vals, binary + '0')

    # Recursive case, go right, add 1 to binary representation
    if tree.get_right() is not None:
        
        get_binary(tree.get_right(), vals, binary + '1')
    
    return vals

# Takes a binary string a huffman dictionary and decodes using the 
# dictionary keys
def decode(string, dictionary):
    while len(string)<1:
        string = input('Invalid binary input. Try again: ')
    
    # Find longest key in the dictionary
    longest = 0
    for key in dictionary:
        if len(key) > longest:
            longest = len(key)
    
    out = ''
    k = ''
      
    for i in string:
        # Add a character from the string to k
        k += i
        
        # If the string k is longer than the longest key, the input must be invalid
        if len(k) > longest:
                string = input('Invalid binary input. All numbers must match a given encoding. Try again: ')
                return decode(string, dictionary)
        
        # Compare k to eack of the keys in the dictionary
        # Add a character to the output string if appropriate
        # Shorten string to dispose of already decoded binary
        for j in dictionary:
                
            if k == j:
                out += dictionary[j]
                string = string[len(k):]
                k = ''
                break
                
                
    # If k has any left over characters, the input must have been invalid
    if len(k) > 0:
        string = input('Invalid binary input. All numbers must match a given encoding. Try again: ')
        return decode(string, dictionary)

    else:
        return out

# Interacts with the user to recieve binary and print it's translation
def output_decode(dictionary):
    new_string = input('\nEnter a binary string to be decoded: ')

    decoding = decode(new_string, dictionary)
    print('\nThe decoding of the given binary: ' + decoding + '\n')
    again = input('To decode another binary string, enter \'Y\'.'
                ' To encode a new string, enter \'NEW\'.'
                ' If you are finished, press Enter: ')

    if again.lower() == 'y':
        output_decode(dictionary)

    if again.lower() == 'new':         
        main()

# Prints a huffman dictionary and optimal representation of a the given string
def print_dict(dictionary, string):
    print('\nOptimal binary encodings for each letter:')
    for i in dictionary:
        print(dictionary[i] + ': ' + i)

    out = ''
    for j in string:
        for k in dictionary:
            if j == dictionary[k]:
                out += k
                break  
    
    
    print('\nOptimal binary of string \'' + string + '\': ' + out)
    print('Optimal number of bits: ' + str(len(out)))


def main():
    string = input('\nInput a string to encode: ')
    while len(string) < 2:
        print('Not enough letters. Try again.')
        string = input('\nInput a string to encode: ')

    nodes = create_Nodes(string)
    
    ht = create_huffman_tree(nodes)
  
    values = {}    
    bi_dict = get_binary(ht, values)
    
    print_dict(bi_dict, string)

    output_decode(bi_dict)

if __name__ == '__main__':
    main() 
    


    







             









