
from random import randint, seed


class Point():
    def __init__(self, r, g, b, x, y):
        self.red = r
        self.green = g
        self.blue = b
        self.x = x
        self.y = y

    def swapcolor(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b


class Figure():
    points = [None]*4

    def rotate_fig(self, matrix, coord):
        for c in coord:
            if c[0] < 0 or c[0] > 9 or c[1] < 0 or c[1] > 23:
                return False
            if (matrix[c[1]][c[0]] is not None
                    and matrix[c[1]][c[0]] not in self.points):
                return False
        for i in range(len(self.points)):
            matrix[self.points[i].y][self.points[i].x] = None
            self.points[i].x = coord[i][0]
            self.points[i].y = coord[i][1]
        for p in reversed(self.points):
            matrix[p.y][p.x] = p
        return True

    def fig_down(self, matrix):
        for p in reversed(self.points):
            if p.y == 0:
                return False
            if (matrix[p.y-1][p.x] not in self.points
                    and matrix[p.y-1][p.x] is not None):
                return False
        for i in range(len(self.points)):
            matrix[self.points[i].y][self.points[i].x] = None
            self.points[i].y -= 1
        for p in reversed(self.points):
            matrix[p.y][p.x] = p
        return True

    def fig_up(self, matrix):
        for p in reversed(self.points):
            if (matrix[p.y+1][p.x] not in self.points
                    and matrix[p.y+1][p.x] is not None):
                return False
        for i in range(len(self.points)):
            matrix[self.points[i].y][self.points[i].x] = None
            self.points[i].y += 1
        for p in reversed(self.points):
            matrix[p.y][p.x] = p
        return True

    def fig_swing(self, matrix, direction):
        d = 0
        if (direction.lower() == "left"):
            d = -1
        elif (direction.lower() == "right"):
            d = 1
        else:
            raise TypeError("invalid value. It takes the"
                            + "meaning of 'left' or 'right'")
        for p in self.points:
            if (p.x+d < 0 or p.x+d > 9):
                return False
            if (matrix[p.y][p.x + d]not in self.points
                    and matrix[p.y][p.x + d] is not None):
                return False
        for i in range(len(self.points)):
            matrix[self.points[i].y][self.points[i].x] = None
            self.points[i].x += d
        for p in reversed(self.points):
            matrix[p.y][p.x] = p
        return True


class Fig_T(Figure):
    r = 0.5
    g = 0.0
    b = 0.5

    def __init__(self, matrix):
        self.rot = 'up'
        self.points[0] = Point(self.r, self.g, self.b, 4, 21)
        self.points[1] = Point(self.r, self.g, self.b, 3, 20)
        self.points[2] = Point(self.r, self.g, self.b, 4, 20)
        self.points[3] = Point(self.r, self.g, self.b, 5, 20)
        for p in reversed(self.points):
            matrix[p.y][p.x] = p

    def rotate_fig(self, matrix):
        cent = self.points[2]
        name_rot = {
                    'up': 'left', 'left': 'down', 'down': 'right',
                    'right': 'up'
                    }

        if self.rot == 'up':
            coord = [
                     [cent.x,   cent.y],
                     [cent.x+1, cent.y-1],
                     [cent.x+1, cent.y],
                     [cent.x+1, cent.y+1]
                     ]
        if self.rot == 'left':
            coord = [
                     [cent.x,   cent.y],
                     [cent.x-1, cent.y+1],
                     [cent.x, cent.y+1],
                     [cent.x+1, cent.y+1]
                     ]
        if self.rot == 'down':
            coord = [
                     [cent.x,   cent.y],
                     [cent.x-1, cent.y-1],
                     [cent.x-1, cent.y],
                     [cent.x-1, cent.y+1]
                     ]
        if self.rot == 'right':
            coord = [
                     [cent.x,   cent.y],
                     [cent.x-1, cent.y-1],
                     [cent.x, cent.y-1],
                     [cent.x+1, cent.y-1]
                     ]
        if super().rotate_fig(matrix, coord):
            self.rot = name_rot[self.rot]
            return True
        return False


class Fig_O(Figure):
    r = 0.3
    g = 0.5
    b = 0.3

    def __init__(self, matrix):
        self.points[0] = Point(self.r, self.g, self.b, 4, 21)
        self.points[1] = Point(self.r, self.g, self.b, 5, 21)
        self.points[2] = Point(self.r, self.g, self.b, 4, 20)
        self.points[3] = Point(self.r, self.g, self.b, 5, 20)
        for p in reversed(self.points):
            matrix[p.y][p.x] = p

    def rotate_fig(self, matrix):
        return True


class Fig_L(Figure):
    r = 0.0
    g = 0.0
    b = 0.5

    def __init__(self, matrix):
        self.rot = 'up'
        self.points[0] = Point(self.r, self.g, self.b, 5, 20)
        self.points[1] = Point(self.r, self.g, self.b, 4, 22)
        self.points[2] = Point(self.r, self.g, self.b, 4, 21)
        self.points[3] = Point(self.r, self.g, self.b, 4, 20)
        for p in reversed(self.points):
            matrix[p.y][p.x] = p

    def rotate_fig(self, matrix):
        cent = self.points[2]
        name_rot = {
                    'up': 'left', 'left': 'down', 'down': 'right',
                    'right': 'up'
                    }

        if self.rot == 'up':
            coord = [
                     [cent.x+1,   cent.y+1],
                     [cent.x-1, cent.y],
                     [cent.x, cent.y],
                     [cent.x+1, cent.y]
                     ]
        if self.rot == 'left':
            coord = [
                     [cent.x-1,   cent.y+1],
                     [cent.x, cent.y-1],
                     [cent.x, cent.y],
                     [cent.x, cent.y+1]
                     ]
        if self.rot == 'down':
            coord = [
                     [cent.x-1,   cent.y-1],
                     [cent.x-1, cent.y],
                     [cent.x, cent.y],
                     [cent.x+1, cent.y]
                     ]
        if self.rot == 'right':
            coord = [
                     [cent.x+1,   cent.y-1],
                     [cent.x, cent.y+1],
                     [cent.x, cent.y],
                     [cent.x, cent.y-1]
                     ]
        if super().rotate_fig(matrix, coord):
            self.rot = name_rot[self.rot]
            return True
        return False


class Fig_J(Figure):
    r = 0.5
    g = 0.5
    b = 0.0

    def __init__(self, matrix):
        self.rot = 'up'
        self.points[0] = Point(self.r, self.g, self.b, 3, 20)
        self.points[1] = Point(self.r, self.g, self.b, 4, 22)
        self.points[2] = Point(self.r, self.g, self.b, 4, 21)
        self.points[3] = Point(self.r, self.g, self.b, 4, 20)
        for p in reversed(self.points):
            matrix[p.y][p.x] = p

    def rotate_fig(self, matrix):
        cent = self.points[2]
        name_rot = {
                    'up': 'left', 'left': 'down', 'down': 'right',
                    'right': 'up'
                    }

        if self.rot == 'up':
            coord = [
                     [cent.x+1,   cent.y-1],
                     [cent.x-1, cent.y],
                     [cent.x, cent.y],
                     [cent.x+1, cent.y]
                     ]
        if self.rot == 'left':
            coord = [
                     [cent.x+1,   cent.y+1],
                     [cent.x, cent.y-1],
                     [cent.x, cent.y],
                     [cent.x, cent.y+1]
                     ]
        if self.rot == 'down':
            coord = [
                     [cent.x-1,   cent.y+1],
                     [cent.x-1, cent.y],
                     [cent.x, cent.y],
                     [cent.x+1, cent.y]
                     ]
        if self.rot == 'right':
            coord = [
                     [cent.x-1,   cent.y-1],
                     [cent.x, cent.y+1],
                     [cent.x, cent.y],
                     [cent.x, cent.y-1]
                     ]
        if super().rotate_fig(matrix, coord):
            self.rot = name_rot[self.rot]
            return True
        return False


class Fig_I(Figure):
    r = 0.7
    g = 0.7
    b = 0.7

    def __init__(self, matrix):
        self.rot = 'vert'
        self.points[0] = Point(self.r, self.g, self.b, 4, 23)
        self.points[1] = Point(self.r, self.g, self.b, 4, 22)
        self.points[2] = Point(self.r, self.g, self.b, 4, 21)
        self.points[3] = Point(self.r, self.g, self.b, 4, 20)
        for p in reversed(self.points):
            matrix[p.y][p.x] = p

    def rotate_fig(self, matrix):
        cent = self.points[2]
        name_rot = {
                    'vert': 'horiz', 'horiz': 'vert'
                    }

        if self.rot == 'vert':
            coord = [
                     [cent.x,   cent.y+2],
                     [cent.x, cent.y+1],
                     [cent.x, cent.y],
                     [cent.x, cent.y-1]
                     ]
        if self.rot == 'horiz':
            coord = [
                     [cent.x+2,   cent.y],
                     [cent.x+1, cent.y],
                     [cent.x, cent.y],
                     [cent.x-1, cent.y]
                     ]

        if super().rotate_fig(matrix, coord):
            self.rot = name_rot[self.rot]
            return True
        return False


class Fig_Z(Figure):
    r = 0.3
    g = 0.1
    b = 0.5

    def __init__(self, matrix):
        self.rot = 'vert'
        self.points[0] = Point(self.r, self.g, self.b, 3, 21)
        self.points[1] = Point(self.r, self.g, self.b, 4, 21)
        self.points[2] = Point(self.r, self.g, self.b, 4, 20)
        self.points[3] = Point(self.r, self.g, self.b, 5, 20)
        for p in reversed(self.points):
            matrix[p.y][p.x] = p

    def rotate_fig(self, matrix):
        cent = self.points[1]
        name_rot = {
                    'vert': 'horiz', 'horiz': 'vert'
                    }

        if self.rot == 'vert':
            coord = [
                     [cent.x,   cent.y-1],
                     [cent.x, cent.y],
                     [cent.x+1, cent.y],
                     [cent.x+1, cent.y+1]
                     ]
        if self.rot == 'horiz':
            coord = [
                     [cent.x-1,   cent.y],
                     [cent.x, cent.y],
                     [cent.x, cent.y-1],
                     [cent.x+1, cent.y-1]
                     ]

        if super().rotate_fig(matrix, coord):
            self.rot = name_rot[self.rot]
            return True
        return False


class Fig_S(Figure):
    r = 0.5
    g = 0.1
    b = 0.3

    def __init__(self, matrix):
        self.rot = 'vert'
        self.points[0] = Point(self.r, self.g, self.b, 3, 19)
        self.points[1] = Point(self.r, self.g, self.b, 4, 19)
        self.points[2] = Point(self.r, self.g, self.b, 4, 20)
        self.points[3] = Point(self.r, self.g, self.b, 5, 20)
        for p in reversed(self.points):
            matrix[p.y][p.x] = p

    def rotate_fig(self, matrix):
        cent = self.points[2]
        name_rot = {
                    'vert': 'horiz', 'horiz': 'vert'
                    }

        if self.rot == 'vert':
            coord = [
                     [cent.x+1,   cent.y-1],
                     [cent.x+1, cent.y],
                     [cent.x, cent.y],
                     [cent.x, cent.y+1]
                     ]
        if self.rot == 'horiz':
            coord = [
                     [cent.x-1,   cent.y-1],
                     [cent.x, cent.y-1],
                     [cent.x, cent.y],
                     [cent.x+1, cent.y]
                     ]

        if super().rotate_fig(matrix, coord):
            self.rot = name_rot[self.rot]
            return True
        return False


class Pole():
    def __init__(self, key_gen):
        self.key_gen = key_gen
        seed(key_gen)
        self.radn = randint(1, 2)
        self.matrix = []
        for i in range(24):
            self.matrix.append([None]*10)
        self.score = 0
        self.speed = 1.0
        self.lvl = 0
        self.lines = 0
        self.fig = None
        self.next_lines = 5

    def remove_lines(self):
        t_lines = 0
        indexs = []
        for i in range(len(self.matrix)):
            if None not in self.matrix[i]:
                indexs.append(i)
                t_lines += 1
        for i in range(t_lines):
            del self.matrix[indexs[i]-i]
            self.matrix.append([None]*10)
        if t_lines == 4:
            self.score += t_lines*250
        else:
            self.score += t_lines*100
        self.lines += t_lines
        if self.lines > self.next_lines:
            self.next_lines += 10
            self.speed *= 0.95
            return True
        else:
            return False

    def next(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] is not None:
                    self.matrix[i][j].x = j
                    self.matrix[i][j].y = i
        key = randint(1, 7)
        if (key == 1):
            self.fig = Fig_T(self.matrix)
        elif(key == 2):
            self.fig = Fig_I(self.matrix)
        elif(key == 3):
            self.fig = Fig_L(self.matrix)
        elif(key == 4):
            self.fig = Fig_J(self.matrix)
        elif(key == 5):
            self.fig = Fig_O(self.matrix)
        elif(key == 6):
            self.fig = Fig_Z(self.matrix)
        elif(key == 7):
            self.fig = Fig_S(self.matrix)
