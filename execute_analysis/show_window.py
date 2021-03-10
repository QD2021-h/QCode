import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from analysis_excel import Ui_MainWindow

def show_main_window():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    # the icon_img must input the same_level_dir with the current project
    ui = Ui_MainWindow()
    # init_window
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_main_window()
