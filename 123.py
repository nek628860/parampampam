import pyowm

owm = pyowm.OWM('e878873e293b20d87b9a674afbb66c9a', language='ru')  
place=input('какой город?')

observation = owm.weather_at_place(place)
w = observation.get_weather()                    
observation_list = owm.weather_around_coords(-22.57, -43.12)
print('влажность-'+str(w.get_humidity()))
print('сейчас '+str(w.get_detailed_status()))
print('температура '+str(w.get_temperature('celsius')['temp']))
if float(w.get_temperature('celsius')['temp'])<15:
         print('оденься потеплее')
elif float(w.get_temperature('celsius')['temp'])>=15:
           print('забей на куртец')
 
input()
