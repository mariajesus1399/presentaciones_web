from manim import *

class P5EA(Scene):
    def construct(self):
        self.camera.background_color = "#005da4"
        Problema = Tex("Problema 5")
        Titulo = Tex("Algunas funciones de densidad de probabilidad")
        Ejercicio = Tex("Ejercicio A")
        Enunciado = Tex("En el artículo ``Evaluación de la fatiga de aspas con aplicaciones en turbinas de viento de eje vertical'' (J. Solar Energy Engr., 1982: 107–111) se hace un estudio del estrés vibratorio de un aspa de viento en un túnel de viento, a una velocidad particular. El autor propone que la v.a. $X$ que denota el estrés vibratorio, medido en librafuerza por pulgada cuadrada (psi), tiene una distribución de Rayleigh con un pdf (donde $\theta$ es una constante positiva) dado por", font_size=24)
        Eq1 = MathTex(r"\frac{x}{\theta^2} e^{-x^2/(2\theta^2)} & x > 0 \\")
        Titulo.next_to(Problema,DOWN)
        self.play(Write(Problema))
        self.play(Write(Titulo))
        #self.add(Problema, Titulo)
        self.wait(2)
        Titulo.shift(5*UP)
        Problema.shift(5*UP)
        self.play(ApplyMethod(Ejercicio.shift,3*UP))
        self.play(ApplyMethod(Enunciado.shift,1*UP))
        self.play(ApplyMethod(Eq1.shift,1*DOWN))
        #self.play(Write(enunciado))
