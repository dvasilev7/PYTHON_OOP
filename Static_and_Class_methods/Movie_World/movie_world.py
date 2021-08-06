class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
            return True
        return False

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
        customer = list(filter(lambda x: x.id == customer_id, self.customers))[0]
        if dvd.id in [d.id for d in customer.rented_dvds]:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = list(filter(lambda x: x.id == customer_id, self.customers))[0]
        if dvd_id in [d.id for d in customer.rented_dvds]:
            dvd = list(filter(lambda d: d.id == dvd_id, self.dvds))[0]
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        customers = "\n".join([c.__repr__() for c in self.customers])
        dvds = "\n".join([d.__repr__() for d in self.dvds])
        result += f'{customers}\n'
        result += dvds
        return result



