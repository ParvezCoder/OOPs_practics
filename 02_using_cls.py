# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of
#  how many objects have been created. Use a class variable
#  and a class method with cls to manage and display the count.
class Counter():
    count = 0

    def __init__(self):
        Counter.count +=1
    @classmethod
    def display(cls):
        print(f"total object created {cls.count}")

dis = Counter()
dis = Counter()
dis3 = Counter()
dis.display()
