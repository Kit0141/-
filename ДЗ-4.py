class Worker:

    def __init__(self, salary=15):
        self.salary = salary


    def work(self):
        print('Этот рабочий получает', self.salary, '$ в час.')


    def __del__(self):
        print("Этот парень был из тех, кто просто любил жить.")

class Driver(Worker):

    def __init__(self, salary=60000):
        self.salary = salary


    def work(self):
        print('Этот водила получает', self.salary, '$ в месяц.')

