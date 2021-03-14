from Models.Constants import SEATS_LETTERS


class Fuselage:

    def __init__(self, rows, seats_per_row) -> None:
        self._rows = rows
        self._seats_per_row = seats_per_row
        self._seats = list(list(f'{row}{letter}' for letter in SEATS_LETTERS[:self._seats_per_row]) for row in range(1, self._rows + 1))
    
    def get_seats(self): return self._seats