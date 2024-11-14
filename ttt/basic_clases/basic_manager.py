from basic_clases.basic_seller import Seller
from basic_clases.basic_user import User


class Manager(Seller):
    def __init__(self, data):
        super().__init__(data)

    def doing(self):
        inp = str(input('1 -- read doc\n'
                        '2 -- read acc\n'
                        'ex -- end session\n'
                        ': '))
        if inp == '1':
            self.reading_doc()
        elif inp == '2':
            self.reading_accs()
        elif inp == 'ex':
            return
