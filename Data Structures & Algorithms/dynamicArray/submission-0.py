class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []

    def get(self, i: int) -> int:
        for idx in range(len(self.array)):
            if idx==i:
                return self.array[idx]


    def set(self, i: int, n: int) -> None:
        for idx in range(len(self.array)):
            if idx==i:
                self.array[idx]=n

    def pushback(self, n: int) -> None:
        if self.capacity<= len(self.array):
            self.resize()
        self.array.append(n)

    def popback(self) -> int:
        pop_val = self.array[-1]
        self.array = self.array[:-1]
        return pop_val

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity
