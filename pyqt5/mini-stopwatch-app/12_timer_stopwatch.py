import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

from datetime import datetime

# Screen resolution
res_W = 1920
res_H = 1080
win_W = 800
win_H = 500
res_WH = res_W // 2
res_HH = res_H // 2
win_pos_W = res_WH - (win_W // 2)
win_pos_H = res_HH - (win_H // 2)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows clock Using Timer")
        # self.setGeometry(250,150,350,350)
        self.setGeometry(win_pos_W, win_pos_H, win_W, win_H)

        self.UI()

    def UI(self):
        # --------------------------------------
        # --- create buttons widget - layout ---
        self.button_widgets = QWidget()
        button_layout = QHBoxLayout(self.button_widgets)

        # self.colorLabel=QLabel(self)
        # self.colorLabel.resize(250,250)
        # self.colorLabel.setStyleSheet("background-color:green")
        # self.colorLabel.move(40,20)

        ###################### Buttons ##################
        btnStart=QPushButton("Start",self)
        btnStart.move(80,300)
        btnStart.clicked.connect(self.start)

        btnStop=QPushButton("Stop",self)
        btnStop.move(190,300)
        btnStop.clicked.connect(self.stop)

        # --- button EXIT ---
        btnExitApp = QPushButton("Exit App")
        btnExitApp.move(200,300)
        btnExitApp.clicked.connect(self.exit_app_event)     # connect signal to slot
        btnExitApp.setStyleSheet("background-color : pink") # color of button

        # add buttons to button layout
        button_layout.addWidget(btnStart)
        button_layout.addWidget(btnStop)
        button_layout.addWidget(btnExitApp)

        # ---------------------------
        # --- main central layout ---
        # ---------------------------
        # create central layout
        self.central_widget = QWidget()
        central_layout = QVBoxLayout(self.central_widget) 

        # add other layouts to central layout
        central_layout.addWidget(self.button_widgets)

        # Set the layout on the application's window
        self.setCentralWidget(self.central_widget)

        ################## Timer ########################
        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateClock)
        self.value=0

        self.show()

    def updateClock(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time is :", current_time)

        # if self.value==0:
        #     self.colorLabel.setStyleSheet("background-color:yellow")
        #     self.value=1
        # else:
        #     self.colorLabel.setStyleSheet("background-color:red")
        #     self.value=0
        pass

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

def main():
    App = QApplication(sys.argv)
    window=Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()