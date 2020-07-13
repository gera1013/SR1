import struct

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h', w)

def dword(d):
    return struct.pack('=l', d)

def color(r, g, b):
    return bytes([b, g, r])

# función para redondear los números de tipo float
# dos decimales
def roundUp(result):
    new_result = int(result - result % 1)

    if result % 1 == 0:
        return new_result
    elif int(str(result % 1)[2]) > 4:
        return new_result + 1
    elif int(str(result % 1)[3]) > 4:
        return new_result + 1
    else:
        return new_result

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

class Render(object):
    def __init__(self):
        self.glInit()
    
    # no tiene parámetros
    # esta función se ejecuta al crear un objeto de tipo render
    # inicializa las variables necesarias en su valor default
    def glInit(self):
        self.height = 0
        self.width = 0
        self.vp_height = 0
        self.vp_width = 0
        self.vp_start_point_x = 0
        self.vp_start_point_y = 0
        self.clear_color = WHITE
        self.point_color = BLACK

    # (width, height)
    # se inicializa el framebuffer con la altura y ancho indicados
    def glCreateWindow(self, width, height):
        self.height = height
        self.width = width

        return True

    # no tiene parametros
    # se llena el mapa de bits con el color seleccionado
    def glClear(self):
        self.pixels = [[self.clear_color for x in range(self.width)] for y in range(self.height)]

    # (r, g, b) - valores entre 0 y 1
    # define el color con el que se realiza el clear
    def glClearColor(self, r, g, b):
        if r > 1 or r < -1 or g > 1 or g < -1 or b > 1 or b < -1:
            return False
        
        self.clear_color = color(int(r * 255 - r * 255 % 1), int(g * 255 - g * 255 % 1), int(b * 255 - b * 255 % 1))

        return True
    
    # (r, g, b) - valores entre 0 y 1
    # define el color con el que se dibuja el punto
    def glColor(self, r, g, b):
        if r > 1 or r < -1 or g > 1 or g < -1 or b > 1 or b < -1:
            return False

        self.point_color = color(int(r * 255 - r * 255 % 1), int(g * 255 - g * 255 % 1), int(b * 255 - b * 255 % 1))
        return True

    # (x, y, width, height)
    # crea el viewport en donde se podrá dibujar
    # restringe al viewport dentro de la ventana
    def glViewPort(self, x, y, width, height):
        if x > self.width or y > self.height:
            return False
        elif x + width > self.width or y + height > self.height:
            return False
        else:
            self.vp_start_point_x = x
            self.vp_start_point_y = y
            self.vp_width = width
            self.vp_height = height
            return True

    # no tiene parámetros
    # función extra
    # dibuja el contorno del viewport 
    def glDrawViewPort(self):
        for x in range(self.vp_start_point_x, self.vp_start_point_x + self.vp_width):
            self.pixels[self.vp_start_point_y][x] = color(255, 0, 251)
            self.pixels[self.vp_start_point_y + self.vp_height][x] = color(255, 0, 251)
        
        for y in range(self.vp_start_point_y, self.vp_start_point_y + self.vp_height):
            self.pixels[y][self.vp_start_point_x] = color(255, 0, 251)
            self.pixels[y][self.vp_start_point_x + self.vp_width] = color(255, 0, 251)

    # (x, y) - valores entre -1 y 1
    # se crea un punto dentro del viewport
    # las coordenadas son relativas al viewport
    def glVertex(self, x, y):
        new_width = (self.vp_width / 2) - ((self.vp_width / 2) % 1)
        new_height = (self.vp_height / 2) - ((self.vp_height / 2) % 1)
        _x = new_width + self.vp_start_point_x
        _y = new_height + self.vp_start_point_y
        new_x = _x + (x * new_width)
        new_y = _y + (y * new_height)
        self.pixels[roundUp(new_y)][roundUp(new_x)] = self.point_color
    
    # no tiene parámetros
    # renderiza el mapa de bits
    def glFinish(self):
        file = open('SR1.bmp', 'wb')

        # file header
        file.write(bytes('B'.encode('ascii')))
        file.write(bytes('M'.encode('ascii')))
                   
        file.write(dword(14 + 40 + self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(14 + 40))

        # image header
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        # pixels, 3 bytes each
        for x in range(self.height):
            for y in range(self.width):
                file.write(self.pixels[x][y])

        file.close()

