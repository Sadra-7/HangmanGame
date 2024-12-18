from data_access_layer.sql_data import Get_data

import random

data = Get_data()



class Business:
    def __init__(self):
        names = data.get_names()
        self.name_list = []
        self.letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
            , 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        for i in names:
            str_name = str(i).upper()
            for a in str_name:
                if a not in self.letter_list:

                    str_name = str_name.replace(a, "")

            self.name_list.append(str_name)

    def get_random_name(self):
        max_index = len(self.name_list) - 1
        random_index = random.randint(0 , max_index)
        current_name = self.name_list[random_index]
        self.name_list.remove(current_name)

        return current_name



