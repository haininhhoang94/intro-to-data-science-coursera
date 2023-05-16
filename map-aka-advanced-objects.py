class Person:
    department = "School of Information"

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name("Christopher Brooks")
person.set_location("Ann Arbor, MI, USA")
print("{} live in {} and works in the department {}".format(
    person.name, person.location, person.department
))

# Map function
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
list(cheapest)

# Problems

