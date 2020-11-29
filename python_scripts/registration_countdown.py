"""
Script to create a sensor displaying the number of days until some event.
Automate to update every day. found somewhere on the hass forums, modified for own use
"""
x = datetime.datetime.now()

EVENT = 'car_registration'
YEAR = x.year + 1
MONTH = 1
DAY = 18

day_of_interest = datetime.datetime(YEAR, MONTH, DAY)
now = datetime.datetime.now()
diff = day_of_interest - now

hass.states.set('sensor.' + EVENT, diff.days,{
    'unit_of_measurement': 'days',
    'friendly_name': 'Registration',
    'icon': 'mdi:calendar'
})
