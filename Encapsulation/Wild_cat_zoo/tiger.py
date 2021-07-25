from Wild_cat_zoo.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender, age):
        super(Tiger, self).__init__(name, gender, age, money_for_care=45)