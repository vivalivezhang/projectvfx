from projectVFX_Global import *

class timelogCalendar(QtGui.QCalendarWidget):
    def __init__(self, parent = None):
        super(timelogCalendar,self).__init__(parent)
        
        self.setFirstDayOfWeek(Qt.Monday)
        self.setGridVisible(True)
        self.setSelectionMode(QtGui.QCalendarWidget.NoSelection)
        self.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        
        datformat = QtGui.QTextCharFormat()
        datformat.setForeground(QtGui.QColor(200,200,200))
        self.setWeekdayTextFormat(Qt.Monday, datformat)
        self.setWeekdayTextFormat(Qt.Tuesday, datformat)
        self.setWeekdayTextFormat(Qt.Wednesday, datformat)
        self.setWeekdayTextFormat(Qt.Thursday, datformat)
        self.setWeekdayTextFormat(Qt.Friday, datformat)
        
        endformat = QtGui.QTextCharFormat()
        endformat.setForeground(QtGui.QColor(200,200,200))
        self.setWeekdayTextFormat(Qt.Saturday, endformat)
        self.setWeekdayTextFormat(Qt.Sunday, endformat)
        