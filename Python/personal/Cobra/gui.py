# -*- coding: utf-8 -*-

import sys,os
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QMainWindow, qApp, QAction, QToolTip, 
    QPushButton, QApplication) 
from PyQt5.QtGui import QIcon,QFont

window_title = "Cobra V0.01"
win_dim = {
	"h":720,
	"w":1280
}
truepath = os.getcwd()

class Window(QMainWindow):

	actions = {}
	def __init__(self):
		super().__init__()
		
		QToolTip.setFont(QFont('SansSerif',12))
		self.initWindow()
		self.initUI()
		self.initToolbar()
		self.initMenubar()
		self.show()

	def initWindow(self):

		self.setToolTip("This is a <b>QMainWindow</b> widget!")
		self.resize(win_dim["w"],win_dim["h"])
		self.centerScreen()
		self.setWindowTitle(window_title)
		self.setWindowIcon(QIcon(truepath+"/img/ShittyCobra.png"))


	def initUI(self):
		btn = QPushButton("Press Me!", self)
		btn.setToolTip("This is a <i>QPushButton</i> widget!")
		btn.resize(btn.sizeHint())
		btn.move(win_dim["w"]/2,win_dim["h"]/2)

	def initToolbar(self):
		exitAct = QAction(QIcon(truepath+"/img/ShittyCobra.png"),'&Exit Cobra', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit Cobra')
		exitAct.triggered.connect(qApp.quit)
		self.toolbar = self.addToolBar("Exit Cobra")
		self.toolbar.addAction(exitAct)
		self.actions["exit"] = exitAct

	def initMenubar(self):

		menu = self.menuBar()
		menu.setNativeMenuBar(False)
		fileMenu = menu.addMenu("&File")
		print(self.actions)
		for action in self.actions:
			print(action)
			fileMenu.addAction(self.actions[action])

	def centerScreen(self):

		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())



if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())