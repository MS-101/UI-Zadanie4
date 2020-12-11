import tkinter
import math
import random
import time


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.distance = 0


points_init = [Point(-4500, -4400, "red"), Point(-4100, -3000, "red"), Point(-1800, -2400, "red"),
               Point(-2500, -3400, "red"), Point(-2000, -1400, "red"),
               Point(4500, -4400, "green"), Point(4100, -3000, "green"), Point(1800, -2400, "green"),
               Point(2500, -3400, "green"), Point(2000, -1400, "green"),
               Point(-4500, 4400, "blue"), Point(-4100, 3000, "blue"), Point(-1800, 2400, "blue"),
               Point(-2500, 3400, "blue"), Point(-2000, 1400, "blue"),
               Point(4500, 4400, "purple"), Point(4100, 3000, "purple"), Point(1800, 2400, "purple"),
               Point(2500, 3400, "purple"), Point(2000, 1400, "purple")]


def init_points():
    # remove points from array
    for point in points:
        remove_point(point)

    # create initial points
    points.clear()
    for point in points_init:
        points.append(point)

    # add points to array
    for point in points:
        add_point(point)


def add_point(point):
    pointArray[-point.y + 5000][point.x + 5000] = point.color


def remove_point(point):
    pointArray[-point.y + 5000][point.x + 5000] = ""


def update_canvas():
    pointCanvas.delete("all")

    for y in range(len(pointArray)):
        for x in range(len(pointArray[y])):
            if pointArray[y][x] != "":
                pointCanvas.create_oval(round(x / 20) - 5, round(y / 20) - 5,
                                        round(x/20) + 5, round(y/20) + 5, fill=pointArray[y][x])

    pointCanvas.create_line(0, 250, 500, 250)
    pointCanvas.create_line(250, 0, 250, 500)


def reset():
    init_points()
    update_canvas()


def experiment1():
    start_time = time.time()

    if len(points) > 20:
        init_points()
    generate_points(1)
    update_canvas()

    print("Experiment 1 trval " + str(time.time() - start_time) + " sekúnd.")


def experiment2():
    start_time = time.time()

    if len(points) > 20:
        init_points()
    generate_points(3)
    update_canvas()

    print("Experiment 2 trval " + str(time.time() - start_time) + " sekúnd.")


def experiment3():
    start_time = time.time()

    if len(points) > 20:
        init_points()
    generate_points(7)
    update_canvas()

    print("Experiment 3 trval " + str(time.time() - start_time) + " sekúnd.")


def experiment4():
    start_time = time.time()

    if len(points) > 20:
        init_points()
    generate_points(15)
    update_canvas()

    print("Experiment 4 trval " + str(time.time() - start_time) + " sekúnd.")


def generate_points(k):
    cur_color = "red"

    correct_counter = 0
    point_class_count = 5000

    for i in range(point_class_count):
        for j in range(4):
            if cur_color == "red":
                while True:
                    x = random.randint(-5000, 500 - 1)
                    y = random.randint(-5000 + 1, 500 - 1)

                    if pointArray[-y + 5000][x + 5000] == "":
                        break

                classified_color = classify(x, y, k)
                if cur_color == classified_color:
                    correct_counter += 1

                cur_color = "green"
            elif cur_color == "green":
                while True:
                    x = random.randint(-5000, 5000 - 1)
                    y = random.randint(-5000 + 1, 500 - 1)

                    if pointArray[-y + 5000][x + 5000] == "":
                        break

                classified_color = classify(x, y, k)
                if cur_color == classified_color:
                    correct_counter += 1

                cur_color = "blue"
            elif cur_color == "blue":
                while True:
                    x = random.randint(-5000, 500 - 1)
                    y = random.randint(-500 + 1, 5000)

                    if pointArray[-y + 5000][x + 5000] == "":
                        break

                classified_color = classify(x, y, k)
                if cur_color == classified_color:
                    correct_counter += 1

                cur_color = "purple"
            else:
                while True:
                    x = random.randint(-500 + 1, 5000 - 1)
                    y = random.randint(-500 + 1, 5000)

                    if pointArray[-y + 5000][x + 5000] == "":
                        break

                classified_color = classify(x, y, k)
                if cur_color == classified_color:
                    correct_counter += 1

                cur_color = "red"

            # add new point
            new_point = Point(x, y, classified_color)
            points.append(new_point)
            add_point(new_point)

    success_rate = round(correct_counter / (point_class_count * 4) * 100, 2)
    print("Úspešnosť klasifikátora pre experiment s k=" + str(k) + ": " + str(success_rate) + "%")


def classify(x, y, k):
    # calculate distances of all points from this new point
    for point in points:
        point.distance = math.sqrt((point.x - x)**2 + (point.y - y)**2)

    # sort all points by distance
    sorted_points = sorted(points, key=lambda obj: obj.distance)

    # get k neighbours
    neighbours = []
    for i in range(k):
        neighbours.append(sorted_points[i])

    # initialize color counters
    red_counter = 0
    blue_counter = 0
    green_counter = 0
    purple_counter = 0

    max_counter = 0
    max_colors = []

    # calculate prevailing neighbour color
    for neighbour in neighbours:
        if neighbour.color == "red":
            red_counter += 1

            if max_counter < red_counter:
                max_counter = red_counter
                max_colors.clear()
                max_colors.append("red")
            elif max_counter == red_counter:
                max_colors.append("red")
        elif neighbour.color == "blue":
            blue_counter += 1

            if max_counter < blue_counter:
                max_counter = blue_counter
                max_colors.clear()
                max_colors.append("blue")
            elif max_counter == blue_counter:
                max_colors.append("blue")
        elif neighbour.color == "green":
            green_counter += 1

            if max_counter < green_counter:
                max_counter = green_counter
                max_colors.clear()
                max_colors.append("green")
            elif max_counter == green_counter:
                max_colors.append("green")
        elif neighbour.color == "purple":
            purple_counter += 1

            if max_counter < purple_counter:
                max_counter = purple_counter
                max_colors.clear()
                max_colors.append("purple")
            elif max_counter == purple_counter:
                max_colors.append("purple")

    # get random color from prevailing colors
    random_index = random.randrange(len(max_colors))
    color = max_colors[random_index]

    return color


root = tkinter.Tk()

root.geometry("550x550")
root.resizable(False, False)
root.title("Svab_UI_Zadanie4")

pointCanvas = tkinter.Canvas(root, bg="white", width=500, height=500)
pointCanvas.pack()

buttonFrame = tkinter.Frame(root)
buttonFrame.pack(fill="x", padx=10, pady=5)

resetBtn = tkinter.Button(buttonFrame, text="Reset", command=reset)
resetBtn.grid(row=0, column=0, padx=10, pady=5)
experiment1Btn = tkinter.Button(buttonFrame, text="Experiment 1", command=experiment1)
experiment1Btn.grid(row=0, column=1, padx=10, pady=5)
experiment2Btn = tkinter.Button(buttonFrame, text="Experiment 2", command=experiment2)
experiment2Btn.grid(row=0, column=2, padx=10, pady=5)
experiment3Btn = tkinter.Button(buttonFrame, text="Experiment 3", command=experiment3)
experiment3Btn.grid(row=0, column=3, padx=10, pady=5)
experiment4Btn = tkinter.Button(buttonFrame, text="Experiment 4", command=experiment4)
experiment4Btn.grid(row=0, column=4, padx=10, pady=5)

pointArray = []
for i in range(10000):
    pointArray.append([])

    for j in range(10000):
        pointArray[i].append("")

points = []

reset()

root.mainloop()
