#sensores

from sense_hat import SenseHat
sense = SenseHat()
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

message = "Temperatura: " + str(t) + " Presion: " + str(p) + " Humedad: " + str(h)+"%"
sense.show_message(message, scroll_speed=0.05)
