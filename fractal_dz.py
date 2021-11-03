import turtle as tl

def draw_fractal(scale):
    if scale >= 5:
        draw_fractal(scale / 2)
        tl.left(60)
        draw_fractal(scale / 2)
        tl.right(110)
        draw_fractal(scale / 2)
        tl.left(60)
        draw_fractal(scale / 2)
    else:
        tl.forward(scale)

tl.speed(100)
tl.color('green')
scale = 100
tl.pensize(2)
tl.penup()
tl.goto(0, -scale / 2)
tl.pendown()

draw_fractal(scale)
tl.done()
