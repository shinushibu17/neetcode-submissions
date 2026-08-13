class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if "+" in i:
                record.append(sum(record[-2:]))
            elif i in "C":
                record.pop()
            elif i in "D":
                record.append(record[-1]*2)
            else:
                record.append(int(i))
        return sum(record)