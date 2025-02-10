import turtle
from math import cos, sin, radians


class FlowerArt:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("LightSkyBlue")
        self.screen.title("Flores para ti ❤️")
        
        self.t = turtle.Turtle()
        self.t.pensize(4)
        self.t.shape("turtle")
        self.t.speed(0)  # Máxima velocidad

    def go(self, x, y):
        """Mover tortuga a una posición sin dibujar"""
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def draw_petal_shape(self, color_pen, color_fill, positions):
        """Dibuja una forma de pétalo con coordenadas específicas"""
        self.t.pencolor(color_pen)
        self.t.fillcolor(color_fill)
        
        self.go(positions[0][0], positions[0][1])
        self.t.begin_fill()
        
        for pos in positions:
            self.t.setheading(pos[2])
            self.t.circle(pos[3], pos[4])
            
        self.t.end_fill()

    def draw_center(self, x, y, size):
        """Dibuja el centro circular de una flor"""
        self.go(x, y)
        self.t.begin_fill()
        self.t.setheading(90)
        self.t.circle(size)
        self.t.end_fill()

    def draw_leaf(self, x, y, angle, color_dark, color_light):
        """Dibuja una hoja con degradado"""
        self.t.pencolor(color_dark)
        self.t.fillcolor(color_light)
        
        self.go(x, y)
        self.t.begin_fill()
        self.t.setheading(angle)
        self.t.circle(75.51, 121.08)
        self.t.setheading(angle + 175.82)
        self.t.circle(72.70, 129.82)
        self.t.end_fill()

    def draw_flower(self, x, y, color_pen, color_fill):
        """Dibuja una flor completa con pétalos y centro"""
        # Pétalos
        self.t.pencolor(color_pen)
        self.t.fillcolor(color_fill)
        
        angles = [330.2, 42.2, 114.2, 186.2, 258.2]
        self.go(x, y)
        
        self.t.begin_fill()
        for angle in angles:
            self.t.setheading(angle)
            self.t.circle(22.66, 236.14)
        self.t.end_fill()
        
        # Centro de la flor
        self.t.pencolor("Gold")
        self.t.fillcolor("Gold")
        self.go(x-4.81, y+20.88)
        self.t.begin_fill()
        self.t.setheading(90)
        self.t.circle(22.5)
        self.t.end_fill()

    def add_sparkles(self):
        """Añade destellos decorativos"""
        sparkle_positions = [
            (100, 100), (-100, 100), (0, 150),
            (150, 50), (-150, 50), (75, 125),
            (-75, 125), (125, 75), (-125, 75)
        ]
        
        original_pensize = self.t.pensize()
        self.t.pensize(2)
        self.t.color("white")
        
        for x, y in sparkle_positions:
            self.go(x, y)
            for _ in range(4):
                self.t.forward(5)
                self.t.backward(5)
                self.t.right(90)
                
        self.t.pensize(original_pensize)

    def create_art(self):
        # Dibujar formas base
        petal_positions = [
            [(40.03, -163.53, 104.91, 120.54, 29.94),
             (None, None, 49.57, -315.30, 15.58),
             (None, None, 33.99, 172.07, 64.94),
             (None, None, 185.9, 227.51, 53.26),
             (None, None, 239.17, 99.15, 72.41),
             (None, None, 213.649, 74.25, 50.32),
             (None, None, 339.29, 108.41, 47.43)],
            
            [(-37.02, -69.53, 98.75, -121.74, 54.75),
             (None, None, 131.6, 187.54, 48.16),
             (None, None, 253.4, 134.51, 95.25)],
            
            [(69.69, -55.52, 184.72, 90.59, 53.66),
             (None, None, 127.63, 111.93, 45.5),
             (None, None, 234.89, 80.10, 70.23),
             (None, None, 9.8, 152.91, 31.68),
             (None, None, 311.3, 108.05, 42.6),
             (None, None, 58.45, 88.07, 63.09)]
        ]

        for positions in petal_positions:
            self.draw_petal_shape("DarkKhaki", "Khaki", positions)

        # Dibujar centro principal
        self.t.pencolor("MediumVioletRed")
        self.t.fillcolor("HotPink")
        self.draw_center(16.3, -99.27, 19.5)

        # Dibujar hojas
        leaf_configs = [
            (-79.30, 110.03, 165.01, "DarkGreen", "LimeGreen"),
            (-122.12, 151, 79.67, "DarkGreen", "LimeGreen"),
            (-100.51, 123.98, 119.46, "DarkGreen", "LawnGreen"),
            (-90.46, 135.14, 22.07, "DarkGreen", "LawnGreen")
        ]

        for config in leaf_configs:
            self.draw_leaf(*config)

        # Dibujar flores
        flower_configs = [
            (155.36, 115.58, "Tomato", "Orange"),
            (60.97, 170, "SteelBlue", "DarkTurquoise"),
            (45.377, 120, "IndianRed", "LightSalmon"),
            (-11.60, 41.39, "MediumOrchid", "Violet"),
            (65.71, 85.27, "DarkGray", "White")
        ]

        for config in flower_configs:
            self.draw_flower(*config)

        # Añadir destellos
        self.add_sparkles()

        # Escribir mensaje
        self.t.color("Chocolate")
        self.go(100, -250)
        self.t.write("I LOVE YOU  ❤️", False, "center", 
                    ("Bradley Hand ITC", 40, "bold"))

        self.t.hideturtle()
        self.screen.exitonclick()

if __name__ == "__main__":
    art = FlowerArt()
    art.create_art()