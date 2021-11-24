from manim import *
class AddingText(Scene):
#Adding text on the screen
    def construct(self):
        my_first_text=Tex("Writing with manim is fun")
        second_line=Tex("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=Tex("for me and you!")
        third_line.next_to(my_first_text,DOWN)
        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

#A short script showing how to use Latex commands
class BasicEquations(Scene):
#A short script showing how to use Latex commands
    def construct(self):
        eq1=Tex("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=Tex("$\\vec{F}_{net} = \\sum_i \\vec{F}_i$")
        eq2.shift(2*DOWN)
        self.play(Write(eq1))
        self.play(Write(eq2))

class ColoringEquations(Scene):
#Grouping and coloring parts of equations
    def construct(self):
        line1=Tex("\\text{The vector }", "$\\vec{F}_{net}$", "\\text{ is the net force on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=Tex("m", "\\text{ and acceleration }", "$\\vec{a}$", ". ")
        line2.set_color_by_tex_to_color_map({
        "m": YELLOW,
        "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))
