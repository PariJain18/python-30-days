class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = date_string.split("-")
        return cls(int(day), int(month), int(year))

    def display(self):
        print("Day:", self.day)
        print("Month:", self.month)
        print("Year:", self.year)


d1 = Date.from_string("18-09-2026")

d1.display()