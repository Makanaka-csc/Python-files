# Program  to extract useful data from a raw data stream obtained from a sensor
# Makanaka Mangwanda
# 02 April 2024


# slicing the block from begein to end
def get_block(data):
   
   begin_index = data.find('BEGIN')
   end_index = data.find('END')

   raw = data[begin_index:end_index]
   return raw


# get the location
def location(block):
   location =block[block.find(',')+1: block.find('END')]
   location = location[location.find(' '):]
   location=location[::-1]
   location = location.lower().title()

   return location
    
    

# get the temperature
def temperature(block):
   temperature = block[block.find(' ')+1:block.find('_')]
   return eval(temperature)

   
# find the x_coordinate
def x_coordinate(block):
   x_coordinate = block[block.find(' '):block.find(',')]
   x_coordinate = x_coordinate[x_coordinate.find(':')+1:]
   return x_coordinate

# find the y_coordinate
def y_coordinate(block):
   y_coordinate =block[block.find(',')+1:block.find('END')]
   y_coordinate = y_coordinate[:y_coordinate.find(' ')]
   return  y_coordinate


# find the pressure
def pressure(block):
   pressure =block[block.find('_')+1:block.find(':')]
   return eval(pressure)


        

def main():
   data = input("Enter the raw data:\n")
   block = get_block(data)
   print('Site information:')
   print('Location:', location(block))
   print('Coordinates:', y_coordinate(block), x_coordinate(block))
   print('Temperature: {:.2f} C'.format(temperature(block)))
   print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
   main()
