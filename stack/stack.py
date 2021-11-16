class Stack:
    def __init__(self):
        self.__list = []
        self.__top = 0

    def push(self, no):
        self.__list.append(no)
        self.__top=+1
    
    def pop(self):
        if self.__top <= 0:
            raise Exception("Empty stack cannot pop")
        ans = self.__list[self.__top-1]
        del self.__list[self.__top-1]
        self.__top=-1
        return ans
    
    def is_empty(self):
        if not len(self.__list):
            return True
        return False

    def peek(self):
        if self.__top>0:
            return self.__list[self.__top-1]


