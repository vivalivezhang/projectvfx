# -*- coding: utf-8 -*-
from projectVFX_Global import *
from appEnvCalc import appEnvCalc



class appListView(QtGui.QListView):
    execed = QtCore.Signal()
    def __init__(self, parent = None):
        super(appListView, self).__init__(parent)


        self.setViewMode(QtGui.QListView.IconMode)
        self.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.setMovement(QtGui.QListView.Static)
        self.setGridSize(QtCore.QSize(90,90))
        self.setResizeMode(QtGui.QListView.Adjust)
        self.setTextElideMode(Qt.ElideNone)
        self.setIconSize(QtCore.QSize(50,50))
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.setFocusPolicy(Qt.NoFocus)

        self.__RightButtonselectedIndex = None

        self.createActions()
        self.createRightButtonMenu()

    #def mousePressEvent(self, e):
    #    if e.button() == Qt.RightButton:
    #        index = self.indexAt(e.pos())
    #        if index.isValid():
    #            self.RightButtonMenu.move(self.cursor().pos())
    #            self.RightButtonMenu.show()
    #            return
    #    super(appListView, self).mousePressEvent(e)

    #def mouseReleaseEvent(self, e):
    #    if e.button() == Qt.RightButton:
    #        index = self.indexAt(e.pos())
    #        if index.isValid():
    #            log_(e.type())


    def mouseDoubleClickEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            index = self.indexAt(e.pos())
            if index.isValid():
                self.execApp(index)
                return

        super(appListView, self).mouseDoubleClickEvent(e)


    def contextMenuEvent(self, reason):
        index = self.indexAt(reason.pos())
        if index.isValid():
            self.__RightButtonselectedIndex = index
            self.RightButtonMenu.move(self.mapToGlobal(reason.pos()))
            self.RightButtonMenu.show()
            return
        super(appListView, self).contextMenuEvent(reason)

    def execApp(self, index = None):
        if not index:
            index = self.__RightButtonselectedIndex
        execFile = self.model().getAppExec(index)

        sttingEnvs = self.model().getAppEnv(index) + self.model().getGEnv()
        #log_(sttingEnv)




        #sttingEnv['NUKE_PATH'] = '/All/Oxygen/util/nuke/7.0_test:/All/Oxygen/cpp/eclipse_test/ndk_test_1/so'
        finalEnv = appEnvCalc(sttingEnvs).getResult()

        log_(finalEnv['NUKE_PATH'])
        #log_(finalEnv)

        try:
            # exec! #
            subprocess.Popen(execFile, env = finalEnv,)#shell = True)#(SYS_TYPE_ not in ('win', 'mac') ) )
            self.execed.emit()
        except Exception, error:
            QtGui.QMessageBox.critical(self, 'error', str(error).decode('UTF8'))




    def createActions(self, ):
        self.execAction = QtGui.QAction("Exec", self,)
        self.settingAction = QtGui.QAction("Setting", self,)

        self.execAction.triggered.connect(self.execApp)
        self.settingAction.triggered.connect(self.settingApp)

    def createRightButtonMenu(self, ):
        self.RightButtonMenu = QtGui.QMenu(self)

        self.RightButtonMenu.addAction(self.execAction)
        self.RightButtonMenu.addSeparator()
        self.RightButtonMenu.addAction(self.settingAction)



    def settingApp(self):

        index = self.__RightButtonselectedIndex
        log_(index.row())
