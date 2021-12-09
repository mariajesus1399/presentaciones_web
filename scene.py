from manim import *

class Plantilla(Scene):
    def construct(self):
        #Ingrese en N el número de Problema
        Problema = Tex("Problema N")
        Titulo = Tex("Ingrese acá de qué trata el problema")
        Titulo.next_to(Problema,DOWN)
        self.play(Write(Problema))
        self.play(Write(Titulo))
        self.wait(5)
        self.remove(*Problema,*Titulo)
        #Ingrese el enunciado, puede variar el tamaño de la letra si es necesario
        Enunciado = Tex("(a) En el artículo ``Evaluación de la fatiga de aspas con aplicaciones en turbinas de viento de eje vertical'' (J. Solar Energy Engr., 1982: 107–111) se hace un estudio del estrés vibratorio de un aspa de viento en un túnel de viento, a una velocidad particular. El autor propone que la v.a. $X$ que denota el estrés vibratorio, medido en librafuerza por pulgada cuadrada (psi), tiene una distribución de Rayleigh con un pdf (donde $\\theta$ es una constante positiva) dado por", font_size=24)
        #Ingrese la ecuacion del enunciado
        Enunciado_eq1 = MathTex(r"f_X(x;\theta) = \begin{cases} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} & x > 0 \\ 0 & \text{de otra forma} \end{cases}")
        Enunciado_eq1.next_to(Enunciado,DOWN)
        #Puede variar el shift dependiendo de la longitud del enunciado
        self.play(ApplyMethod(Enunciado.shift,3*UP))
        self.play(ApplyMethod(Enunciado_eq1.shift,2*UP))
        self.wait(5)
        self.remove(*Enunciado,*Enunciado_eq1)
        #Ingrese el enunciado de la primera pregunta
        Pregunta1 = Tex("I . Verifique que $f_X(x;\\theta)$ es un pdf legítimo.", font_size=30)
        self.play(ApplyMethod(Pregunta1.shift,3*UP))
        #Ingrese la introducción a la solución
        Solucion_introduccion1 = Tex("Utilizando la integral dada en las fórmulas de interés:", font_size=30)
        #Ingrese las ecuaciones para la solucion del problema
        Solucion_eq1 = MathTex(r"\int_{-\infty}^{+\infty} f_x(x) dx &= 1  \\ 1 &= \int_{0}^{+\infty} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} dx \\ &= \frac{1}{\theta^2} \left[ - \frac{1}{2/(2\theta^2)} e^{-x^2/(2\theta^2)} \right]_{0}^{+\infty} \\ &= - \left(e^{-\infty^2/(2\theta^2)} - e^{-0^2/(2\theta^2)} \right) = 0 + 1 = 1", font_size=30)
        self.play(ApplyMethod(Solucion_introduccion1.shift,2*UP))
        self.play(Write(Solucion_eq1))
