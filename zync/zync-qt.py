import sys
from PyQt4 import QtCore, QtGui

from qt_ui import Ui_MainWindow as Ui_Form


class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.button_sync, QtCore.SIGNAL("clicked()"),
                               self.do_sync)

    def do_sync(self):
        print "hi!"



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
