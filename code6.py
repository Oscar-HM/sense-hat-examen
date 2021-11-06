#creeper

from sense_hat import SenseHat
sense = SenseHat()

g = (0, 255, 0)
b = (0, 0, 0)

pantalla = [
 g, g, g, g, g, g, g, g,
 g, g, g, g, g, g, g, g,
 g, b, b, g, g, b, b, g,
 g, b, b, g, g, b, b, g,
 g, g, g, b, b, g, g, g,
 g, g, b, b, b, b, g, g,
 g, g, b, b, b, b, g, g,
 g, g, b, g, g, b, g, g
]

for i in range(1):
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
x=round(x, 0)
y=round(y, 0)
z=round(z, 0)
print("x={0}, y={1}, z={2}".format(x, y, z))
  
if x == -1:
  sense.set_rotation(180)
  sense.set_pixels(pantalla)
elif y == 1:
  sense.set_rotation(90)
  sense.set_pixels(pantalla)
elif y == -1:
  sense.set_rotation(270)
  sense.set_pixels(pantalla)
else:
  sense.set_rotation(0)
  sense.set_pixels(pantalla)
