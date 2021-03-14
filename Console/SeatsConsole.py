from Models.Constants import ConsoleColors


class SeatsConsole:

    def __init__(self, seats_service) -> None:
        self._seats_service = seats_service
        
    def load(self, seats) -> None: 
        reserved_seats = self._seats_service.get_reserved()
        updated_seats = [[self._load_seat_with_reservation_status(reserved_seats, seat) for seat in row] for row in seats]
        self._print_to_console(updated_seats)

    def _print_to_console(self, updated_seats):
        console = ''
        for updated_seats_row in updated_seats:
            for updated_seat in updated_seats_row:
                console += f'{updated_seat}'
                if updated_seats_row.index(updated_seat) != len(updated_seats_row) - 1: console += ' - '
            console+='\n'
        print(console)


    def _load_seat_with_reservation_status(self, reserved_seats, seat) -> str:
        for reserved_seat in reserved_seats:
            if seat == reserved_seat: return f'{ConsoleColors.RED}{ConsoleColors.BOLD}{seat}{ConsoleColors.DEFAULT}'
        return f'{ConsoleColors.GREEN}{ConsoleColors.BOLD}{seat}{ConsoleColors.DEFAULT}'
    
