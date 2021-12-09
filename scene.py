from manim import *

class Plantilla(Scene):
    def construct(self):
        #--- Primera diapositiva
        #Ingrese el número de problema
        Problema = Tex("Problema 5")
        #Ingrese sobre qué trata el problema
        Titulo = Tex("Algunas funciones de densidad de probabilidad")
        Titulo.next_to(Problema,DOWN)
        self.play(Write(Problema))
        self.play(Write(Titulo))
        #Puede variar el tiempo de espera entre cada diapostiva
        self.wait(5)
        self.remove(*Problema,*Titulo)
        #---

        #--- Segunda diapositiva
        #Ingrese el enunciado, puede variar el tamaño de la letra si es necesario en el font_size
        Enunciado = Tex("(a) En el artículo ``Evaluación de la fatiga de aspas con aplicaciones en turbinas de viento de eje vertical'' (J. Solar Energy Engr., 1982: 107–111) se hace un estudio del estrés vibratorio de un aspa de viento en un túnel de viento, a una velocidad particular. El autor propone que la v.a. $X$ que denota el estrés vibratorio, medido en librafuerza por pulgada cuadrada (psi), tiene una distribución de Rayleigh con un pdf (donde $\\theta$ es una constante positiva) dado por", font_size=24)
        #Ingrese la ecuacion del enunciado de ser necesaria
        Enunciado_eq1 = MathTex(r"f_X(x;\theta) = \begin{cases} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} & x > 0 \\ 0 & \text{de otra forma} \end{cases}")
        Enunciado_eq1.next_to(Enunciado,DOWN)
        #Puede variar el shift dependiendo de la longitud del enunciado
        self.play(ApplyMethod(Enunciado.shift,3*UP))
        self.play(ApplyMethod(Enunciado_eq1.shift,2*UP))
        #Puede variar el tiempo de espera entre cada diapostiva
        self.wait(5)
        self.remove(*Enunciado,*Enunciado_eq1)
        #---

        #--- Tercera diapositiva
        #Ingrese el enunciado de la primera pregunta
        Pregunta1 = Tex("I . Verifique que $f_X(x;\\theta)$ es un pdf legítimo.", font_size=30)
        self.play(ApplyMethod(Pregunta1.shift,3*UP))
        #Ingrese la introducción a la solución de la primera pregunta
        Solucion_introduccion1 = Tex("Utilizando la integral dada en las fórmulas de interés:", font_size=30)
        #Ingrese las ecuaciones para la solucion de la primera pregunta
        Solucion_eq1 = MathTex(r"\int_{-\infty}^{+\infty} f_x(x) dx &= 1  \\ 1 &= \int_{0}^{+\infty} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} dx \\ &= \frac{1}{\theta^2} \left[ - \frac{1}{2/(2\theta^2)} e^{-x^2/(2\theta^2)} \right]_{0}^{+\infty} \\ &= - \left(e^{-\infty^2/(2\theta^2)} - e^{-0^2/(2\theta^2)} \right) = 0 + 1 = 1", font_size=30)
        self.play(ApplyMethod(Solucion_introduccion1.shift,2*UP))
        self.play(Write(Solucion_eq1))
        #Puede variar el tiempo de espera entre cada diapostiva
        self.wait(5)
        self.remove(*Pregunta1,*Solucion_introduccion1, *Solucion_eq1)
        #---

        #Cuarta diapositiva
        #Ingrese el enunciado de la segunda pregunta
        Pregunta2 = Tex("II . Suponga que $\\theta = 100$ (valor sugerido por un gráfico del artículo). ¿Cuál es la probabilidad de que $X$ es menos de 200, al menos 200?", font_size=30)
        self.play(ApplyMethod(Pregunta2.shift,3*UP))
        #Ingrese la introducción para la solucion de la segunda pregunta parte 1
        Solucion_introduccion2_1 = Tex("Menos de 200: $P(X < 200) = \\int_{-\\infty}^{200} f_x(x) dx$", font_size=30)
        #Ingrese las ecuaciones para la solucion de la segunda pregunta parte 1
        Solucion_eq2_1 = MathTex(r"P(X < 200) 	&= \int_{0}^{200} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} dx \\ &= \frac{1}{100^2} \left[ - \frac{1}{2/(2\cdot 100^2)} e^{-x^2/(2(100)^2)} \right]_{0}^{200} \\ &= - \left(e^{-(200)^2/(2\cdot 100^2)} - e^{-(0)^2/(2\cdot 100^2)} \right) \\&= - \left(e^{-2} - e^{0}\right) = 0.864665", font_size=30)
        self.play(ApplyMethod(Solucion_introduccion2_1.shift,2*UP))
        self.play(Write(Solucion_eq2_1))
        self.wait(5)
        self.remove(*Solucion_introduccion2_1, *Solucion_eq2_1)
        #---

        #Quinta diapostiva
        #Ingrese la introducción para la solucion de la segunda pregunta parte 2
        Solucion_introduccion2_2 = Tex("Al menos 200: $P(X > 200) = \\int_{200}^{+\\infty} f_x(x) dx = 1 - P(X < 200) = 1 - 0.864665 = 0.135335$. Verificación con la integral:", font_size=30)
        #Ingrese las ecuaciones para la solucion de la segunda pregunta parte 2
        Solucion_eq2_2 = MathTex(r"P(X > 200) 	&= \int_{200}^{\infty} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} dx \\ &= \frac{1}{100^2} \left[ - \frac{1}{2/(2\cdot 100^2)} e^{-x^2/(2(100)^2)} \right]_{200}^{\infty} \\ &= - \left(e^{-(\infty)^2/(2\cdot 100^2)} - e^{-(200)^2/(2\cdot 100^2)} \right) \\ &= - \left(0 - e^{-2}\right) = 0.135335", font_size=30)
        self.play(ApplyMethod(Solucion_introduccion2_2.shift,2*UP))
        self.play(Write(Solucion_eq2_2))
        self.wait(5)
        self.remove(*Pregunta2,*Solucion_introduccion2_2, *Solucion_eq2_2)
        #---
