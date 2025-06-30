"""
Written by Ahreum Lee in 2022

current controller
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import qdarkstyle

import serial
import time

import Setting
import GUI

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class makeWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """
        Make the main window
            with layout defined in GUI.py
            and experimental specs defined in current_set_value.csv
        """
        super().__init__()

        self.settings = Setting.Setting(self)

        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self, self.settings)


        self.initUi()

    def draw_pcb_panel(self):

        self.ui.pcb_panel()
        self.fill_set_value()

        self.ui.button_common_up.clicked.connect(self.on_common_up)
        self.ui.button_common_down.clicked.connect(self.on_common_down)
        for i in range(self.settings.num_pcb):
            self.ui.button_up[i].clicked.connect(lambda state, x=i: self.on_up(x))
            self.ui.button_down[i].clicked.connect(lambda state, x=i: self.on_down(x))


        self.ui.button_common_up.setEnabled(True)
        self.ui.button_common_down.setEnabled(True)
        for i in range(self.settings.num_pcb):
            self.ui.button_up[i].setEnabled(True)
            self.ui.button_down[i].setEnabled(True)

    def initUi(self):
        self.draw_pcb_panel()
        # Set text
        self.fill_set_value()
        self.ui.open.setText(self.settings.file_name)
        self.ui.save.setText(self.settings.save_as)

        # Connect UI elements to GUI_functions
        self.ui.connect_button.clicked.connect(self.on_connect_to_teensy)
        self.ui.apply_button.clicked.connect(self.on_apply)
        self.ui.monitor_button.clicked.connect(self.on_monitor)
        self.ui.button_open.clicked.connect(self.on_open)
        self.ui.button_save.clicked.connect(self.on_save)


        self.ui.apply_button.setEnabled(False)
        self.ui.monitor_button.setEnabled(False)

    def on_connect_to_teensy(self):

        self.settings.update_set_value()

        self.teensy = serial.Serial(self.settings.set_value['port'],int(self.settings.set_value['rate']))

        print("Connecting to teensy with ...")
        print("\t port: ", self.settings.set_value['port'])
        print("\t baud rate: ", self.settings.set_value['rate'])


        self.ui.port_value.setEnabled(False)
        self.ui.rate_value.setEnabled(False)

        self.ui.apply_button.setEnabled(True)
        self.ui.button_common_up.setEnabled(True)
        self.ui.button_common_down.setEnabled(True)
        for i in range(self.settings.num_pcb):
            self.ui.button_up[i].setEnabled(True)
            self.ui.button_down[i].setEnabled(True)
        """ below function is not implemented yet, so I disabled the button """
        # self.ui.monitor_button.setEnabled(True)


    def on_common_up(self):

        # Read settings from the screen
        self.settings.set_value['step_size'] = self.ui.value_step_size.text()
        self.settings.set_value['min_current'] = self.ui.value_min_current.text()
        self.settings.set_value['max_current'] = self.ui.value_max_current.text()

        stepSize = float(self.settings.set_value['step_size'])
        minCurrent = float(self.settings.set_value['min_current'])
        maxCurrent = float(self.settings.set_value['max_current'])

        # Update the screen
        for i in range(self.settings.num_pcb):
            if self.ui.combobox_common_increase[i].currentText() == '+':
                newValue = float(self.ui.set_value[i].text()) + stepSize
                if newValue <= minCurrent:
                    newValue = minCurrent
                elif newValue >= maxCurrent:
                    newValue = maxCurrent
                self.ui.set_value[i].setText("{:1.2f}".format(newValue))
            elif self.ui.combobox_common_increase[i].currentText() == '-':
                newValue = float(self.ui.set_value[i].text()) - stepSize
                if newValue <= minCurrent:
                    newValue = minCurrent
                elif newValue >= maxCurrent:
                    newValue = maxCurrent
                self.ui.set_value[i].setText("{:1.2f}".format(newValue))

        # Connect to microcontroller and upload the new values
        self.on_apply()

    def on_common_down(self):

        # Read settings from the screen
        self.settings.set_value['step_size'] = self.ui.value_step_size.text()
        self.settings.set_value['min_current'] = self.ui.value_min_current.text()
        self.settings.set_value['max_current'] = self.ui.value_max_current.text()

        stepSize = float(self.settings.set_value['step_size'])
        minCurrent = float(self.settings.set_value['min_current'])
        maxCurrent = float(self.settings.set_value['max_current'])

        # Update the screen
        for i in range(self.settings.num_pcb):
            if self.ui.combobox_common_increase[i].currentText() == '+':
                newValue = float(self.ui.set_value[i].text()) - stepSize
                if newValue <= minCurrent:
                    newValue = minCurrent
                elif newValue >= maxCurrent:
                    newValue = maxCurrent
                self.ui.set_value[i].setText("{:1.2f}".format(newValue))
            elif self.ui.combobox_common_increase[i].currentText() == '-':
                newValue = float(self.ui.set_value[i].text()) + stepSize
                if newValue <= minCurrent:
                    newValue = minCurrent
                elif newValue >= maxCurrent:
                    newValue = maxCurrent
                self.ui.set_value[i].setText("{:1.2f}".format(newValue))

        # Connect to microcontroller and upload the new values
        self.on_apply()

    def on_up(self, idx):
        print("up button for ", idx, "-th out")
        # Read settings from the screen
        self.settings.set_value['step_size'] = self.ui.value_step_size.text()
        self.settings.set_value['min_current'] = self.ui.value_min_current.text()
        self.settings.set_value['max_current'] = self.ui.value_max_current.text()

        stepSize = float(self.settings.set_value['step_size'])
        minCurrent = float(self.settings.set_value['min_current'])
        maxCurrent = float(self.settings.set_value['max_current'])

        # Update the screen
        newValue = float(self.ui.set_value[idx].text()) + stepSize
        if newValue <= minCurrent:
            newValue = minCurrent
        elif newValue >= maxCurrent:
            newValue = maxCurrent
        self.ui.set_value[idx].setText("{:1.2f}".format(newValue))

        # Connect to microcontroller and upload the new values
        self.on_apply()

    def on_down(self, i):

        # Read settings from the screen
        self.settings.set_value['step_size'] = self.ui.value_step_size.text()
        self.settings.set_value['min_current'] = self.ui.value_min_current.text()
        self.settings.set_value['max_current'] = self.ui.value_max_current.text()

        stepSize = float(self.settings.set_value['step_size'])
        minCurrent = float(self.settings.set_value['min_current'])
        maxCurrent = float(self.settings.set_value['max_current'])

        # Update the screen
        newValue = float(self.ui.set_value[i].text()) - stepSize
        if newValue <= minCurrent:
            newValue = minCurrent
        elif newValue >= maxCurrent:
            newValue = maxCurrent
        self.ui.set_value[i].setText("{:1.2f}".format(newValue))

        # Connect to microcontroller and upload the new values
        self.on_apply()

    def fill_set_value(self):
        """
        Fill the set values for the pcb boards
        """
        for i in range(self.settings.num_pcb):
            self.ui.set_value[i].setText(self.settings.set_value['pcb_' + str(i)])

    def on_apply(self):
        print("[main.on_apply]")

        # Update self.settings.set_value with the GUI values.
        self.settings.update_set_value()

        self.ui.apply_button.setEnabled(False)
        # self.ui.monitor_button.setEnabled(False)

        var = ''
        for i in range(self.settings.num_pcb):
            var += self.settings.set_value['pcb_' + str(i)]
            if i < self.settings.num_pcb - 1:
                var += " "

        print("[", var, "]")
        var = var.encode('utf-8')
        self.teensy.write(var)
        time.sleep(0.1) # is it really needed?

        self.ui.apply_button.setEnabled(True)
        # self.ui.monitor_button.setEnabled(True)


    def on_monitor(self):
        print("[main.on_apply]")

        # Update self.settings.set_value with the GUI values.
        self.settings.update_set_value()

        self.ui.apply_button.setEnabled(False)
        self.ui.monitor_button.setEnabled(False)

        self.ui.apply_button.setEnabled(True)
        self.ui.monitor_button.setEnabled(True)


    def on_open(self):
        # Remove previous PCI6733 and DDS control panels
        self.ui.gridLayout_0.removeWidget(self.ui.box_pcb)
        self.ui.box_pcb.deleteLater()
        self.ui.box_pcb = None

        # Read the open filename and read it
        self.settings.file_name = self.ui.open.text()
        if self.settings.file_name == '':
            self.settings.file_name = 'current_set_value.csv' # if nothing then set as default file
        self.settings.read_set_value()

        # Create new PCI6733 and DDS control panels
        self.ui.settings = self.settings
        self.draw_pcb_panel()

        print("[main.on_open] open file: " + self.settings.file_name)

    def on_save(self):
        # Read the save filename
        self.settings.save_as = self.ui.save.text()

        # Update self.settings.set_value with the GUI values.
        self.settings.update_set_value()

        # Write the self.settings.set_value to the self.settings.save_as
        self.settings.record_set_value_and_check_errors()

        print("[main.on_save] save file: " + self.settings.save_as)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    application = makeWindow()
    application.show()
    sys.exit(app.exec())
