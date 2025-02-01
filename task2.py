"""task2.py"""
import turtle

# Функція для малювання гілки
def draw_tree(branch_length, angle, level):
    if level > 0:
        turtle.forward(branch_length)

        turtle.right(angle)
        draw_tree(branch_length * 0.7, angle, level - 1)
        turtle.left(2 * angle)
        draw_tree(branch_length * 0.7, angle, level - 1)

        turtle.right(angle)
        turtle.backward(branch_length)

# Основна функція
def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -screen.window_height() // 2 + 50)
    turtle.pendown()
    turtle.speed(0)

    draw_tree(200, 47.5, level)

    turtle.done()

if __name__ == "__main__":
    main()
