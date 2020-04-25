class Flight:

    def __init__(self, number, aircraft):
        self.number = number
        self.aircraft = aircraft
        rows, seats = self.aircraft.seating_plan()
        self.seating = [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self.aircraft.model()

    def number(self):
        return self.number

    def airline(self):
        return self.number[:2]

    def book_seat(self, seat, passenger):
        # Example seat: '17A'
        row = int(seat[:-1])
        column = seat[-1]
        self.seating[row][column] = passenger


class Aircraft:

    def __init__(self, model, num_rows_seats, num_column_seats):
        self.model = model
        self.num_rows_seats = num_rows_seats
        self.num_column_seats = num_column_seats

    def model(self):
        return self.model

    def seating_plan(self):
        return (range(1, self.num_rows_seats + 1),
                "ABCDEFGHJK"[:self.num_column_seats])
