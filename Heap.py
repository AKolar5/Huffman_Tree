

class Heap:

    def __init__(self):
        self.__capacity = 1
        self.__contents = [None] * self.__capacity
        self.__size = 0

    def __len__(self):
        return self.__size

    def insert_element(self, value):
        # Grow array if necessary
        if self.__size + 1 > self.__capacity:
            self.__grow()
        
        # Put values in next unoccupied cell in contents
        self.__contents[self.__size] = value
        
        index = self.__size
        
        # Place the value in its proper cell
        while index > 0:
            if index % 2 == 0:
                if self.__contents[index//2-1] > value:
                     temp = self.__contents[index//2-1] 
                     self.__contents[index//2-1] = value
                     self.__contents[index] = temp
                     index = index//2-1
                else:
                    break
            elif index % 2 != 0:
                if self.__contents[index//2] > value:
                    temp = self.__contents[index//2] 
                    self.__contents[index//2] = value
                    self.__contents[index] = temp
                    index = index//2
                else:
                    break

        self.__size += 1

    def remove_element(self):
        # Stores value at index zero (root)
        # Sets last value in array as index 0
        to_return = self.__contents[0]
        self.__contents[0] = self.__contents[self.__size-1]
        self.__contents[self.__size-1] = None
        self.__size -= 1

        value = self.__contents[0]
        index = 0

        # Moves the new value at index 0 to its proper place
        while index < (self.__size//2):
            if self.__contents[index*2+1] is None and self.__contents[index*2+2] is None:
                break
            
            elif self.__contents[index*2+1] is None:
                if self.__contents[index*2+2] < value:
                    temp = self.__contents[index*2+2]
                    self.__contents[index*2+2] = value
                    self.__contents[index] = temp
                    index = index*2+2
                else:
                    break

            elif self.__contents[index*2+2] is None:
                if self.__contents[index*2+1] < value:
                    temp = self.__contents[index*2+1]
                    self.__contents[index*2+1] = value
                    self.__contents[index] = temp
                    index = index*2+1
                else:
                    break

            elif self.__contents[index*2+2] < self.__contents[index*2+1]:
                if self.__contents[index*2+2] < value:
                    temp = self.__contents[index*2+2]
                    self.__contents[index*2+2] = value
                    self.__contents[index] = temp
                    index = index*2+2
                else:
                    break
            elif self.__contents[index*2+1] <= self.__contents[index*2+2]:
                if self.__contents[index*2+1] < value:
                    temp = self.__contents[index*2+1]
                    self.__contents[index*2+1] = value
                    self.__contents[index] = temp
                    index = index*2+1
                else:
                    break

        return to_return  

    # Doubles size of the contents array
    def __grow(self):
    

        self.__capacity *= 2 #double capacity
        old_array = self.__contents #make an alias for contents
        self.__contents = [None] * (self.__capacity) #assign self.contents to an empty array with new cap
        
        # put items from old array into self.__contents
        
        for i in range(len(old_array)):
            self.__contents[i] = old_array[i]

        
    # String method for testing
    def __str__(self):
    
        # special case
        if self.__size == 0:
            return '[ ]'
        
        # put deque values into an ordered array
        # front at index zero
        lst = [None] * self.__size
        for i in range(len(lst)):
            lst[i] = str(self.__contents[i])
        
        string = '[ ' + ', '.join(lst) + ' ]'
        return string

        

if __name__ == '__main__':
    pass
