from manim import *

class P5EA(Scene):
    def construct(self):
        Problema = Tex("Problema 5")
        Titulo = Tex("Algunas funciones de densidad de probabilidad")
        Ejercicio = Tex("Ejercicio A")
        Enunciado = Tex("En el artículo ``Evaluación de la fatiga de aspas con aplicaciones en turbinas de viento de eje vertical'' (J. Solar Energy Engr., 1982: 107–111) se hace un estudio del estrés vibratorio de un aspa de viento en un túnel de viento, a una velocidad particular. El autor propone que la v.a. $X$ que denota el estrés vibratorio, medido en librafuerza por pulgada cuadrada (psi), tiene una distribución de Rayleigh con un pdf (donde $\\theta$ es una constante positiva) dado por", font_size=24)
        Enunciado_eq1 = MathTex(r"f_X(x;\theta) = \begin{cases} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} & x > 0 \\ 0 & \text{de otra forma} \end{cases}")
        Enunciado_eq1.set_color_by_tex_to_color_map({
                "o": "#00c0f3",
        })
        Titulo.next_to(Problema,DOWN)
        self.play(Write(Problema))
        self.play(Write(Titulo))
        #self.add(Problema, Titulo)
        self.wait(2)
        Titulo.shift(5*UP)
        Problema.shift(5*UP)
        self.play(ApplyMethod(Ejercicio.shift,3*UP))
        self.play(ApplyMethod(Enunciado.shift,1*UP))
        self.play(ApplyMethod(Enunciado_eq1.shift,1*DOWN))
        Pregunta1 = Tex("Verifique que $f_X(x;\\theta)$ es un pdf legítimo.")
        Ejercicio.shift(5*UP)
        Enunciado.shift(5*UP)
        Enunciado_eq1.shift(6*UP)
        self.play(ApplyMethod(Pregunta1.shift,4*UP))
        Solucion = Tex("Utilizando la integral dada en las fórmulas de interés:")
        #Solucion_eq1 = MathTex(r"\int_{-\infty}^{+\infty} f_x(x) \di{x} &= 1 ")
        eq1 = MathTex(r"\int_{-\infty}^{+\infty} f_x(x) dx &= 1  \\ 1 &= \int_{0}^{+\infty} \frac{x}{\theta^2} e^{-x^2/(2\theta^2)} dx \\ &= \frac{1}{\theta^2} \left[ - \frac{1}{2/(2\theta^2)} e^{-x^2/(2\theta^2)} \right]_{0}^{+\infty} \\ &= - \left(e^{-\infty^2/(2\theta^2)} - e^{-0^2/(2\theta^2)} \right) = 0 + 1 = 1")
        self.play(ApplyMethod(Solucion.shift,3*UP))
        self.play(ApplyMethod(eq1.shift,1*UP))
