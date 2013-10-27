# -*- coding: utf-8 -*-

__all__ = ['FaderWidget']

from projectVFX_Global import *

class FaderWidget(QtGui.QWidget):
    """
    FaderWidget(QtGui.QWidget)

    Fades between two widgets.
    Animation begins immediately after instantiation,
    and the FaderWidget deletes itself upon completion.

    QWidget old_widget  - the starting widget
    QWidget new_widget  - the ending widget
    int     duration    - fade time in milliseconds
    bool    reverse     - do fade backwards
    """
    def __init__(self, old_widget, new_widget=None, duration=500, reverse=False):

        QtGui.QWidget.__init__(self, new_widget)

        self.resize(old_widget.size())

        self.old_pixmap = QtGui.QPixmap(old_widget.size())
        old_widget.render(self.old_pixmap)

        self.pixmap_opacity = 1.0

        self.timeline = QtCore.QTimeLine()
        if reverse:
            self.timeline.setDirection(self.timeline.Backward)
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.deleteLater)
        self.timeline.setDuration(duration)

        self.timeline.start()
        self.show()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()

    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.repaint()



class FadeExample(QtGui.QWidget):
    """
    FadeExample(QtGui.QWidget)

    Example widget using a FaderWidget to transition
    between two simple colored QWidgets in a stack layout.
    """
    def __init__(self):
        super(FadeExample, self).__init__()

        self.resize(600,600)
        self.vlayout = QtGui.QVBoxLayout(self)

        self.w1 = QtGui.QWidget()
        self.w1.setStyleSheet("QWidget {background-color: red;}")

        self.w2 = QtGui.QWidget()
        self.w2.setStyleSheet("QWidget {background-color: blue;}")

        self.stacked = QtGui.QStackedLayout()
        self.stacked.addWidget(self.w1)
        self.stacked.addWidget(self.w2)

        self.vlayout.addLayout(self.stacked)

        self.fadeButton = QtGui.QPushButton("Fade")
        self.resetButton = QtGui.QPushButton("Reset")

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.fadeButton)
        buttonLayout.addWidget(self.resetButton)

        self.vlayout.addLayout(buttonLayout)

        self.fadeButton.clicked.connect(self.fade)
        self.resetButton.clicked.connect(self.reset)

    def fade(self):
        FaderWidget(self.w1, self.w2)

        self.stacked.setCurrentWidget(self.w2)
    def reset(self):

        self.stacked.setCurrentWidget(self.w1)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    aFadeExample = FadeExample()
    aFadeExample.show()

    app.exec_()
