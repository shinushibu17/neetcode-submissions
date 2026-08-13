class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        while len(operations):
            i = operations[0]
            if i in "+":
                record.append(sum(record[-2:]))
            elif i in "D":
                record.append(record[-1]*2)
            elif i in "C":
                record.pop()
            else:
                record.append(int(i))
            operations = operations[1:]
        return sum(record)