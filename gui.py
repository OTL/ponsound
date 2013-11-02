import sys
import os
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui


class ButtonBox(QtGui.QWidget):
    def __init__(self, names, player, parent):
        super(QtGui.QWidget, self).__init__(parent=parent)
        grid = QtGui.QGridLayout()
        for i, name in enumerate(names):
            button = QtGui.QPushButton(name, self)
            button.clicked.connect(self.make_calluser(player, name))
            row, col = divmod(i, 5)
            grid.addWidget(button, row, col)
        self.setLayout(grid)

    def make_calluser(self, player, name):
        def calluser():
            player.play(name + '.mp3')
        return calluser

class MusicFile:
    def __init__(self, name):
        self._name = name

    def play(self):
        print self._name

class Player:
    def __init__(self):
        pass

    def play(self, file):
        os.system('open -g ' + file)

def main():
    app = QtGui.QApplication(sys.argv)
    panel = QtGui.QWidget()
    player = Player()
    button_box = ButtonBox([os.path.splitext(x)[0] for x in os.listdir('.')
                            if os.path.splitext(x)[1] == '.mp3'],
                           player, panel)
    panel_layout = QtGui.QVBoxLayout()
    panel_layout.addWidget(button_box)
    panel.setLayout(panel_layout)
#    panel.setFixedSize(320, 200)

    main_window = QtGui.QMainWindow()
    main_window.setWindowTitle("Pon Sound")

    main_window.setCentralWidget(panel)
    main_window.show()
    
    app.exec_()

main()
