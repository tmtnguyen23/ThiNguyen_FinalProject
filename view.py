# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app-designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(807, 572))
        MainWindow.setMaximumSize(QtCore.QSize(807, 572))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(70, 120, 671, 311))
        self.tabs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabs.setDocumentMode(False)
        self.tabs.setObjectName("tabs")
        self.tab_cube = QtWidgets.QWidget()
        self.tab_cube.setObjectName("tab_cube")
        self.entry_side = QtWidgets.QLineEdit(self.tab_cube)
        self.entry_side.setGeometry(QtCore.QRect(120, 110, 221, 31))
        self.entry_side.setObjectName("entry_side")
        self.label_side = QtWidgets.QLabel(self.tab_cube)
        self.label_side.setGeometry(QtCore.QRect(60, 120, 55, 16))
        self.label_side.setObjectName("label_side")
        self.button_ans_cub = QtWidgets.QPushButton(self.tab_cube)
        self.button_ans_cub.setGeometry(QtCore.QRect(180, 190, 93, 28))
        self.button_ans_cub.setObjectName("button_ans_cub")
        self.image_cube = QtWidgets.QLabel(self.tab_cube)
        self.image_cube.setGeometry(QtCore.QRect(400, 80, 171, 151))
        self.image_cube.setText("")
        self.image_cube.setPixmap(QtGui.QPixmap("images/cube.png"))
        self.image_cube.setObjectName("image_cube")
        self.title_cube = QtWidgets.QLabel(self.tab_cube)
        self.title_cube.setGeometry(QtCore.QRect(200, 20, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_cube.setFont(font)
        self.title_cube.setObjectName("title_cube")
        self.radio_roundup_cube = QtWidgets.QRadioButton(self.tab_cube)
        self.radio_roundup_cube.setGeometry(QtCore.QRect(160, 160, 131, 20))
        self.radio_roundup_cube.setObjectName("radio_roundup_cube")
        self.tabs.addTab(self.tab_cube, "")
        self.tab_sphere = QtWidgets.QWidget()
        self.tab_sphere.setObjectName("tab_sphere")
        self.button_ans_sph = QtWidgets.QPushButton(self.tab_sphere)
        self.button_ans_sph.setGeometry(QtCore.QRect(170, 210, 93, 28))
        self.button_ans_sph.setObjectName("button_ans_sph")
        self.title_sphere = QtWidgets.QLabel(self.tab_sphere)
        self.title_sphere.setGeometry(QtCore.QRect(200, 20, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_sphere.setFont(font)
        self.title_sphere.setObjectName("title_sphere")
        self.entry_radius = QtWidgets.QLineEdit(self.tab_sphere)
        self.entry_radius.setGeometry(QtCore.QRect(120, 120, 221, 31))
        self.entry_radius.setObjectName("entry_radius")
        self.label_radius = QtWidgets.QLabel(self.tab_sphere)
        self.label_radius.setGeometry(QtCore.QRect(60, 130, 55, 16))
        self.label_radius.setObjectName("label_radius")
        self.image_sphere = QtWidgets.QLabel(self.tab_sphere)
        self.image_sphere.setGeometry(QtCore.QRect(400, 80, 171, 151))
        self.image_sphere.setText("")
        self.image_sphere.setPixmap(QtGui.QPixmap("images/sphere.png"))
        self.image_sphere.setObjectName("image_sphere")
        self.radio_pi_sphere = QtWidgets.QRadioButton(self.tab_sphere)
        self.radio_pi_sphere.setGeometry(QtCore.QRect(110, 170, 100, 20))
        self.radio_pi_sphere.setAutoExclusive(False)
        self.radio_pi_sphere.setObjectName("radio_pi_sphere")
        self.radio_roundup_sphere = QtWidgets.QRadioButton(self.tab_sphere)
        self.radio_roundup_sphere.setGeometry(QtCore.QRect(220, 170, 131, 20))
        self.radio_roundup_sphere.setAutoExclusive(False)
        self.radio_roundup_sphere.setObjectName("radio_roundup_sphere")
        self.tabs.addTab(self.tab_sphere, "")
        self.tab_rectangular = QtWidgets.QWidget()
        self.tab_rectangular.setObjectName("tab_rectangular")
        self.title_rcpr = QtWidgets.QLabel(self.tab_rectangular)
        self.title_rcpr.setGeometry(QtCore.QRect(160, 20, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_rcpr.setFont(font)
        self.title_rcpr.setObjectName("title_rcpr")
        self.image_rcpr = QtWidgets.QLabel(self.tab_rectangular)
        self.image_rcpr.setGeometry(QtCore.QRect(410, 70, 171, 151))
        self.image_rcpr.setText("")
        self.image_rcpr.setPixmap(QtGui.QPixmap("images/rcpr.png"))
        self.image_rcpr.setObjectName("image_rcpr")
        self.button_ans_rcpr = QtWidgets.QPushButton(self.tab_rectangular)
        self.button_ans_rcpr.setGeometry(QtCore.QRect(230, 230, 93, 28))
        self.button_ans_rcpr.setObjectName("button_ans_rcpr")
        self.entry_length_rcpr = QtWidgets.QLineEdit(self.tab_rectangular)
        self.entry_length_rcpr.setGeometry(QtCore.QRect(170, 120, 221, 31))
        self.entry_length_rcpr.setObjectName("entry_length_rcpr")
        self.label_width_rcpr = QtWidgets.QLabel(self.tab_rectangular)
        self.label_width_rcpr.setGeometry(QtCore.QRect(110, 90, 55, 16))
        self.label_width_rcpr.setObjectName("label_width_rcpr")
        self.label_length_rcpr = QtWidgets.QLabel(self.tab_rectangular)
        self.label_length_rcpr.setGeometry(QtCore.QRect(110, 130, 55, 16))
        self.label_length_rcpr.setObjectName("label_length_rcpr")
        self.entry_height_rcpr = QtWidgets.QLineEdit(self.tab_rectangular)
        self.entry_height_rcpr.setGeometry(QtCore.QRect(170, 160, 221, 31))
        self.entry_height_rcpr.setObjectName("entry_height_rcpr")
        self.label_height_rcpr = QtWidgets.QLabel(self.tab_rectangular)
        self.label_height_rcpr.setGeometry(QtCore.QRect(110, 170, 55, 16))
        self.label_height_rcpr.setObjectName("label_height_rcpr")
        self.entry_width_rcpr = QtWidgets.QLineEdit(self.tab_rectangular)
        self.entry_width_rcpr.setGeometry(QtCore.QRect(170, 80, 221, 31))
        self.entry_width_rcpr.setObjectName("entry_width_rcpr")
        self.radio_roundup_rcpr = QtWidgets.QRadioButton(self.tab_rectangular)
        self.radio_roundup_rcpr.setGeometry(QtCore.QRect(210, 200, 131, 20))
        self.radio_roundup_rcpr.setObjectName("radio_roundup_rcpr")
        self.tabs.addTab(self.tab_rectangular, "")
        self.tab_cone = QtWidgets.QWidget()
        self.tab_cone.setObjectName("tab_cone")
        self.title_cone = QtWidgets.QLabel(self.tab_cone)
        self.title_cone.setGeometry(QtCore.QRect(200, 20, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_cone.setFont(font)
        self.title_cone.setObjectName("title_cone")
        self.image_cone = QtWidgets.QLabel(self.tab_cone)
        self.image_cone.setGeometry(QtCore.QRect(400, 80, 171, 151))
        self.image_cone.setText("")
        self.image_cone.setPixmap(QtGui.QPixmap("images/cone.png"))
        self.image_cone.setObjectName("image_cone")
        self.entry_radius_cone = QtWidgets.QLineEdit(self.tab_cone)
        self.entry_radius_cone.setGeometry(QtCore.QRect(160, 80, 221, 31))
        self.entry_radius_cone.setText("")
        self.entry_radius_cone.setObjectName("entry_radius_cone")
        self.entry_height_cone = QtWidgets.QLineEdit(self.tab_cone)
        self.entry_height_cone.setGeometry(QtCore.QRect(160, 130, 221, 31))
        self.entry_height_cone.setObjectName("entry_height_cone")
        self.label_radius_cone = QtWidgets.QLabel(self.tab_cone)
        self.label_radius_cone.setGeometry(QtCore.QRect(90, 90, 55, 16))
        self.label_radius_cone.setObjectName("label_radius_cone")
        self.label_height_cone = QtWidgets.QLabel(self.tab_cone)
        self.label_height_cone.setGeometry(QtCore.QRect(90, 140, 55, 16))
        self.label_height_cone.setObjectName("label_height_cone")
        self.button_ans_cone = QtWidgets.QPushButton(self.tab_cone)
        self.button_ans_cone.setGeometry(QtCore.QRect(220, 210, 93, 28))
        self.button_ans_cone.setObjectName("button_ans_cone")
        self.radio_pi_cone = QtWidgets.QRadioButton(self.tab_cone)
        self.radio_pi_cone.setGeometry(QtCore.QRect(150, 180, 110, 20))
        self.radio_pi_cone.setAutoExclusive(False)
        self.radio_pi_cone.setObjectName("radio_pi_cone")
        self.radio_roundup_cone = QtWidgets.QRadioButton(self.tab_cone)
        self.radio_roundup_cone.setGeometry(QtCore.QRect(260, 180, 131, 20))
        self.radio_roundup_cone.setAutoExclusive(False)
        self.radio_roundup_cone.setObjectName("radio_roundup_cone")
        self.tabs.addTab(self.tab_cone, "")
        self.tab_cylinder = QtWidgets.QWidget()
        self.tab_cylinder.setObjectName("tab_cylinder")
        self.title_cyc = QtWidgets.QLabel(self.tab_cylinder)
        self.title_cyc.setGeometry(QtCore.QRect(200, 20, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_cyc.setFont(font)
        self.title_cyc.setObjectName("title_cyc")
        self.image_cyc = QtWidgets.QLabel(self.tab_cylinder)
        self.image_cyc.setGeometry(QtCore.QRect(400, 80, 171, 151))
        self.image_cyc.setText("")
        self.image_cyc.setPixmap(QtGui.QPixmap("images/cylinder.png"))
        self.image_cyc.setObjectName("image_cyc")
        self.entry_radius_cyc = QtWidgets.QLineEdit(self.tab_cylinder)
        self.entry_radius_cyc.setGeometry(QtCore.QRect(160, 80, 221, 31))
        self.entry_radius_cyc.setText("")
        self.entry_radius_cyc.setObjectName("entry_radius_cyc")
        self.label_radius_cyc = QtWidgets.QLabel(self.tab_cylinder)
        self.label_radius_cyc.setGeometry(QtCore.QRect(30, 80, 121, 31))
        self.label_radius_cyc.setObjectName("label_radius_cyc")
        self.entry_height_cyc = QtWidgets.QLineEdit(self.tab_cylinder)
        self.entry_height_cyc.setGeometry(QtCore.QRect(160, 130, 221, 31))
        self.entry_height_cyc.setObjectName("entry_height_cyc")
        self.label_height_cyc = QtWidgets.QLabel(self.tab_cylinder)
        self.label_height_cyc.setGeometry(QtCore.QRect(60, 140, 55, 16))
        self.label_height_cyc.setObjectName("label_height_cyc")
        self.button_ans_cyc = QtWidgets.QPushButton(self.tab_cylinder)
        self.button_ans_cyc.setGeometry(QtCore.QRect(220, 210, 93, 28))
        self.button_ans_cyc.setObjectName("button_ans_cyc")
        self.radio_pi_cylinder = QtWidgets.QRadioButton(self.tab_cylinder)
        self.radio_pi_cylinder.setGeometry(QtCore.QRect(150, 180, 110, 20))
        self.radio_pi_cylinder.setAutoExclusive(False)
        self.radio_pi_cylinder.setObjectName("radio_pi_cylinder")
        self.radio_roundup_cylinder = QtWidgets.QRadioButton(self.tab_cylinder)
        self.radio_roundup_cylinder.setGeometry(QtCore.QRect(260, 180, 131, 20))
        self.radio_roundup_cylinder.setAutoExclusive(False)
        self.radio_roundup_cylinder.setObjectName("radio_roundup_cylinder")
        self.tabs.addTab(self.tab_cylinder, "")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(250, 30, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_main.setFont(font)
        self.label_main.setObjectName("label_main")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(60, 440, 700, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_output.setFont(font)
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Volume Calculator"))
        self.label_side.setText(_translate("MainWindow", "Side"))
        self.button_ans_cub.setText(_translate("MainWindow", "Get Answer!"))
        self.title_cube.setText(_translate("MainWindow", "Calculates the Volume of a Cube"))
        self.radio_roundup_cube.setText(_translate("MainWindow", "2-decimal answer"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_cube), _translate("MainWindow", "Cube"))
        self.button_ans_sph.setText(_translate("MainWindow", "Get Answer!"))
        self.title_sphere.setText(_translate("MainWindow", "Calculates the Volume of a Sphere"))
        self.label_radius.setText(_translate("MainWindow", "Radius"))
        self.radio_pi_sphere.setText(_translate("MainWindow", "answer w/ π"))
        self.radio_roundup_sphere.setText(_translate("MainWindow", "2-decimal answer"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_sphere), _translate("MainWindow", "Sphere"))
        self.title_rcpr.setText(_translate("MainWindow", "Calculates the Volume of a Rectangular Prism"))
        self.button_ans_rcpr.setText(_translate("MainWindow", "Get Answer!"))
        self.label_width_rcpr.setText(_translate("MainWindow", "Width"))
        self.label_length_rcpr.setText(_translate("MainWindow", "Length"))
        self.label_height_rcpr.setText(_translate("MainWindow", "Height"))
        self.radio_roundup_rcpr.setText(_translate("MainWindow", "2-decimal answer"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_rectangular), _translate("MainWindow", "Rectangular Prism"))
        self.title_cone.setText(_translate("MainWindow", "Calculates the Volume of a Cone"))
        self.label_radius_cone.setText(_translate("MainWindow", "Radius"))
        self.label_height_cone.setText(_translate("MainWindow", "Height"))
        self.button_ans_cone.setText(_translate("MainWindow", "Get Answer!"))
        self.radio_pi_cone.setText(_translate("MainWindow", "answer w/ π"))
        self.radio_roundup_cone.setText(_translate("MainWindow", "2-decimal answer"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_cone), _translate("MainWindow", "Cone"))
        self.title_cyc.setText(_translate("MainWindow", "Calculates the Volume of a Cylinder"))
        self.label_radius_cyc.setText(_translate("MainWindow", "Radius of the base"))
        self.label_height_cyc.setText(_translate("MainWindow", "Height"))
        self.button_ans_cyc.setText(_translate("MainWindow", "Get Answer!"))
        self.radio_pi_cylinder.setText(_translate("MainWindow", "answer w/ π"))
        self.radio_roundup_cylinder.setText(_translate("MainWindow", "2-decimal answer"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_cylinder), _translate("MainWindow", "Cylinder"))
        self.label_main.setText(_translate("MainWindow", "Welcome to Volume Calculator!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())