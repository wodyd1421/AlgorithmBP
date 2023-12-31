class MaxMinQueue() :

    def __init__(self) : 

        self.queue = []

        self.MaxIdx = None

        self.MinIdx = None

    def isEmpty(self) : 

        return not self.queue

    def Insert(self, data=None) :

        if self.isEmpty() :

            self.MaxIdx = 0

            self.MinIdx = 0

            self.queue.append(data)

            return

        if data > self.queue[self.MaxIdx] :

            self.MaxIdx = len(self.queue)

        if data < self.queue[self.MinIdx] :

            self.MinIdx = len(self.queue)

        self.queue.append(data)

    def DeleteMax(self) :

        if self.isEmpty() :

            return

        self.queue.pop(self.MaxIdx)

        if self.MaxIdx < self.MinIdx : 

            self.MinIdx -= 1

        if self.isEmpty() :

            self.MaxIdx = None

            self.MinIdx = None

            return

        self.MaxIdx = self.queue.index(max(self.queue))

    def DeleteMin(self) : 

        if self.isEmpty() : 

            return

        self.queue.pop(self.MinIdx)

        if self.MinIdx < self.MaxIdx : 

            self.MaxIdx -= 1

        if self.isEmpty() :

            self.MaxIdx = None

            self.MinIdx = None

            return

        self.MinIdx = self.queue.index(min(self.queue))

def solution(operations):

    answer = []

    Structure = MaxMinQueue()

    for oper in operations :

        #print(oper)

        deter = oper[0]        

        if deter == 'I' :

            Structure.Insert(int(oper[2:]))

            print(Structure.MaxIdx)

        elif deter == 'D' :

            if int(oper[2:]) == 1 :

                Structure.DeleteMax()

            elif int(oper[2:]) == -1 :

                Structure.DeleteMin()

            else :

                return -1

        else : 

            return -1

    if Structure.isEmpty() : 

        answer = [0, 0]

    else : 

        answer.append(Structure.queue[Structure.MaxIdx])

        answer.append(Structure.queue[Structure.MinIdx])

    return answer