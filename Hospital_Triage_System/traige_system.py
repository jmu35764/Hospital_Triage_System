from itertools import count
from heapq import heappush, heappop

class Triage_System():
    def __init__(self):
       self.pq = []
       self.counter = count()
       
    def add_patient(self, name, severity):
        if not isinstance(name, str) or name == " ":
            try:
                raise ValueError("Invalid Name")
            except ValueError as e:
                return print("ERROR ->", e)
        if severity > 5 or severity < 1 or not isinstance(severity, int):
            try:
                raise ValueError("Invalid Name")
            except ValueError as e:
                return print("ERROR ->", e)

        heappush(self.pq, (-severity, next(self.counter), name))

    def process_next(self):
        patient = heappop(self.pq)
        return patient[2], patient[0]-1

if __name__ == "__main__":

    test_01 = Triage_System()
    test_01.add_patient("Sally", 4)
    test_01.add_patient("Mike", 3)
    test_01.add_patient("Tracy", 1)
    test_01.add_patient("Tim", 1)
    test_01.add_patient("Paulo", 4)
    print(test_01.pq)
    #print(test_01.process_next())
    #print(test_01.pq[0])
    #print(test_01.pq[1])
    print(test_01.process_next())
    print(test_01.pq)




