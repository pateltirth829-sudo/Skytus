class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat Booked")
            print("Remaining Seats =", self.seats)
        else:
            print("No Seats Available")

f = Flight(5)

f.book_seat()
f.book_seat()