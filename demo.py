# ejemplo 1
# class Car:
#
#   def __init__(self, brand, color, year):
#       #variable privada
#   	  self._year = year #variable setter
#
#
# car_1 = Car("MiniCooper", "Blue", "2017")
#
# print(car_1._year)
# #>> 2017

# ejemplo 2
# class Car:
#
#   def __init__(self, brand, color, year):
#       #variable privada
#   	  self._year = year
#   	  #variable oculta
#   	  self.__brand = brand
#   	  self.__color = color
#
#
# car_1 = Car("MiniCooper", "Blue", "2017")
#
# print(car_1._year)
# print(car_1._Car__brand)

# ejemplo 3
class Car:

  def __init__(self, brand, color):
  	  self.__brand = brand
  	  self.__color = color

  #métodos getter
  def get_brand(self):
      return self.__brand

  def get_color(self):
      return self.__color

  #métodos setter
  def set_brand(self, value):
      self.__brand = value

  def set_color(self, value):
      self.__color = value

  brand = property(get_brand, set_brand)
  color = property(get_color, set_color)

car_1 = Car("MiniCooper", "Blue")

#método getter `brand` para obtener marca
print(car_1.brand)
#>>"MiniCooper"

#método getter `color` para obtener color
print(car_1.color)
#>>"Blue"

#método setter `color` para asignar nuevo valor al color
car_1.color = "Red"

print(car_1.color)
#>>"Red"
