class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            try:
                record.append(int(operations[i]))
            except:
                if "+" in operations[i]:
                    record.append(int(record[-1])+int(record[-2]))
                if "D" in operations[i]:
                    record.append(int(record[-1])*2)
                if "C" in operations[i]:
                    record = record[:-1]

        return sum(record)
