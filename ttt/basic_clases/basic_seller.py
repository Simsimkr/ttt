from basic_clases.basic_user import User


class Seller(User):
    def __init__(self, data):
        super().__init__(data)

    def doing(self):
        while True:
            inp = str(input('1 -- work\n'
                            'ex -- end session\n'
                            ': '))
            if inp == '1':
                self.work()
            elif inp == 'ex':
                return
