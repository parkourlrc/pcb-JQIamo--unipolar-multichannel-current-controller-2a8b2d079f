from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, settings):
        self.settings = settings

        self.board_label = []
        self.set_value = []
        self.monitor_value = []
        self.min_x_size = 500
        self.max_x_size = 600
        self.min_y_size = 200
        self.max_y_size = 400

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(self.max_x_size, self.min_y_size)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_0 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_0.setObjectName("gridLayout_0")

        # JQI image
        self.box_jqi = QtWidgets.QFrame(self.centralwidget)
        self.box_jqi.setObjectName("box_jqi")
        self.layout_jqi = QtWidgets.QHBoxLayout(self.box_jqi)
        self.layout_jqi.setObjectName("layout_jqi")
        self.jqi_label = QtWidgets.QLabel()
        self.jqi_image = QtGui.QPixmap('jqi-logo.png').scaledToWidth(300)
        self.jqi_label.setPixmap(self.jqi_image)
        self.layout_jqi.addWidget(self.jqi_label)
        self.gridLayout_0.addWidget(self.box_jqi, 3, 1, 1, 1)

        # General setup
        self.general_setup()

        # PCB board control panel
        self.pcb_panel()

        # self.step_increase_panel()

        # Open & Save panel
        self.file_panel()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def general_setup(self):
        self.box_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.box_1.setObjectName("box_1")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.box_1)
        self.gridLayout_1.setObjectName("gridLayout_1")

        self.port_label = QtWidgets.QLabel()
        self.port_label.setMinimumSize(QtCore.QSize(34, 20))
        self.port_label.setMaximumSize(QtCore.QSize(34, 20))
        self.port_label.setObjectName("port_label")
        self.gridLayout_1.addWidget(self.port_label, 0, 0, 1, 1)
        self.port_value = QtWidgets.QLineEdit()
        self.port_value.setMinimumSize(QtCore.QSize(60, 20))
        self.port_value.setMaximumSize(QtCore.QSize(60, 20))
        self.gridLayout_1.addWidget(self.port_value, 0, 1, 1, 1)
        self.rate_label = QtWidgets.QLabel()
        self.rate_label.setMinimumSize(QtCore.QSize(60, 20))
        self.rate_label.setMaximumSize(QtCore.QSize(60, 20))
        self.rate_label.setObjectName("rate_label")
        self.gridLayout_1.addWidget(self.rate_label, 0, 2, 1, 1)
        self.rate_value = QtWidgets.QLineEdit()
        self.rate_value.setMinimumSize(QtCore.QSize(60, 20))
        self.rate_value.setMaximumSize(QtCore.QSize(60, 20))
        self.gridLayout_1.addWidget(self.rate_value, 0, 3, 1, 1)

        # buttons
        self.connect_button = QtWidgets.QPushButton()
        self.connect_button.setMinimumSize(QtCore.QSize(180, 20))
        self.connect_button.setMaximumSize(QtCore.QSize(180, 20))
        self.gridLayout_1.addWidget(self.connect_button, 0, 4, 1, 2)
        self.apply_button = QtWidgets.QPushButton()
        self.apply_button.setMinimumSize(QtCore.QSize(50, 20))
        self.apply_button.setMaximumSize(QtCore.QSize(50, 20))
        self.gridLayout_1.addWidget(self.apply_button, 0, 6, 1, 1)
        self.monitor_button = QtWidgets.QPushButton()
        self.monitor_button.setMinimumSize(QtCore.QSize(50, 20))
        self.monitor_button.setMaximumSize(QtCore.QSize(50, 20))
        self.gridLayout_1.addWidget(self.monitor_button, 1, 6, 1, 1)



        self.label_min_current = QtWidgets.QLabel()
        self.label_min_current.setMinimumSize(QtCore.QSize(90, 20))
        self.label_min_current.setMaximumSize(QtCore.QSize(90, 20))
        self.label_min_current.setObjectName("label_min_current")
        self.gridLayout_1.addWidget(self.label_min_current, 1, 0, 1, 1)
        self.value_min_current = QtWidgets.QLineEdit()
        self.value_min_current.setMinimumSize(QtCore.QSize(60, 20))
        self.value_min_current.setMaximumSize(QtCore.QSize(60, 20))
        self.gridLayout_1.addWidget(self.value_min_current, 1, 1, 1, 1)

        self.label_max_current = QtWidgets.QLabel()
        self.label_max_current.setMinimumSize(QtCore.QSize(90, 20))
        self.label_max_current.setMaximumSize(QtCore.QSize(90, 20))
        self.label_max_current.setObjectName("label_max_current")
        self.gridLayout_1.addWidget(self.label_max_current, 1, 2, 1, 1)
        self.value_max_current = QtWidgets.QLineEdit()
        self.value_max_current.setMinimumSize(QtCore.QSize(60, 20))
        self.value_max_current.setMaximumSize(QtCore.QSize(60, 20))
        self.gridLayout_1.addWidget(self.value_max_current, 1, 3, 1, 1)

        self.label_step_size = QtWidgets.QLabel()
        self.label_step_size.setMinimumSize(QtCore.QSize(70, 20))
        self.label_step_size.setMaximumSize(QtCore.QSize(70, 20))
        self.label_step_size.setObjectName("label_step_size")
        self.gridLayout_1.addWidget(self.label_step_size, 1, 4, 1, 1)
        self.value_step_size = QtWidgets.QLineEdit()
        self.value_step_size.setMinimumSize(QtCore.QSize(60, 20))
        self.value_step_size.setMaximumSize(QtCore.QSize(60, 20))
        self.gridLayout_1.addWidget(self.value_step_size, 1, 5, 1, 1)


        self.gridLayout_0.addWidget(self.box_1, 0, 0, 1, 2)

        _translate = QtCore.QCoreApplication.translate
        self.port_label.setText(_translate("MainWindow", "Port"))
        self.rate_label.setText(_translate("MainWindow", "Baud Rate"))
        self.label_min_current.setText(_translate("MainWindow", "Min. Current (A)"))
        self.label_max_current.setText(_translate("MainWindow", "Max. Current (A)"))
        self.label_step_size.setText(_translate("MainWindow", "Step Size (A)"))
        self.connect_button.setText(_translate("MainWindow","Connect to Teensy"))
        self.apply_button.setText(_translate("MainWindow","Apply"))
        self.monitor_button.setText(_translate("MainWindow","Monitor"))
        self.port_value.setText(_translate("MainWindow",self.settings.set_value['port']))
        self.rate_value.setText(_translate("MainWindow",self.settings.set_value['rate']))
        self.value_min_current.setText(_translate("MainWindow",self.settings.set_value['min_current']))
        self.value_max_current.setText(_translate("MainWindow",self.settings.set_value['max_current']))
        self.value_step_size.setText(_translate("MainWindow",self.settings.set_value['step_size']))

    def pcb_panel(self):
        self.box_pcb = QtWidgets.QGroupBox(self.centralwidget)
        self.box_pcb.setObjectName("box_pcb")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.box_pcb)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.set_label = QtWidgets.QLabel()
        self.set_label.setMinimumSize(QtCore.QSize(100, 20))
        self.set_label.setMaximumSize(QtCore.QSize(100, 20))
        self.set_label.setObjectName("set_label")
        self.gridLayout_2.addWidget(self.set_label, 1, 0, 1, 2)
        self.monitor_label = QtWidgets.QLabel()
        self.monitor_label.setMinimumSize(QtCore.QSize(100, 20))
        self.monitor_label.setMaximumSize(QtCore.QSize(100, 20))
        self.monitor_label.setObjectName("monitor_label")
        self.gridLayout_2.addWidget(self.monitor_label, 3, 0, 1, 2)

        self.button_common_up = QtWidgets.QToolButton()
        self.button_common_up.setMinimumSize(QtCore.QSize(40, 20))
        self.button_common_up.setMaximumSize(QtCore.QSize(40, 20))
        self.gridLayout_2.addWidget(self.button_common_up, 2, 0, 1, 1)
        self.button_common_down = QtWidgets.QToolButton()
        self.button_common_down.setMinimumSize(QtCore.QSize(40, 20))
        self.button_common_down.setMaximumSize(QtCore.QSize(40, 20))
        self.gridLayout_2.addWidget(self.button_common_down, 2, 1, 1, 1)


        self.board_label = []
        self.set_value = []
        self.monitor_value = []
        self.button_up = []
        self.button_down = []
        self.combobox_common_increase = []

        for i in range(self.settings.num_pcb):


            self.board_label.append(QtWidgets.QLineEdit())
            self.board_label[i].setMinimumSize(QtCore.QSize(105, 20))
            self.board_label[i].setMaximumSize(QtCore.QSize(105, 20))
            self.gridLayout_2.addWidget(self.board_label[i], 0, 3*i+2, 1, 3)


            self.set_value.append(QtWidgets.QLineEdit())
            self.set_value[i].setMinimumSize(QtCore.QSize(105, 20))
            self.set_value[i].setMaximumSize(QtCore.QSize(105, 20))
            self.gridLayout_2.addWidget(self.set_value[i], 1, 3*i+2, 1, 3)

            self.combobox_common_increase.append(QtWidgets.QComboBox())
            self.combobox_common_increase[i].addItem("N/A")
            self.combobox_common_increase[i].addItem("+")
            self.combobox_common_increase[i].addItem("-")
            self.combobox_common_increase[i].setMinimumSize(QtCore.QSize(40, 20))
            self.combobox_common_increase[i].setMaximumSize(QtCore.QSize(40, 20))
            self.gridLayout_2.addWidget(self.combobox_common_increase[i], 2, 3*i+2, 1, 1)
            self.button_up.append(QtWidgets.QToolButton())
            self.button_up[i].setMinimumSize(QtCore.QSize(20, 20))
            self.button_up[i].setMaximumSize(QtCore.QSize(20, 20))
            self.gridLayout_2.addWidget(self.button_up[i], 2, 3*i+3, 1, 1)
            self.button_down.append(QtWidgets.QToolButton())
            self.button_down[i].setMinimumSize(QtCore.QSize(20, 20))
            self.button_down[i].setMaximumSize(QtCore.QSize(20, 20))
            self.gridLayout_2.addWidget(self.button_down[i], 2, 3*i+4, 1, 1)

            self.monitor_value.append(QtWidgets.QLineEdit())
            self.monitor_value[i].setMinimumSize(QtCore.QSize(105, 20))
            self.monitor_value[i].setMaximumSize(QtCore.QSize(105, 20))
            self.gridLayout_2.addWidget(self.monitor_value[i], 3, 3*i+2, 1, 3)

        self.gridLayout_0.addWidget(self.box_pcb, 2, 0, 1, 2)

        _translate = QtCore.QCoreApplication.translate
        self.set_label.setText(_translate("MainWindow", "Set Current (A)"))
        self.monitor_label.setText(_translate("MainWindow", "Monitor Current (A)"))
        self.button_common_up.setText(_translate("MainWindow", u'\u2191'))
        self.button_common_down.setText(_translate("MainWindow", u'\u2193'))
        for i in range(self.settings.num_pcb):
            self.board_label[i].setText(_translate("MainWindow",self.settings.set_value['name_' + str(i)]))
            self.set_value[i].setText(_translate("MainWindow",self.settings.set_value['pcb_' + str(i)]))
            self.button_up[i].setText(_translate("MainWindow",u'\u2191'))
            self.button_down[i].setText(_translate("MainWindow",u'\u2193'))

    def step_increase_panel(self):
        self.box_step_increase = QtWidgets.QGroupBox(self.centralwidget)
        self.box_step_increase.setObjectName("box_step_increase")
        self.gridLayout_step_increase = QtWidgets.QGridLayout(self.box_step_increase)
        self.gridLayout_step_increase.setObjectName("gridLayout_step_increase")

        self.label_step_size = QtWidgets.QLabel()
        self.label_step_size.setMinimumSize(QtCore.QSize(80, 20))
        self.label_step_size.setMaximumSize(QtCore.QSize(80, 20))
        self.label_step_size.setObjectName("label_step_size")
        self.gridLayout_step_increase.addWidget(self.label_step_size, 0, 0, 1, 1)
        self.value_step_size = QtWidgets.QLineEdit()
        self.value_step_size.setMinimumSize(QtCore.QSize(80, 20))
        self.value_step_size.setMaximumSize(QtCore.QSize(80, 20))
        self.gridLayout_step_increase.addWidget(self.value_step_size, 0, 1, 1, 1)

        self.button_up = QtWidgets.QToolButton()
        self.button_up.setMinimumSize(QtCore.QSize(40, 20))
        self.button_up.setMaximumSize(QtCore.QSize(40, 20))
        self.gridLayout_step_increase.addWidget(self.button_up, 0, 2, 1, 1)
        self.button_down = QtWidgets.QToolButton()
        self.button_down.setMinimumSize(QtCore.QSize(40, 20))
        self.button_down.setMaximumSize(QtCore.QSize(40, 20))
        self.gridLayout_step_increase.addWidget(self.button_down, 0, 3, 1, 1)

        self.gridLayout_0.addWidget(self.box_step_increase, 3, 0, 1, 2)

        _translate = QtCore.QCoreApplication.translate
        self.dA_label.setText(_translate("MainWindow", "Step Size (A)"))
        self.dA_value.setText(_translate("MainWindow",self.settings.set_value['step_size']))

    def file_panel(self):
        # Open & Save
        self.box_file = QtWidgets.QGroupBox(self.centralwidget)
        self.box_file.setObjectName("box_file")
        self.gridLayout_file = QtWidgets.QGridLayout(self.box_file)
        self.gridLayout_file.setObjectName("gridLayout_file")

        self.open = QtWidgets.QLineEdit()
        self.open.setMinimumSize(QtCore.QSize(300, 20))
        self.open.setMaximumSize(QtCore.QSize(300, 20))
        self.open.setObjectName("open")
        self.gridLayout_file.addWidget(self.open, 0, 0, 1, 1)

        self.button_open = QtWidgets.QPushButton()
        self.button_open.setMinimumSize(QtCore.QSize(60, 20))
        self.button_open.setMaximumSize(QtCore.QSize(60, 20))
        self.button_open.setObjectName("button_open")
        self.gridLayout_file.addWidget(self.button_open, 0, 1, 1, 1)
        self.save = QtWidgets.QLineEdit()
        self.save.setMinimumSize(QtCore.QSize(300, 20))
        self.save.setMaximumSize(QtCore.QSize(300, 20))
        self.save.setObjectName("save")
        self.gridLayout_file.addWidget(self.save, 1, 0, 1, 1)
        self.button_save = QtWidgets.QPushButton()
        self.button_save.setMinimumSize(QtCore.QSize(60, 20))
        self.button_save.setMaximumSize(QtCore.QSize(60, 20))
        self.button_save.setObjectName("button_save")
        self.gridLayout_file.addWidget(self.button_save, 1, 1, 1, 1)

        self.gridLayout_0.addWidget(self.box_file, 3, 0, 1, 1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Current Control"))

        self.box_file.setTitle(_translate("MainWindow", "Open and Save"))
        self.button_open.setText(_translate("MainWindow", "Open"))
        self.button_save.setText(_translate("MainWindow", "Save"))
