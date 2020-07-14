import OpenGL.GL as GL
from PyQt5.QtWidgets import QOpenGLWidget
from Type_Tet import Point


class PyQtOpenGl(QOpenGLWidget):

    def set_matrix(self, matrix):
        self.matrix = matrix
        self.update()

    def __init__(self, parrent=None):
        super().__init__(parrent)
        self.paint_0 = False

    def initializeGL(self):
        GL.glClearColor(0, 0.5, 0.5, 0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    def resizeGL(self, w, h):
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(0, 10, 0, 20, 1, -1)
        GL.glViewport(0, 0, w, h)

    def paintGL(self):

        def _create_quard(p, x_1, y_1):
            x = x_1
            y = y_1
            GL.glColor3f(p.red, p.green, p.blue)
            GL.glRectf(x+.0, y+.0, x+1.0, y+1.0)
            GL.glColor3f(p.red+0.3, p.green+0.3, p.blue+0.3)
            GL.glRectf(x+.15, y+.15, x+0.85, y+0.85)
            GL.glColor3f(p.red+0.5, p.green+0.5, p.blue+0.5)
            GL.glBegin(GL.GL_POLYGON)
            GL.glVertex2f(x+0.0, y+1.0)
            GL.glVertex2f(x+1.0, y+1.0)
            GL.glVertex2f(x+0.85, y+0.85)
            GL.glVertex2f(x+0.15, y+0.85)
            GL.glEnd()
            GL.glColor3f(p.red-0.3, p.green-0.3, p.blue-0.3)
            GL.glBegin(GL.GL_POLYGON)
            GL.glVertex2f(x+0.0, y+0.0)
            GL.glVertex2f(x+1.0, y+0.0)
            GL.glVertex2f(x+0.85, y+0.15)
            GL.glVertex2f(x+0.15, y+0.15)
            GL.glEnd()

        if self.paint_0:
            for line in self.matrix:
                for p in line:
                    if type(p) == Point:
                        _create_quard(p, p.x, p.y)
