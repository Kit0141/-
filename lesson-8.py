class SimpleIterator:
    def __init__(self, limit=10):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration
# ----------------------------------------------------------------------------------------------

def simple_generator(val=10):
    while val > 0:
        val -= 1
        yield val

        yield val + 23

gen_iter = simple_generator()

# ----------------------------------------------------------------------------------------------

some_list = [1, 2, 3, 4]
new_list = [x ** 2 for x in some_list if x % 2 == 0]  # представление списка
print(new_list)

# ----------------------------------------------------------------------------------------------