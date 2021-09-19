import turtle


def configure_turtle():
    turtle.tracer(False)
    turtle.colormode(255)
    turtle.mode('logo')  # heading north in the beginning
    turtle.screensize(6000, 6000, 'black')


def draw_line(current_stroke, number_of_strokes, digit):
    color = int(current_stroke / (number_of_strokes / 255))
    turtle.pencolor(255, 255 - color, color)
    rotation = get_rotation(digit)
    turtle.setheading(rotation)
    turtle.forward(3)
    # Refresh only occasionally to speed up things
    if current_stroke % 10_000 == 0:
        turtle.update()


def get_rotation(digit):
    rotation = digit * 36
    return rotation


def get_pi():
    with open("pi.txt") as f:
        pi = f.read()
        return pi


def main():
    configure_turtle()
    number = get_pi()
    number_of_strokes = 200_000
    for n in range(number_of_strokes):
        digit = int(number[n])
        draw_line(n, number_of_strokes, digit)
    turtle.done()


if __name__ == '__main__':
    main()
