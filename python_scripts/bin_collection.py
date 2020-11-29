# script that calculates what bin goes out 
dt = datetime.datetime.now()
x = (datetime.datetime.date(dt).isocalendar()[1])%2
y = datetime.datetime.date(dt).isocalendar()[1]
if x == 1:
    hass.states.set('sensor.bin_collection', "Recycling + Organics", {
        'friendly_name': "Bin Collection Type",
        'icon': 'mdi:recycle'
    })
elif y == 52 or y == 1:
    hass.states.set('sensor.bin_collection', "Christmas Period - All Bins", {
        'friendly_name': "Bin Collection Type",
        'icon': 'mdi:stocking'
    })
else:
    hass.states.set('sensor.bin_collection', "General Waste + Organics", {
        'friendly_name': "Bin Collection Type",
        'icon': 'mdi:delete'
    })

