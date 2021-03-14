from Models.Aircrafts.PrivateJet import PrivateJet
from Models.Aircrafts.Airbus import AirBus
from Services.SeatsService import SeatsService
from Console.SeatsConsole import SeatsConsole

airbus = AirBus('AB123')

seats_service = SeatsService()

seats_console = SeatsConsole(seats_service)

seats_console.load(airbus.get_seats())

airbus.start_engine()

airbus.stop_engine()