"""code goes here"""
class Door:
    # metodo constructor
    def __init__(self, color, size, status="Cerrado"):
        # Variable de instancia oculta doble __
        self.__color = color
        self.__size = size
        self.__status = status

    #Metodo getter
    @property
    def color(self):
        # Levantar una excepcion de Error
        raise AttributeError("Do not Modify")

    @property
    def size(self):
        return self.__size

    @property
    def status(self):
        return self.__status

    @color.setter
    def color(self, value):
        self.__color = value

    @size.setter
    def size(self, value):
        #self.__size = value
        # Levantar una excepcion de error
        raise AttributeError("Do not Modify")

    @status.setter
    def status(self, value):
        self.__status = value

    # Si status == "Cerrado" return "Business is closed"
    # SI status == "Abierto" return "open" + (self.__color) + "door"
    def open(self):
        if self.__status == "Cerrado":
            return "Business is closed"
        else:
            return "open " + (self.__color) + " door"

    # Si status == "Cerrado" return "Door is closed"
    # SI status == "Abierto" return "closed door of " + srt(self.__size) + " meters" concatena
    def close(self):
        if self.__status == "Cerrado":
            return "Door is closed"
        else:
            return "close door of " + str(self.__size) +  " meters"
