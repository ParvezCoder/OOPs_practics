class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start  # initialize the current number
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# Test the Countdown class
for number in Countdown(5):
    print(number)
