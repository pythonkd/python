import queue, tkinter, random, time, threading


class Food(object):

    def __init__(self, q):
        self.queue = q
        self.new_food()

    def new_food(self):
        x = random.randrange(55, 485, 10)
        y = random.randrange(55, 285, 10)
        self.position = x, y
        self.queue.put({"food": self.position})


class Snake(threading.Thread):

    def __init__(self, world, q):
        threading.Thread.__init__(self)
        self.world = world
        self.queue = q
        self.points_earned = 0
        self.food = Food(self.queue)
        self.direction = "Left"
        self.snake_points = [(495, 55), (485, 55), (475, 55), (465, 55), (455, 55)]
        self.start()

    def run(self):

        if self.world.is_game_over:
            self._delete()
        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.1)
            self.move()

    def move(self):
        new_snake_points = self.cal_new_pos()
        if self.food.position == new_snake_points:
            self.points_earned += 1
            self.queue.put({"points_earned": self.points_earned})
            self.food.new_food()
        else:
            self.snake_points.pop(0)
            self.check_game_over(new_snake_points)
        self.snake_points.append(new_snake_points)

    def cal_new_pos(self):
        last_x, last_y = self.snake_points[-1]
        if self.direction == "Up":
            new_snake_point = last_x, last_y - 10
        elif self.direction == "Left":
            new_snake_point = last_x - 10, last_y
        elif self.direction == "Down":
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Right":
            new_snake_point = last_x + 10, last_y
        return new_snake_point

    def check_game_over(self, snake_point):
        x, y = snake_point
        if x >= 505 or x <= -5 or y <= -5 or y >= 305 or (snake_point in self.snake_points):
            self.queue.put({"game_over": True})


class World():

    def __init__(self, q):
        self.queue = q
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=500, height=300, bg="white")
        self.canvas.pack()
        self.is_game_over = False
        self.Snake = Snake(self, self.queue)
        self.canvas.bind_all("<KeyPress-Up>", self.key_pressed)
        self.canvas.bind_all("<KeyPress-Down>", self.key_pressed)
        self.canvas.bind_all("<KeyPress-Left>", self.key_pressed)
        self.canvas.bind_all("<KeyPress-Right>", self.key_pressed)

        self.snake = self.canvas.create_line(0, 0, 0, 0, fill="black", width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill="#FFCC4C", outline='#FFCC4C')
        self.points_earned = self.canvas.create_text(450, 20, fill="white", text='SCORE: 0')
        self.queue_handler()
        self.root.mainloop()

    def key_pressed(self, e):

        self.Snake.direction = e.keysym

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()
                elif task.get("move"):
                    points = [x for point in task['move'] for x in point]
                    self.canvas.coords(self.snake, *points)
                elif task.get("food"):
                    x, y = task.get("food")
                    points = [x - 5, y - 5, x + 5, y + 5]
                    self.canvas.coords(self.food, *points)
                elif task.get("points_earned"):
                    points = task['points_earned']
                    self.canvas.itemconfig(self.points_earned, text="SCORE: {}".format(points))
        except queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(250, 120, fill="green", text="Game Over")
        qb = tkinter.Button(self.root, bg="green", text="Quit", command=self.root.destroy)
        qb.pack()
        rb = tkinter.Button(self.root, bg="green", text="Again", command=start)
        rb.pack()


def start():
    q = queue.Queue()
    world = World(q)
    world.root.mainloop()


if __name__ == "__main__":
    start()
