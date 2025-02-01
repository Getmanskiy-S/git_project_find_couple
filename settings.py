# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 559)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 541, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.rb_easy = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_easy.setFont(font)
        self.rb_easy.setChecked(True)
        self.rb_easy.setObjectName("rb_easy")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_easy)
        self.horizontalLayout.addWidget(self.rb_easy)
        self.rb_normal = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_normal.setFont(font)
        self.rb_normal.setObjectName("rb_normal")
        self.buttonGroup.addButton(self.rb_normal)
        self.horizontalLayout.addWidget(self.rb_normal)
        self.rb_hard = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_hard.setFont(font)
        self.rb_hard.setObjectName("rb_hard")
        self.buttonGroup.addButton(self.rb_hard)
        self.horizontalLayout.addWidget(self.rb_hard)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 541, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cards_slider = QtWidgets.QSlider(parent=self.horizontalLayoutWidget_2)
        self.cards_slider.setMinimum(2)
        self.cards_slider.setMaximum(50)
        self.cards_slider.setSingleStep(1)
        self.cards_slider.setProperty("value", 2)
        self.cards_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.cards_slider.setObjectName("cards_slider")
        self.horizontalLayout_3.addWidget(self.cards_slider)
        self.cards_spinbox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.cards_spinbox.setGeometry(QtCore.QRect(170, 280, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cards_spinbox.setFont(font)
        self.cards_spinbox.setMinimum(2)
        self.cards_spinbox.setMaximum(50)
        self.cards_spinbox.setSingleStep(1)
        self.cards_spinbox.setProperty("value", 2)
        self.cards_spinbox.setObjectName("cards_spinbox")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 330, 541, 91))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.volume_slider = QtWidgets.QSlider(parent=self.horizontalLayoutWidget_3)
        self.volume_slider.setMinimum(1)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSingleStep(1)
        self.volume_slider.setProperty("value", 50)
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.horizontalLayout_4.addWidget(self.volume_slider)
        self.volume_spinbox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.volume_spinbox.setGeometry(QtCore.QRect(170, 430, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.volume_spinbox.setFont(font)
        self.volume_spinbox.setMinimum(1)
        self.volume_spinbox.setMaximum(100)
        self.volume_spinbox.setSingleStep(1)
        self.volume_spinbox.setProperty("value", 50)
        self.volume_spinbox.setObjectName("volume_spinbox")
        self.save_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(180, 470, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Настройки игры"))
        self.label_2.setText(_translate("MainWindow", "Сложность:"))
        self.rb_easy.setText(_translate("MainWindow", "легко"))
        self.rb_normal.setText(_translate("MainWindow", "нормально"))
        self.rb_hard.setText(_translate("MainWindow", "сложно"))
        self.label_4.setText(_translate("MainWindow", "Кол-во пар карточек:"))
        self.label_5.setText(_translate("MainWindow", "Громкость (%)"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить изменения"))
