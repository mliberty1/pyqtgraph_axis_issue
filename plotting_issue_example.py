from PySide2.QtWidgets import QMainWindow, QWidget, QGridLayout
from pyqtgraph import ViewBox, PlotItem
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

app = QtGui.QApplication([])

window = QMainWindow()
holder = QWidget()
holder_layout = QGridLayout()
holder.setLayout(holder_layout)
window.setCentralWidget(holder)

#
# Grid section
#
grid_widget = pg.GraphicsLayoutWidget()
grid_viewBox1 = ViewBox(enableMenu=True)
grid_viewBox1.setXRange(0, 5, padding=0)
grid_viewBox1.setYRange(0, 2.5, padding=0)
grid_subplot1 = PlotItem(viewBox=grid_viewBox1)
grid_subplot1.showGrid(True, True, 0.2)
grid_viewBox1.setParent(grid_subplot1)
grid_widget.addItem(grid_subplot1, col=0, row=0)

grid_viewBox2 = ViewBox(enableMenu=True)
grid_viewBox2.setXRange(0, 5, padding=0)
grid_viewBox2.setYRange(0, 2.5, padding=0)
grid_subplot2 = PlotItem(viewBox=grid_viewBox2)
grid_subplot2.showGrid(True, True, 0.2)
grid_viewBox2.setParent(grid_subplot2)
grid_widget.addItem(grid_subplot2, col=1, row=0)

grid_viewBox3 = ViewBox(enableMenu=True)
grid_viewBox3.setXRange(0, 5, padding=0)
grid_viewBox3.setYRange(0, 2.5, padding=0)
grid_subplot3 = PlotItem(viewBox=grid_viewBox3)
grid_subplot3.showGrid(True, True, 0.2)
grid_viewBox3.setParent(grid_subplot3)
grid_widget.addItem(grid_subplot3, col=0, row=1)

grid_viewBox4 = ViewBox(enableMenu=True)
grid_viewBox4.setXRange(0, 5, padding=0)
grid_viewBox4.setYRange(0, 2.5, padding=0)
grid_subplot4 = PlotItem(viewBox=grid_viewBox4)
grid_subplot4.showGrid(True, True, 0.2)
grid_viewBox4.setParent(grid_subplot4)
grid_widget.addItem(grid_subplot4, col=1, row=1)
#
# Grid XLink 1->2,2->3,3-4
#
grid_subplot1.setXLink(grid_subplot2)
grid_subplot2.setXLink(grid_subplot3)
grid_subplot3.setXLink(grid_subplot4)


holder_layout.addWidget(grid_widget)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        window.show()
        QtGui.QApplication.instance().exec_()
