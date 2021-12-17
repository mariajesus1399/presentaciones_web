from manim import *
from manim_presentation import Slide
class animacion(Scene):
	def construct(self):
		texto_1 = Tex("Vamos a animar una formula con ", "Manim")\
		.scale(1.3)\
		.move_to(UP*2.5)
		texto_1[1].set_color(GREEN)

		formula_1 = Tex("v", "=", "{d $\\over$ dt}(", "A", "$\\sin$ ($\\omega$ t + $\\phi$))")\
		.scale(.7)
		formula_2 = Tex("v", "=", "A", "{d $\\over$ dt}(", "$\\sin$ ($\\omega$ t + $\\phi$))")\
		.scale(.7)
		formula_3 = Tex("v", "=", "A", "$\\cos$ ($\\omega$ t + $\\phi$)", "{d $\\over$ dt}(", "($\\omega$ t + $\\phi$))")\
		.scale(.7)\
		.move_to(DOWN + RIGHT*.63)
		formula_4 = Tex("v", "=", "A", "$\\omega$", "$\\cos$ ($\\omega$ t + $\\phi$)")\
		.scale(.7)\
		.move_to(DOWN*2 + LEFT*.25)
		self.play(
			Write(texto_1)
			)
		self.wait(2)
		self.play(
			Write(formula_1)
			)
		self.wait(2)

		self.play(
			ApplyMethod(formula_1.move_to, UP)
			)

		self.wait(2)

		self.play(
			ApplyMethod(formula_1[1].copy().move_to, formula_2[1]),
			ApplyMethod(formula_1[3].copy().move_to, formula_2[2]),
			ApplyMethod(formula_1[2].copy().move_to, formula_2[3]),
			ApplyMethod(formula_1[4].copy().move_to, formula_2[4]),
			)
		self.wait(2)

		self.play(
			ApplyMethod(formula_2[1].copy().move_to, formula_3[1]),
			ApplyMethod(formula_2[2].copy().move_to, formula_3[2]),
			ApplyMethod(formula_2[3].copy().move_to, formula_3[4]),
			Transform(formula_2[4].copy(), formula_3[3]),
			Transform(formula_2[4], formula_3[5])
			)
		self.wait(2)

		self.play(
			ApplyMethod(formula_3[1].copy().move_to, formula_4[1]),
			ApplyMethod(formula_3[2].copy().move_to, formula_4[2]),
			ApplyMethod(formula_3[3].copy().move_to, formula_4[4]),
			Transform(formula_3[4], formula_4[3]),
			Transform(formula_3[5], formula_4[3]),
			)
		self.wait(5)
