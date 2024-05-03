class StackAlgo:
    def __init__(self, stacksize):
        self.stack = [0] * stacksize
        self.top = -1

    def push(self, data):
        if not self.overflow():
            self.top += 1
            self.stack[self.top] = data
        else:
            print('Stack overFlow')

    def pop(self):
        if not self.underflow():
            element = self.stack[self.top]
            self.top -= 1
            print('removed element...:' + str(element))
        else:
            print('Stack Under Flow')

    def underflow(self):
        if self.top == -1:
            return True
        else:
            return False

    def overflow(self):
        if self.top == len(self.stack) - 1:
            return True
        else:
            return False


teststack = StackAlgo(10)
for i in range(1, 20):
    teststack.push(i)
for i in range(0, 5):
    teststack.pop()
