from manim import *
from manim_presentation import Slide
class problema3(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		formula_1 = Tex("Z", "=", "$\\frac{R - \\mu}{\\sigma}$")\
		.scale(.7)
		self.play(
			Write(formula_1)
			)
		self.wait(2)
		self.play(
			ApplyMethod(formula_1.move_to, UP)
			)

class problema3_b_3(Scene):
	def construct(self):
		self.camera.background_color = WHITE
		#Definicion de formulas del problema
		formula_1 = Tex("$E[Y]$", "$=$", "$\\int_{-\\infty}^{+\\infty}$", "$f_Y(y)$", "$dy$")\
		.scale(.7)
		formula_2 = Tex("$=$", "$\int_{-\infty}^{+\infty}$", "[", "$0.1 \\delta(y - 690)$", "+","$0.3 \\delta(y - 680)$", "+", "$0.25 \\delta(y - 670)$", "+", "$0.2 \\delta(y - 660)$", "+", "$0.1 \\delta(y - 650)$", "+", "$0.05 \\delta(y - 640)$", "]", "dy")\
		.scale(.7)
		formula_3 = Tex("$=$", "$0.1 \\cdot 690$", "+", "$0.3 \\cdot 680$", "+", "$0.25 \\cdot  670$", "+", "$0.2 \\cdot 660$", "+", "$0.1 \\cdot 650$", "+", "$0.05 \\cdot 640$")\
		.scale(.7)\
		.move_to(DOWN)
		formula_4 = Tex("=", "669.5")\
		.scale(.7)\
		.move_to(DOWN*2 + LEFT*.25)
		formula_4.bg=SurroundingRectangle(formula_4,color=BLUE)
		formula_4_group=VGroup(formula_4,formula_4.bg)
		#Animaciones de ecuaciones
		self.play(
			Write(formula_1) #Animacion para escribir una formula
			)
		self.wait(2)
		self.play(
			ApplyMethod(formula_1.move_to, UP) #Animacion para mover una formula hacia arriba
			)
		#Animacion para transformar una ecuacion
		self.play(
			ApplyMethod(formula_1[1].copy().move_to, formula_2[0]),
			ApplyMethod(formula_1[2].copy().move_to, formula_2[1]),
			Transform(formula_1[3].copy(), formula_2[2]),
			Transform(formula_1[3].copy(), formula_2[3]),
			Transform(formula_1[3].copy(), formula_2[4]),
			Transform(formula_1[3].copy(), formula_2[5]),
			Transform(formula_1[3].copy(), formula_2[6]),
			Transform(formula_1[3].copy(), formula_2[7]),
			Transform(formula_1[3].copy(), formula_2[8]),
			Transform(formula_1[3].copy(), formula_2[9]),
			Transform(formula_1[3].copy(), formula_2[10]),
			Transform(formula_1[3].copy(), formula_2[11]),
			Transform(formula_1[3].copy(), formula_2[12]),
			Transform(formula_1[3].copy(), formula_2[13]),
			Transform(formula_1[3].copy(), formula_2[14]),
			ApplyMethod(formula_1[4].copy().move_to, formula_2[15]),
			)
		self.wait(2)
		#Animacion para transformar una ecuacion
		self.play(
			ApplyMethod(formula_2[0].copy().move_to, formula_3[0]),
			Transform(formula_2[3].copy(), formula_3[1]),
			ApplyMethod(formula_2[4].copy().move_to, formula_3[2]),
			Transform(formula_2[5].copy(), formula_3[3]),
			ApplyMethod(formula_2[6].copy().move_to, formula_3[4]),
			Transform(formula_2[7].copy(), formula_3[5]),
			ApplyMethod(formula_2[8].copy().move_to, formula_3[6]),
			Transform(formula_2[9].copy(), formula_3[7]),
			ApplyMethod(formula_2[10].copy().move_to, formula_3[8]),
			Transform(formula_2[11].copy(), formula_3[9]),
			ApplyMethod(formula_2[12].copy().move_to, formula_3[10]),
			Transform(formula_2[13].copy(), formula_3[11])
			)
		self.wait(2)
		self.play(
			Transform(formula_3.copy(), formula_4_group)
			)
