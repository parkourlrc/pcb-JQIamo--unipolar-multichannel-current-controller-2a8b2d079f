import csv
import os
import decimal
from PyQt5 import QtWidgets

class Setting():

    def __init__(self, window):
        self.window = window

        self.num_pcb = 5
        self.set_value = {}

        self.ignore = True # whether to ignore a warning.

        self.file_name = './current_set_value.csv' # this is the default value. Might get changed
        self.save_as = './current_set_value.csv'
        self.auto_path = '' # This will be assigned accordingly in self.read_scan_list()

        self.read_set_value()

    def print_set_value(self):
        # this function prints set_value
        for key, val in sorted(self.set_value.items()):
            print(str(key)+"\t", str(val))

    def update_set_value(self):
        """
        Read from GUI and update self.set_value
        """
        decimal.getcontext().prec = 1

        self.set_value = {}
        self.set_value.update({'port': self.window.ui.port_value.text()})
        self.set_value.update({'rate': self.window.ui.rate_value.text()})
        self.set_value.update({'name_0': self.window.ui.board_label[0].text()})
        self.set_value.update({'name_1': self.window.ui.board_label[1].text()})
        self.set_value.update({'name_2': self.window.ui.board_label[2].text()})
        self.set_value.update({'name_3': self.window.ui.board_label[3].text()})
        self.set_value.update({'name_4': self.window.ui.board_label[4].text()})
        self.set_value.update({'pcb_0': self.window.ui.set_value[0].text()})
        self.set_value.update({'pcb_1': self.window.ui.set_value[1].text()})
        self.set_value.update({'pcb_2': self.window.ui.set_value[2].text()})
        self.set_value.update({'pcb_3': self.window.ui.set_value[3].text()})
        self.set_value.update({'pcb_4': self.window.ui.set_value[4].text()})
        self.set_value.update({'step_size': self.window.ui.value_step_size.text()})
        self.set_value.update({'min_current': self.window.ui.value_min_current.text()})
        self.set_value.update({'max_current': self.window.ui.value_max_current.text()})

        # print("[Settings.update_set_value] settings.set_value is now updated with GUI settings")

    def read_set_value(self):
        """
        This function reads an experimental set_value from self.file_name
        and save them to self.set_value
        """

        if self.file_name == '' or self.file_name == None:
            QtWidgets.QMessageBox.warning(
                self.window,
                "Error",
                "Please designate the file name to be read"
            )
            return
        if not os.path.exists(self.file_name):
            QtWidgets.QMessageBox.warning(
                self.window,
                "Error",
                "The file does not exists"
            )
            return

        self.set_value = {}
        with open(self.file_name) as fp:
            for line in fp:
                line = line.rstrip("\n")
                pair = line.split(',')
                if pair != ['']:
                    self.set_value.update({pair[0]: pair[1]})

        """ update self.num_pcb"""

    def record_set_value(self):
        """
        This function writes the experimental set_value to a csv file.
        If self.save_as is not specified, the default location is 'current_set_value.csv'.
        """
        if self.save_as == '' or self.save_as == None:
            self.save_as = './current_set_value.csv'

        # If there's no such file with the file name, make it.
        directory = os.path.dirname(self.save_as)
        if not os.path.exists(directory) and directory:
            os.makedirs(directory)

        # rescan the folder for existing files before enforcing that the
        # file name can't clash with an existing one.
        detected_files = [x for x in os.listdir(directory) if x.endswith(".csv")]
        # prevent accidental overwriting of previous ini files
        if self.save_as in detected_files:
            error_Response = QtWidgets.QMessageBox.question(
                self.window,
                "Warning",
                "The file already exists. Do you wanna overwrite?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
            if error_Response == QtWidgets.QMessageBox.Yes:
                pass
            else:
                return

        with open(self.save_as, 'w') as f:  # Just use 'w' mode in 3.x
            w = csv.writer(f, dialect = 'excel')
            for k,v in self.set_value.items(): # AL-comment: shouldn't it be self.set_value.items()?
                w.writerow([k,v])
        # print('set_value saved in ' + self.save_as + '.')

    def record_set_value_and_check_errors(self):
        """
        This function writes the experimental set_value to a csv file.
        And check if the rate and the delays make sense.
        If self.save_as is not specified, the default location is 'current_set_value.csv'.
        """

        self.record_set_value()

        # compare delays and sampling rate to see if compatible
        # if delay is less than time resolution then creates popup warning
        time_res = 1/float(self.set_value['rate'])
        for i in range(self.num_pcb):
            if float(self.set_value['pcb_' + str(i)]) < 0:
                print(f"The current set value {self.set_value['pcb_' + str(i)]} should be positive.")
            elif float(self.set_value['pcb_' + str(i)]) > 5:
                print(f"The current set value {self.set_value['pcb_' + str(i)]} should be less than 5 A.")

    def boolean_to_string(self, b):
        if b:
            return 'TRUE'
        else:
            return 'FALSE'

    def string_to_boolean(self, s):
        if s == 'TRUE':
            return True
        else:
            return False
