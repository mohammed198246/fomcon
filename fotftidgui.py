# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\CompSys\4th Semeter THESIS\Code\fomcon\fotftidgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_fotftid(object):
    def setupUi(self, MainWindow_fotftid):
        MainWindow_fotftid.setObjectName("MainWindow_fotftid")
        MainWindow_fotftid.resize(659, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow_fotftid)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_StartFreq = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_StartFreq.setFont(font)
        self.lineEdit_StartFreq.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_StartFreq.setObjectName("lineEdit_StartFreq")
        self.gridLayout_3.addWidget(self.lineEdit_StartFreq, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditOrder = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditOrder.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditOrder.setFont(font)
        self.lineEditOrder.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditOrder.setObjectName("lineEditOrder")
        self.gridLayout_3.addWidget(self.lineEditOrder, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 3, 1, 1)
        self.lineEdit_StopFreq = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_StopFreq.setFont(font)
        self.lineEdit_StopFreq.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_StopFreq.setObjectName("lineEdit_StopFreq")
        self.gridLayout_3.addWidget(self.lineEdit_StopFreq, 1, 2, 1, 1)
        self.comboBoxOptTypeMethod = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxOptTypeMethod.sizePolicy().hasHeightForWidth())
        self.comboBoxOptTypeMethod.setSizePolicy(sizePolicy)
        self.comboBoxOptTypeMethod.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBoxOptTypeMethod.setModelColumn(0)
        self.comboBoxOptTypeMethod.setObjectName("comboBoxOptTypeMethod")
        self.gridLayout_3.addWidget(self.comboBoxOptTypeMethod, 0, 1, 1, 2)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBoxData = QtWidgets.QComboBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxData.sizePolicy().hasHeightForWidth())
        self.comboBoxData.setSizePolicy(sizePolicy)
        self.comboBoxData.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxData.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxData.setFont(font)
        self.comboBoxData.setObjectName("comboBoxData")
        self.horizontalLayout_5.addWidget(self.comboBoxData)
        self.pushButtonAddData = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddData.sizePolicy().hasHeightForWidth())
        self.pushButtonAddData.setSizePolicy(sizePolicy)
        self.pushButtonAddData.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonAddData.setFont(font)
        self.pushButtonAddData.setObjectName("pushButtonAddData")
        self.horizontalLayout_5.addWidget(self.pushButtonAddData)
        self.pushButtonDeleteData = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonDeleteData.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteData.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteData.setSizePolicy(sizePolicy)
        self.pushButtonDeleteData.setObjectName("pushButtonDeleteData")
        self.horizontalLayout_5.addWidget(self.pushButtonDeleteData)
        self.pushButtonPlotData = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonPlotData.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPlotData.sizePolicy().hasHeightForWidth())
        self.pushButtonPlotData.setSizePolicy(sizePolicy)
        self.pushButtonPlotData.setObjectName("pushButtonPlotData")
        self.horizontalLayout_5.addWidget(self.pushButtonPlotData)
        self.pushButtonTrimData = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonTrimData.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTrimData.sizePolicy().hasHeightForWidth())
        self.pushButtonTrimData.setSizePolicy(sizePolicy)
        self.pushButtonTrimData.setObjectName("pushButtonTrimData")
        self.horizontalLayout_5.addWidget(self.pushButtonTrimData)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.comboBoxAlgorithm = QtWidgets.QComboBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxAlgorithm.sizePolicy().hasHeightForWidth())
        self.comboBoxAlgorithm.setSizePolicy(sizePolicy)
        self.comboBoxAlgorithm.setMinimumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxAlgorithm.setFont(font)
        self.comboBoxAlgorithm.setObjectName("comboBoxAlgorithm")
        self.horizontalLayout_6.addWidget(self.comboBoxAlgorithm)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(65, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEditLamda = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditLamda.sizePolicy().hasHeightForWidth())
        self.lineEditLamda.setSizePolicy(sizePolicy)
        self.lineEditLamda.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLamda.setFont(font)
        self.lineEditLamda.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLamda.setObjectName("lineEditLamda")
        self.horizontalLayout_4.addWidget(self.lineEditLamda)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_13.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBoxFixZeros = QtWidgets.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxFixZeros.setFont(font)
        self.checkBoxFixZeros.setObjectName("checkBoxFixZeros")
        self.horizontalLayout_9.addWidget(self.checkBoxFixZeros)
        self.textEdit_Zeros = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit_Zeros.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_Zeros.setFont(font)
        self.textEdit_Zeros.setAccessibleDescription("")
        self.textEdit_Zeros.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_Zeros.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhPreferLowercase)
        self.textEdit_Zeros.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_Zeros.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit_Zeros.setReadOnly(True)
        self.textEdit_Zeros.setObjectName("textEdit_Zeros")
        self.horizontalLayout_9.addWidget(self.textEdit_Zeros)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBoxFixPoles = QtWidgets.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxFixPoles.setFont(font)
        self.checkBoxFixPoles.setObjectName("checkBoxFixPoles")
        self.horizontalLayout_8.addWidget(self.checkBoxFixPoles)
        self.textEdit_Poles = QtWidgets.QTextEdit(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_Poles.setFont(font)
        self.textEdit_Poles.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhPreferLowercase)
        self.textEdit_Poles.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_Poles.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit_Poles.setReadOnly(True)
        self.textEdit_Poles.setAcceptRichText(False)
        self.textEdit_Poles.setObjectName("textEdit_Poles")
        self.horizontalLayout_8.addWidget(self.textEdit_Poles)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBoxUseDelay = QtWidgets.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxUseDelay.setFont(font)
        self.checkBoxUseDelay.setObjectName("checkBoxUseDelay")
        self.horizontalLayout_7.addWidget(self.checkBoxUseDelay)
        self.lineEdit_Delay = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_Delay.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Delay.sizePolicy().hasHeightForWidth())
        self.lineEdit_Delay.setSizePolicy(sizePolicy)
        self.lineEdit_Delay.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_Delay.setFont(font)
        self.lineEdit_Delay.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Delay.setObjectName("lineEdit_Delay")
        self.horizontalLayout_7.addWidget(self.lineEdit_Delay)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonModelStability = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonModelStability.sizePolicy().hasHeightForWidth())
        self.pushButtonModelStability.setSizePolicy(sizePolicy)
        self.pushButtonModelStability.setObjectName("pushButtonModelStability")
        self.horizontalLayout.addWidget(self.pushButtonModelStability)
        self.pushButtonModelValidate = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonModelValidate.setEnabled(False)
        self.pushButtonModelValidate.setObjectName("pushButtonModelValidate")
        self.horizontalLayout.addWidget(self.pushButtonModelValidate)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_13.addWidget(self.groupBox_6)
        self.groupBoxInitialGuess = QtWidgets.QGroupBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxInitialGuess.setFont(font)
        self.groupBoxInitialGuess.setObjectName("groupBoxInitialGuess")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBoxInitialGuess)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.groupBoxInitialGuess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(90, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lineEditCommesurateOder = QtWidgets.QLineEdit(self.groupBoxInitialGuess)
        self.lineEditCommesurateOder.setMaximumSize(QtCore.QSize(45, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCommesurateOder.setFont(font)
        self.lineEditCommesurateOder.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditCommesurateOder.setObjectName("lineEditCommesurateOder")
        self.horizontalLayout_10.addWidget(self.lineEditCommesurateOder)
        self.label_7 = QtWidgets.QLabel(self.groupBoxInitialGuess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(60, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.lineEditFOTFOrder = QtWidgets.QLineEdit(self.groupBoxInitialGuess)
        self.lineEditFOTFOrder.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditFOTFOrder.setFont(font)
        self.lineEditFOTFOrder.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditFOTFOrder.setPlaceholderText("")
        self.lineEditFOTFOrder.setObjectName("lineEditFOTFOrder")
        self.horizontalLayout_10.addWidget(self.lineEditFOTFOrder)
        self.comboBoxPolesOrZeros = QtWidgets.QComboBox(self.groupBoxInitialGuess)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxPolesOrZeros.setFont(font)
        self.comboBoxPolesOrZeros.setObjectName("comboBoxPolesOrZeros")
        self.horizontalLayout_10.addWidget(self.comboBoxPolesOrZeros)
        self.pushButtonGeneratGuess = QtWidgets.QPushButton(self.groupBoxInitialGuess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonGeneratGuess.sizePolicy().hasHeightForWidth())
        self.pushButtonGeneratGuess.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonGeneratGuess.setFont(font)
        self.pushButtonGeneratGuess.setObjectName("pushButtonGeneratGuess")
        self.horizontalLayout_10.addWidget(self.pushButtonGeneratGuess)
        self.verticalLayout_13.addWidget(self.groupBoxInitialGuess)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBoxUseCoefLimits = QtWidgets.QCheckBox(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxUseCoefLimits.sizePolicy().hasHeightForWidth())
        self.checkBoxUseCoefLimits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxUseCoefLimits.setFont(font)
        self.checkBoxUseCoefLimits.setObjectName("checkBoxUseCoefLimits")
        self.gridLayout_4.addWidget(self.checkBoxUseCoefLimits, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(110, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 1, 1, 1)
        self.lineEditCoefLimitLower = QtWidgets.QLineEdit(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCoefLimitLower.sizePolicy().hasHeightForWidth())
        self.lineEditCoefLimitLower.setSizePolicy(sizePolicy)
        self.lineEditCoefLimitLower.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCoefLimitLower.setFont(font)
        self.lineEditCoefLimitLower.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditCoefLimitLower.setPlaceholderText("")
        self.lineEditCoefLimitLower.setObjectName("lineEditCoefLimitLower")
        self.gridLayout_4.addWidget(self.lineEditCoefLimitLower, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 3, 1, 1)
        self.lineEditCoefLimitUpper = QtWidgets.QLineEdit(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCoefLimitUpper.sizePolicy().hasHeightForWidth())
        self.lineEditCoefLimitUpper.setSizePolicy(sizePolicy)
        self.lineEditCoefLimitUpper.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCoefLimitUpper.setFont(font)
        self.lineEditCoefLimitUpper.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditCoefLimitUpper.setPlaceholderText("")
        self.lineEditCoefLimitUpper.setObjectName("lineEditCoefLimitUpper")
        self.gridLayout_4.addWidget(self.lineEditCoefLimitUpper, 0, 4, 1, 1)
        self.checkBoxUseExpoLimits = QtWidgets.QCheckBox(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxUseExpoLimits.sizePolicy().hasHeightForWidth())
        self.checkBoxUseExpoLimits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxUseExpoLimits.setFont(font)
        self.checkBoxUseExpoLimits.setObjectName("checkBoxUseExpoLimits")
        self.gridLayout_4.addWidget(self.checkBoxUseExpoLimits, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(110, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 1, 1, 1)
        self.lineEditExpLimitLower = QtWidgets.QLineEdit(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditExpLimitLower.sizePolicy().hasHeightForWidth())
        self.lineEditExpLimitLower.setSizePolicy(sizePolicy)
        self.lineEditExpLimitLower.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditExpLimitLower.setFont(font)
        self.lineEditExpLimitLower.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditExpLimitLower.setPlaceholderText("")
        self.lineEditExpLimitLower.setObjectName("lineEditExpLimitLower")
        self.gridLayout_4.addWidget(self.lineEditExpLimitLower, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setTextFormat(QtCore.Qt.RichText)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 3, 1, 1)
        self.lineEditExpLimitUpper = QtWidgets.QLineEdit(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditExpLimitUpper.sizePolicy().hasHeightForWidth())
        self.lineEditExpLimitUpper.setSizePolicy(sizePolicy)
        self.lineEditExpLimitUpper.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditExpLimitUpper.setFont(font)
        self.lineEditExpLimitUpper.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditExpLimitUpper.setPlaceholderText("")
        self.lineEditExpLimitUpper.setObjectName("lineEditExpLimitUpper")
        self.gridLayout_4.addWidget(self.lineEditExpLimitUpper, 1, 4, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.comboBoxOptFix = QtWidgets.QComboBox(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxOptFix.sizePolicy().hasHeightForWidth())
        self.comboBoxOptFix.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxOptFix.setFont(font)
        self.comboBoxOptFix.setObjectName("comboBoxOptFix")
        self.horizontalLayout_11.addWidget(self.comboBoxOptFix)
        self.pushButtonIdentify = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButtonIdentify.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonIdentify.sizePolicy().hasHeightForWidth())
        self.pushButtonIdentify.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonIdentify.setFont(font)
        self.pushButtonIdentify.setObjectName("pushButtonIdentify")
        self.horizontalLayout_11.addWidget(self.pushButtonIdentify)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addWidget(self.groupBox_7)
        MainWindow_fotftid.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_fotftid)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_fotftid.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_fotftid)
        self.statusbar.setObjectName("statusbar")
        MainWindow_fotftid.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.lineEditOrder)
        self.label_6.setBuddy(self.lineEditLamda)
        self.label_8.setBuddy(self.lineEditCommesurateOder)
        self.label_7.setBuddy(self.lineEditFOTFOrder)
        self.label_9.setBuddy(self.lineEditCoefLimitLower)
        self.label_13.setBuddy(self.lineEditCoefLimitUpper)
        self.label_10.setBuddy(self.lineEditExpLimitLower)
        self.label_12.setBuddy(self.lineEditExpLimitUpper)

        self.retranslateUi(MainWindow_fotftid)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_fotftid)
        MainWindow_fotftid.setTabOrder(self.comboBoxOptTypeMethod, self.lineEdit_StartFreq)
        MainWindow_fotftid.setTabOrder(self.lineEdit_StartFreq, self.lineEdit_StopFreq)
        MainWindow_fotftid.setTabOrder(self.lineEdit_StopFreq, self.lineEditOrder)
        MainWindow_fotftid.setTabOrder(self.lineEditOrder, self.comboBoxData)
        MainWindow_fotftid.setTabOrder(self.comboBoxData, self.pushButtonAddData)
        MainWindow_fotftid.setTabOrder(self.pushButtonAddData, self.comboBoxAlgorithm)
        MainWindow_fotftid.setTabOrder(self.comboBoxAlgorithm, self.lineEditLamda)
        MainWindow_fotftid.setTabOrder(self.lineEditLamda, self.checkBoxFixZeros)
        MainWindow_fotftid.setTabOrder(self.checkBoxFixZeros, self.textEdit_Zeros)
        MainWindow_fotftid.setTabOrder(self.textEdit_Zeros, self.checkBoxFixPoles)
        MainWindow_fotftid.setTabOrder(self.checkBoxFixPoles, self.textEdit_Poles)
        MainWindow_fotftid.setTabOrder(self.textEdit_Poles, self.checkBoxUseDelay)
        MainWindow_fotftid.setTabOrder(self.checkBoxUseDelay, self.lineEdit_Delay)
        MainWindow_fotftid.setTabOrder(self.lineEdit_Delay, self.lineEditCommesurateOder)
        MainWindow_fotftid.setTabOrder(self.lineEditCommesurateOder, self.lineEditFOTFOrder)
        MainWindow_fotftid.setTabOrder(self.lineEditFOTFOrder, self.comboBoxPolesOrZeros)
        MainWindow_fotftid.setTabOrder(self.comboBoxPolesOrZeros, self.pushButtonGeneratGuess)
        MainWindow_fotftid.setTabOrder(self.pushButtonGeneratGuess, self.checkBoxUseCoefLimits)
        MainWindow_fotftid.setTabOrder(self.checkBoxUseCoefLimits, self.lineEditCoefLimitLower)
        MainWindow_fotftid.setTabOrder(self.lineEditCoefLimitLower, self.lineEditCoefLimitUpper)
        MainWindow_fotftid.setTabOrder(self.lineEditCoefLimitUpper, self.checkBoxUseExpoLimits)
        MainWindow_fotftid.setTabOrder(self.checkBoxUseExpoLimits, self.lineEditExpLimitLower)
        MainWindow_fotftid.setTabOrder(self.lineEditExpLimitLower, self.lineEditExpLimitUpper)
        MainWindow_fotftid.setTabOrder(self.lineEditExpLimitUpper, self.comboBoxOptFix)
        MainWindow_fotftid.setTabOrder(self.comboBoxOptFix, self.pushButtonIdentify)

    def retranslateUi(self, MainWindow_fotftid):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_fotftid.setWindowTitle(_translate("MainWindow_fotftid", "FOTF Time Domain Identification"))
        self.groupBox_2.setTitle(_translate("MainWindow_fotftid", "Simulation Parameter"))
        self.lineEdit_StartFreq.setText(_translate("MainWindow_fotftid", "0.0001"))
        self.lineEdit_StartFreq.setPlaceholderText(_translate("MainWindow_fotftid", "Start (float)"))
        self.label_2.setText(_translate("MainWindow_fotftid", "w range:"))
        self.lineEditOrder.setText(_translate("MainWindow_fotftid", "10"))
        self.lineEditOrder.setPlaceholderText(_translate("MainWindow_fotftid", "(int)"))
        self.label.setText(_translate("MainWindow_fotftid", "Method:"))
        self.label_3.setText(_translate("MainWindow_fotftid", "Order:"))
        self.lineEdit_StopFreq.setText(_translate("MainWindow_fotftid", "10000"))
        self.lineEdit_StopFreq.setPlaceholderText(_translate("MainWindow_fotftid", "Stop (int)"))
        self.groupBox_7.setTitle(_translate("MainWindow_fotftid", "Identification and Options"))
        self.groupBox_5.setTitle(_translate("MainWindow_fotftid", "Source Data"))
        self.label_4.setText(_translate("MainWindow_fotftid", "DATA Objects:"))
        self.pushButtonAddData.setText(_translate("MainWindow_fotftid", "Add"))
        self.pushButtonDeleteData.setText(_translate("MainWindow_fotftid", "Delete"))
        self.pushButtonPlotData.setText(_translate("MainWindow_fotftid", "Plot"))
        self.pushButtonTrimData.setText(_translate("MainWindow_fotftid", "Trim"))
        self.label_5.setText(_translate("MainWindow_fotftid", "Algorithm:      "))
        self.label_6.setText(_translate("MainWindow_fotftid", "Lamda:"))
        self.lineEditLamda.setText(_translate("MainWindow_fotftid", "0.01"))
        self.groupBox_6.setTitle(_translate("MainWindow_fotftid", "Identified Model"))
        self.checkBoxFixZeros.setText(_translate("MainWindow_fotftid", "fix"))
        self.textEdit_Zeros.setStatusTip(_translate("MainWindow_fotftid", "0"))
        self.checkBoxFixPoles.setText(_translate("MainWindow_fotftid", "fix"))
        self.checkBoxUseDelay.setText(_translate("MainWindow_fotftid", "delay [s] :"))
        self.lineEdit_Delay.setText(_translate("MainWindow_fotftid", "0"))
        self.lineEdit_Delay.setPlaceholderText(_translate("MainWindow_fotftid", "int [s]"))
        self.pushButtonModelStability.setText(_translate("MainWindow_fotftid", "Stability Check"))
        self.pushButtonModelValidate.setText(_translate("MainWindow_fotftid", "Validate Model"))
        self.groupBoxInitialGuess.setTitle(_translate("MainWindow_fotftid", "Generate Initial Guess Model"))
        self.label_8.setText(_translate("MainWindow_fotftid", "q[0.01:2):"))
        self.lineEditCommesurateOder.setText(_translate("MainWindow_fotftid", "0.5"))
        self.label_7.setText(_translate("MainWindow_fotftid", "Order:"))
        self.lineEditFOTFOrder.setText(_translate("MainWindow_fotftid", "4"))
        self.pushButtonGeneratGuess.setText(_translate("MainWindow_fotftid", "Generate"))
        self.checkBoxUseCoefLimits.setText(_translate("MainWindow_fotftid", "Coefficient Limits"))
        self.label_9.setText(_translate("MainWindow_fotftid", "Minimum:"))
        self.lineEditCoefLimitLower.setText(_translate("MainWindow_fotftid", "4"))
        self.label_13.setText(_translate("MainWindow_fotftid", "Maximum:"))
        self.lineEditCoefLimitUpper.setText(_translate("MainWindow_fotftid", "4"))
        self.checkBoxUseExpoLimits.setText(_translate("MainWindow_fotftid", "Exponents Limits"))
        self.label_10.setText(_translate("MainWindow_fotftid", "Minimum:"))
        self.lineEditExpLimitLower.setText(_translate("MainWindow_fotftid", "4"))
        self.label_12.setText(_translate("MainWindow_fotftid", "Maximum:"))
        self.lineEditExpLimitUpper.setText(_translate("MainWindow_fotftid", "4"))
        self.pushButtonIdentify.setText(_translate("MainWindow_fotftid", "Identify"))

