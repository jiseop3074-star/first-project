# a = 10
# print(type(a))
# b = 10.0
# print(type(b))
# print(type(123))
# print(type(123.0))
# print(type("123"))
# print(type(True))
# print(type(10==20))
# print(type((1+2j)))

class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1
    def isEmpty(self):
        if self.top == -1 : return True
        else : return False
    def isFull(self): return self.top == self.capacity

    def push(self,e):
        if not self.isFull():
            self.top +=1
            self.array[self.top] = e
        else:
            print("stack overflow")
            exit()
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            print("stack underflow")
            exit()
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("stack underflow")
            exit()
    def size(self): return self.top+1
s = ArrayStack(100)
n=input()
for i in n:
    s.push(i)
while not s.isEmpty():
    print(s.pop(), end='')
print()
