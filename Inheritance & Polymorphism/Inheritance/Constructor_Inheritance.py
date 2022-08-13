# Here son class inheritade with father class using constructor mathod
class father:
    def __init__(self) -> None:
        self.property=9000000.0
    def display_property(self):
        print('Father\'s Property=',self.property)
class son(father):
    def __init__(self) -> None:
        pass
s=father()
s.display_property()


# Overriding Super Class Constructor and Methods
class father:
    def __init__(self):
        self.property=800000.0
    def display_property(self):
        print('Father\'s property=',self.property)
class son(father):
    def __init__(self):
        self.property=200000.0
    def display_property(self):
        print('Son\'s property=',self.property)
s1=son()
s1.display_property()
