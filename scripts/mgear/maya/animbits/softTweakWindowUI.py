from mgear.maya import pyqt
from mgear.vendor.Qt import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.search_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_lineEdit.sizePolicy().hasHeightForWidth())
        self.search_lineEdit.setSizePolicy(sizePolicy)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.verticalLayout.addWidget(self.search_lineEdit)
        self.softTweak_listView = QtWidgets.QListView(self.centralwidget)
        self.softTweak_listView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.softTweak_listView.sizePolicy().hasHeightForWidth())
        self.softTweak_listView.setSizePolicy(sizePolicy)
        self.softTweak_listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.softTweak_listView.setAlternatingRowColors(True)
        self.softTweak_listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.softTweak_listView.setObjectName("softTweak_listView")
        self.verticalLayout.addWidget(self.softTweak_listView)
        self.refresh_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.verticalLayout.addWidget(self.refresh_pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.ctlGrp_label = QtWidgets.QLabel(self.groupBox)
        self.ctlGrp_label.setObjectName("ctlGrp_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ctlGrp_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ctlGrp_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ctlGrp_lineEdit.setObjectName("ctlGrp_lineEdit")
        self.horizontalLayout_2.addWidget(self.ctlGrp_lineEdit)
        self.setCtrlGrp_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.setCtrlGrp_pushButton.setEnabled(True)
        self.setCtrlGrp_pushButton.setObjectName("setCtrlGrp_pushButton")
        self.horizontalLayout_2.addWidget(self.setCtrlGrp_pushButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.parent_label = QtWidgets.QLabel(self.groupBox)
        self.parent_label.setObjectName("parent_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.parent_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.parent_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.parent_lineEdit.setObjectName("parent_lineEdit")
        self.horizontalLayout_3.addWidget(self.parent_lineEdit)
        self.setParent_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.setParent_pushButton.setObjectName("setParent_pushButton")
        self.horizontalLayout_3.addWidget(self.setParent_pushButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.size_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.size_doubleSpinBox.setDecimals(3)
        self.size_doubleSpinBox.setSingleStep(0.1)
        self.size_doubleSpinBox.setProperty("value", 0.5)
        self.size_doubleSpinBox.setObjectName("size_doubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.size_doubleSpinBox)
        self.size_label = QtWidgets.QLabel(self.groupBox)
        self.size_label.setObjectName("size_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.size_label)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.newTweak_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.newTweak_pushButton.setObjectName("newTweak_pushButton")
        self.verticalLayout_3.addWidget(self.newTweak_pushButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.delete_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.gridLayout_2.addWidget(self.delete_pushButton, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addObjectToTweak_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.addObjectToTweak_pushButton.setObjectName("addObjectToTweak_pushButton")
        self.gridLayout_3.addWidget(self.addObjectToTweak_pushButton, 1, 0, 1, 1)
        self.removeObjFromTweak_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.removeObjFromTweak_pushButton.setObjectName("removeObjFromTweak_pushButton")
        self.gridLayout_3.addWidget(self.removeObjFromTweak_pushButton, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.selectCtlBase_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.selectCtlBase_pushButton.setObjectName("selectCtlBase_pushButton")
        self.gridLayout_4.addWidget(self.selectCtlBase_pushButton, 1, 0, 1, 1)
        self.selectCtl_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.selectCtl_pushButton.setObjectName("selectCtl_pushButton")
        self.gridLayout_4.addWidget(self.selectCtl_pushButton, 0, 0, 1, 1)
        self.selectObjectsFromTweak_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.selectObjectsFromTweak_pushButton.setObjectName("selectObjectsFromTweak_pushButton")
        self.gridLayout_4.addWidget(self.selectObjectsFromTweak_pushButton, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTearOffEnabled(True)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.exportSelected_action = QtWidgets.QAction(MainWindow)
        self.exportSelected_action.setObjectName("exportSelected_action")
        self.actionExport_Selected = QtWidgets.QAction(MainWindow)
        self.actionExport_Selected.setObjectName("actionExport_Selected")
        self.import_action = QtWidgets.QAction(MainWindow)
        self.import_action.setObjectName("import_action")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.exportAll_action = QtWidgets.QAction(MainWindow)
        self.exportAll_action.setObjectName("exportAll_action")
        self.menuFile.addAction(self.exportSelected_action)
        self.menuFile.addAction(self.exportAll_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.import_action)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(pyqt.fakeTranslate("MainWindow", "MainWindow", None, -1))
        self.label.setText(pyqt.fakeTranslate("MainWindow", "SoftMod Tweaks List", None, -1))
        self.refresh_pushButton.setText(pyqt.fakeTranslate("MainWindow", "Refresh List", None, -1))
        self.groupBox.setTitle(pyqt.fakeTranslate("MainWindow", "Create Tweak", None, -1))
        self.name_label.setText(pyqt.fakeTranslate("MainWindow", "Name", None, -1))
        self.ctlGrp_label.setText(pyqt.fakeTranslate("MainWindow", "Ctl grp", None, -1))
        self.setCtrlGrp_pushButton.setText(pyqt.fakeTranslate("MainWindow", "<<<", None, -1))
        self.parent_label.setText(pyqt.fakeTranslate("MainWindow", "Parent", None, -1))
        self.setParent_pushButton.setText(pyqt.fakeTranslate("MainWindow", "<<<", None, -1))
        self.size_label.setText(pyqt.fakeTranslate("MainWindow", "Ctl Size", None, -1))
        self.newTweak_pushButton.setText(pyqt.fakeTranslate("MainWindow", "New Tweak", None, -1))
        self.groupBox_2.setTitle(pyqt.fakeTranslate("MainWindow", "Delete Tweak", None, -1))
        self.delete_pushButton.setText(pyqt.fakeTranslate("MainWindow", "Delete Tweak", None, -1))
        self.groupBox_3.setTitle(pyqt.fakeTranslate("MainWindow", "Edit Affected", None, -1))
        self.addObjectToTweak_pushButton.setText(pyqt.fakeTranslate("MainWindow", "Add Obj to Selected Tweak", None, -1))
        self.removeObjFromTweak_pushButton.setText(pyqt.fakeTranslate("MainWindow", "Remove Obj from Selected Tweak", None, -1))
        self.groupBox_4.setTitle(pyqt.fakeTranslate("MainWindow", "Select", None, -1))
        self.selectCtlBase_pushButton.setText(pyqt.fakeTranslate("MainWindow", "Select Base Ctl", None, -1))
        self.selectCtl_pushButton.setText(pyqt.fakeTranslate("MainWindow", "Select Ctl", None, -1))
        self.selectObjectsFromTweak_pushButton.setText(pyqt.fakeTranslate("MainWindow", "Select Affected Objects", None, -1))
        self.menuFile.setTitle(pyqt.fakeTranslate("MainWindow", "File", None, -1))
        self.exportSelected_action.setText(pyqt.fakeTranslate("MainWindow", "Export Selected", None, -1))
        self.actionExport_Selected.setText(pyqt.fakeTranslate("MainWindow", "Export Selected", None, -1))
        self.import_action.setText(pyqt.fakeTranslate("MainWindow", "Import", None, -1))
        self.actionAbout.setText(pyqt.fakeTranslate("MainWindow", "About", None, -1))
        self.exportAll_action.setText(pyqt.fakeTranslate("MainWindow", "Export All", None, -1))
