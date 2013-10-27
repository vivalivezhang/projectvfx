# -*- coding: utf-8 -*-

from projectVFX_Global import *

from lib_timelog.timelogCalendar import timelogCalendar

from UI_timelog.mainWindowUI import Ui_MainWindowTimelog

def getQDate(*args):
    if args:
        return QtCore.QDate(int(args[0]), int(args[1]), int(args[2]))
    return QtCore.QDate(int(time.strftime('%Y')), int(time.strftime('%m')), int(time.strftime('%d')))


class Timelog_mainWindow(QtGui.QMainWindow, Ui_MainWindowTimelog):
    def __init__(self, parent = None):
        super(Timelog_mainWindow,self).__init__(parent)
        self.setupUi(self)

        self.createFramework()

        self.setWidgetInit()

    def createFramework(self, ):
        self.timelogCalendar = timelogCalendar()
        self.setCentralWidget(self.timelogCalendar)


    def setWidgetInit(self, ):
        self.setLocale(QtCore.QLocale('UnitedStates'))

        self.actionLogToday.triggered.connect(self.logTimeToday)
        self.actionLogYesterday.triggered.connect(self.logTimeYesterday)
        
        self.actionGotoToday.triggered.connect(self.gotoDay)
        
    def gotoDay(self, n, day = getQDate()):
        self.timelogCalendar.setSelectedDate(day)
    

    def logTimeToday(self, ):
        self.logTime()
    def logTimeYesterday(self, ):
        self.logTime(getQDate().addDays(-1))
    

    def logTime(self, withTime = getQDate()):
        log_(withTime)
    




def mian():
    app = QtGui.QApplication(sys.argv)
    app.setStyle('plastique')
    app.setStyleSheet(lib.darkorangeStylesheet.getStyleSheet())
    app.setFont(QtGui.QFont("DejaVu LGC Sans", 10))

    ######################################################

    window = Timelog_mainWindow()

    window.show()
    window.raise_()

    sys.exit(app.exec_() )



if __name__ == '__main__':
    mian()
