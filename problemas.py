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
		formula_1 = Tex("$E[Y]$", "$=$", "$\\int_{-\\infty}^{+\\infty}$", "$f_Y(y)$", "$dy$")\
		.scale(.7)
		self.play(
			Write(formula_1)
			)
		self.wait(2)
		self.play(
			ApplyMethod(formula_1.move_to, UP)
			)
		formula_2 = Tex("$=$", "$\int_{-\infty}^{+\infty}$", "[", "$0.1 \\delta(y - 690)$", "+","$0.3 \\delta(y - 680)$", "+", "$0.25 \\delta(y - 670)$", "+", "$0.2 \\delta(y - 660)$", "+", "$0.1 \\delta(y - 650)$", "+", "$0.05 \\delta(y - 640)$", "]", "dy")\
		.scale(.7)
		self.play(
			Write(formula_2)
			)
		self.wait(2)
		formula_3 = Tex("$=$", "$0.1 \\cdot 690$", "+", "$0.3 \\cdot 680$", "+", "$0.25 \\cdot  670$", "+", "$0.2 \\cdot 660$", "+", "$0.1 \\cdot 650$", "+", "$0.05 \\cdot 640$")\
		.scale(.7)\
		.move_to(DOWN)
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
