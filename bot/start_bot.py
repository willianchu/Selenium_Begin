from booking_package.booking import Booking

# Version 1.0
# inst = Booking()
# inst.land_first_page()

with Booking(teardown=True) as bot:
  bot.land_first_page()
  print('Closing bot...')