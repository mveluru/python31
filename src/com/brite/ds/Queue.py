class Queue:

    def __init__(self, queuesize):
        self.queueSize = queuesize
        self.queue = [0] * self.queueSize
        self.rear = -1
        self.currentSize = 0
        self.front = 0

    def isQueuefull(self):
        return self.currentSize == len(self.queue)

    def isQueueEmpty(self):
        return self.currentSize == 0

    def enqueue(self, data):
        if not self.isQueuefull():
            self.rear += 1
            self.queue[self.rear] = data
            self.currentSize += 1
            print('Added element: ', self.queue[self.rear])
        else:
            print('queue is full')

    def dequeue(self):
        if not self.isQueueEmpty():
            element = self.queue[self.front]
            self.front += 1
            self.currentSize -= 1
            print("Dequeued element: ", element)
        else:
            print("Queue is empty")

    def resetQueue(self):
        self.__init__(self.queueSize)


def testQueue():
    queue = Queue(10)
    for i in range(1, 12):
        queue.enqueue(i)
    for i in range(1, 12):
        queue.dequeue()


testQueue()
