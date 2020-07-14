from PyQt5 import QtWidgets
from MainMenu import Ui_MainWindow  # импорт нашего сгенерированного файла
from PyQtOpenGlFrame import PyQtOpenGl
from PyQt5.QtCore import Qt
import sys
import Info_dialog
from time import time
from Type_Tet import Pole


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pol = Pole(1)
        self.ui.lineEdit.setInputMask('9'*29)
        self.ui.pushButton.clicked.connect(self.on_click)
        self.ui.lineEdit.textChanged.connect(self.onChanged)
        self.ui.menuAbout.triggered.connect(self.showInfo)
        self._game_init = False
        self.key_changed = False
        self.key = 0

    def showInfo(self):
        info = Info_dialog.Ui_Dialog()
        info.show()

    def onChanged(self, text):
        if not self._game_init:
            self.key_changed = True
            self.key = int(text)

    def keyPressEvent(self, a0):
        if self._game_init:
            if a0.key() == Qt.Key_W:
                if not self.pol.fig.rotate_fig(self.pol.matrix):
                    if (self.pol.fig.fig_swing(self.pol.matrix, 'left')
                            or self.pol.fig.fig_swing(self.pol.matrix, 'right')
                            or self.pol.fig.fig_up(self.pol.matrix)):
                        self.pol.fig.rotate_fig(self.pol.matrix)
                open_gl.set_matrix(self.pol.matrix)
            if a0.key() == Qt.Key_A:
                self.pol.fig.fig_swing(self.pol.matrix, 'left')
                open_gl.set_matrix(self.pol.matrix)
            if a0.key() == Qt.Key_D:
                self.pol.fig.fig_swing(self.pol.matrix, 'right')
                open_gl.set_matrix(self.pol.matrix)
            if a0.key() == Qt.Key_S:
                self.pushFig_down()
                open_gl.set_matrix(self.pol.matrix)

    def on_click(self):
        if not self._game_init:
            open_gl.paint_0 = True
            #if not self.key_changed:
            self.key = int(time())
            self.ui.lineEdit.setText(str(self.key))
            self.pol = Pole(self.key)
            self.pol.next()
            open_gl.set_matrix(application.pol.matrix)
            self._game_init = True
            self.timer_id = self.startTimer(1000, timerType=Qt.PreciseTimer)

    def pushFig_down(self):
        if not self.pol.fig.fig_down(self.pol.matrix):
            for p in self.pol.fig.points:
                if p.y > 19:
                    self._game_init = False
                    self.killTimer(self.timer_id)
            if self.pol.remove_lines():
                self.killTimer(self.timer_id)
                self.timer_id = self.startTimer(int(1000*self.pol.speed),
                                                timerType=Qt.PreciseTimer)
            self.pol.next()
        open_gl.set_matrix(self.pol.matrix)
        application.ui.textBrowser.setText(str(self.pol.score))
        application.ui.textBrowser_2.setText(str(self.pol.lines))

    def timerEvent(self, a0):
        self.pushFig_down()


app = QtWidgets.QApplication([])
application = mywindow()
open_gl = PyQtOpenGl(parrent=application.ui.openGLWidget)
open_gl.setMinimumSize(401, 801)

application.show()
sys.exit(app.exec())
