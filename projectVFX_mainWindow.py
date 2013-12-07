# -*- coding: utf-8 -*-

from projectVFX_Global import *

from UI.mainWindowUI import Ui_mainWindowPVFX
from UI.preferencesUI import Ui_preferencesPVFX

from lib.appListModel import appListModel
from lib.appListView import appListView

from lib.appSetting import appSetting


SETTING_FILE = QtCore.QSettings(os.path.expanduser("~/.ProjectVFX/ProjectVFX_preferences.ini") ,
                                                         QtCore.QSettings.IniFormat)
#SETTING_FILE.setIniCodec('UTF-8')

APP_SETTING_PATH = (opj(BASE_PATH_F_, 'COM/gene/ple/projectvfx', 'db', 'app_setting'))



class projectVFX_mainWindow(QtGui.QMainWindow, Ui_mainWindowPVFX):
    def __init__(self,parent = None):
        super(projectVFX_mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createInitCode()


        self.createFramework()

        # init codeload #
        self.setPjCodeInit()
        self.setPipeline()
        self.setSW()
        self.setGene()

        self.createActions()
        self.createTrayIcon()


        self.createTabWigetFader()
        self.setIconInit()


        self.setWidgetInit()
        self.readSettings()
        #for i in range(1,99999):
        #    log_(i)
        time.sleep(1)
    def createInitCode(self, ):
        self.listViewPipeline_model = appListModel(self)
        self.listViewSW_model = appListModel(self)


    def setWidgetInit(self, ):
        self.splitterPipeline.setSizes([self.size().height()*2/9, self.size().height()*7/9])
        self.splitterCentral.setSizes([self.size().width()*1/6, self.size().width()*5/6])
        self.splitterApp.setSizes([self.size().height()*1/2, self.size().height()*1/2])
        #self.splitter.set

        self.gridLayoutPipeline.addWidget(self.listViewPipeline)


        self.listViewPj.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.listViewPj.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.listViewPj.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listViewPj.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        self.gridLayoutSW.addWidget(self.listViewSW)



        self.actionAbout.triggered.connect(self.on_actionAbout_triggered_event)
        self.actionPre.triggered.connect(self.on_actionPre_triggered_event)
        self.actionQuit.triggered.connect(self.on_Quit_evnet)

        #
        self.listViewPj.selectionModel().selectionChanged.connect(self.on_listViewPj_selectionChanged_event)

        self.pushButton.clicked.connect(self.showTrayMessage)
        
        self.listViewSW.execed.connect(self.hideThis)

        self.setLocale(QtCore.QLocale('UnitedStates'))
        self.setWindowTitle('projectVFX')
        self.move((QtGui.QApplication.desktop().width() - self.width())/2,
            (QtGui.QApplication.desktop().height() - self.height())/2)

    def createFramework(self, ):
        self.listViewPipeline = appListView()
        self.listViewSW = appListView()
        self.widgetPreferences = projectVFX_preferences()

        self.listViewPipeline.setModel(self.listViewPipeline_model)
        self.listViewSW.setModel(self.listViewSW_model)


    def createActions(self):


        #self.maximizeAction = QtGui.QAction("Ma&ximize", self,
        #        triggered=self.showMaximized)


        self.restoreAction = QtGui.QAction("&Restore", self,
                triggered=self.showNormal)
        self.minimizeAction = QtGui.QAction("Mi&nimize", self,
                triggered=self.close)
        self.quitAction = QtGui.QAction("&Quit", self,
                triggered=self.on_Quit_evnet)


    def createTrayIcon(self):
        self.trayIconMenu = QtGui.QMenu(self)

        #self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        self.trayIcon.activated.connect(self.on_trayIcon_activated_event)
        self.trayIcon.messageClicked.connect(self.on_trayIcon_messageClicked_event)

    def createTabWigetFader(self ):
        self.tabWidgetCurrentIndex = self.tabWidgetApp.currentWidget()
        self.tabWidgetApp.currentChanged.connect(self.on_tabWidget_currentChanged_event )


    def setVisible(self, visible):
        self.minimizeAction.setEnabled(visible)
        #self.maximizeAction.setEnabled(not self.isMaximized())
        self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(projectVFX_mainWindow, self).setVisible(visible)


    def closeEvent(self, event):
        self.hideThis()
        event.ignore()
            
    def hideThis(self, ):
        if self.trayIcon.isVisible():
            #QtGui.QMessageBox.information(self, "Systray",
            #        "The program will keep running in the system tray. To "
            #        "terminate the program, choose <b>Quit</b> in the "
            #        "context menu of the system tray entry.")
            self.writeSettings()
            self.hide()
    

    def showEvent(self, event):
        self.readSettings()
        super(projectVFX_mainWindow,self).showEvent(event)


    def showTrayMessage(self,a ,title = 'Message', text = 'Text', icon = 1, duration = 10000):
        self.trayIcon.showMessage( title, text, icon, duration )

    def setIconInit(self, index = 0):
        #icon = self.iconComboBox.itemIcon(index)
        icon = QtGui.QIcon(':/images/vfx.png')
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

        #self.trayIcon.setToolTip(self.iconComboBox.itemText(index))
        self.trayIcon.setToolTip('projectVFX %s' % version_)
        self.trayIcon.show()

    def setPjCodeInit(self, ):
        searchprocpath = QtCore.QDir(BASE_PATH_F_).entryList(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Dirs)
        pj_code = searchprocpath
        pj_code.sort()
        pj_code.insert(0, '')

        self.listViewPj_model = QtGui.QStringListModel(self)
        self.listViewPj_model.setStringList(pj_code)

        self.listViewPj.setModel(self.listViewPj_model)
        self.listViewPj.setCurrentIndex(self.listViewPj_model.index(0))


    def setSW(self, show = ''):
        if not os.path.isdir(APP_SETTING_PATH):
            return False
        showfile = opj(APP_SETTING_PATH, show, 'app_%s.xml' % SYS_TYPE_)
        if (not os.path.isfile(showfile)) or (not show):
            showfile = opj(APP_SETTING_PATH, 'app_%s.xml' % SYS_TYPE_)

        sw_code = self.getXmlCode(showfile)

        self.listViewSW_model.setApps(sw_code)

    def setPipeline(self, ):
        if not os.path.isdir(APP_SETTING_PATH):
            return False
        showfile = opj(APP_SETTING_PATH, 'pipe_%s.xml' % SYS_TYPE_)

        sw_code = self.getXmlCode(showfile)

        self.listViewPipeline_model.setApps(sw_code)
    def setGene(self, ):
        pass

    def getXmlCode(self, f):
        setting = appSetting()
        setting.readXML(f)
        sw_code = setting.getSetting()
        return sw_code


    def on_trayIcon_activated_event(self, reason):
        if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
            if self.isHidden():
                self.showNormal()

            elif not self.isHidden():
                self.close()
            return
        elif reason == QtGui.QSystemTrayIcon.MiddleClick:
            pass


    def on_trayIcon_messageClicked_event(self):
        log_('on_trayIcon_messageClicked_event')


    def on_actionAbout_triggered_event(self):
        QtGui.QMessageBox.about(self, 'About', '<h3>ProjectVFX</h3> <br/> \
                                Release Version<br/> \
                                 %s <br/> \
                                Pipeline ToolKit \
                                <hr/> \
                                Developer:<font color=#7272ea> <u>张凯华 Viva Zhang<br/> \
                                vivalivezhang@gmail.com&gt;</u></font>'.decode('UTF8') % (version_))

    def on_actionPre_triggered_event(self, ):
        self.widgetPreferences.move( QtGui.QCursor().pos() )
        self.widgetPreferences.show()

    def on_Quit_evnet(self, ):
        self.writeSettings()
        QtGui.qApp.quit()

    def on_listViewPj_selectionChanged_event(self, index):
        show = self.listViewPj_model.data(index.indexes()[0] ,Qt.DisplayRole).toString()
        log_(show )
        self.setSW(show)
        self.listViewPipeline_model.setShow(show )
        self.listViewSW_model.setShow(show )

    def on_tabWidget_currentChanged_event(self,idx):
        from lib.fader import FaderWidget
        FaderWidget(self.tabWidgetApp.widget(self.tabWidgetApp.indexOf(self.tabWidgetCurrentIndex) ),
                    self.tabWidgetApp.widget(idx))
        self.tabWidgetCurrentIndex = self.tabWidgetApp.currentWidget()

    def writeSettings(self):
        '''
        try:
            SETTING_FILE.beginGroup('mainWindow')
            SETTING_FILE.setValue('geometry', self.saveGeometry() )
            SETTING_FILE.setValue('state', self.saveState() )
            SETTING_FILE.setValue('splitterPipeline', self.splitterPipeline.saveState() )
            SETTING_FILE.setValue('splitterCentral', self.splitterCentral.saveState())
            SETTING_FILE.setValue('splitterApp', self.splitterApp.saveState())
            SETTING_FILE.setValue('listViewPjIndex', self.listViewPj.currentIndex().data() )
            SETTING_FILE.endGroup()
        except Exception, e:
            log_(e)
        '''


    def readSettings(self):
        '''
        try:
            SETTING_FILE.beginGroup('mainWindow')
            self.restoreGeometry(SETTING_FILE.value('geometry').toByteArray() )
            self.restoreState(SETTING_FILE.value('state').toByteArray() )
            self.splitterPipeline.restoreState(SETTING_FILE.value('splitterPipeline').toByteArray())
            self.splitterCentral.restoreState(SETTING_FILE.value('splitterCentral').toByteArray())
            self.splitterApp.restoreState(SETTING_FILE.value('splitterApp').toByteArray())
            self.listViewPj.setCurrentIndex(self.listViewPj_model.index(
                self.listViewPj_model.stringList().index(SETTING_FILE.value('listViewPjIndex').toByteArray())) )
            SETTING_FILE.endGroup()
        except Exception, e:
            log_(e)
        '''







class projectVFX_preferences(QtGui.QWidget, Ui_preferencesPVFX):
    def __init__(self, parent = None):
        super(projectVFX_preferences,self).__init__(parent)
        self.setupUi(self)

        self.setWidgetInit()

    def setWidgetInit(self, ):
        self.setWindowIcon(QtGui.QIcon(':/images/vfx.png'))

        self.pushButtonClose.clicked.connect(self.close)
        self.pushButtonRevert.clicked.connect(self.on_pushButtonRevert_clicked_event)
        self.pushButtonSave.clicked.connect(self.on_pushButtonSave_clicked_event)

    def on_pushButtonRevert_clicked_event(self, ):
        log_(self.parent())

    def on_pushButtonSave_clicked_event(self, ):
        pass


#class projectVFX_listViewPipeline(QtGui.QListView):
#    def __init__(self, parent = None):
#        super(projectVFX_listViewPipeline,self).__init__(parent)


def main():

    app = QtGui.QApplication(sys.argv)
    app.setStyle('plastique')
    app.setStyleSheet(lib.darkorangeStylesheet.getStyleSheet())
    app.setFont(QtGui.QFont("DejaVu LGC Sans", 10))
    ######################################################
    shareMem = QtCore.QSharedMemory("ProjectVFX_SingleInstanceIdentify")

    for i in range(2):
        if (shareMem.attach(QtCore.QSharedMemory.ReadOnly)):
            shareMem.detach()

    if not (shareMem.create(1)):
        QtGui.QMessageBox.warning(None,'ProjectVFX','ProjectVFX is runing')
        return(app.quit())

    ######################################################
    try:

        splash = QtGui.QSplashScreen()
        iconPixmap = QtGui.QPixmap(':/images/vfxSplash.png')
        splash.setPixmap( iconPixmap )

        splash.show()
        splash.raise_()

        splash.showMessage(('projectVFX %s' % version_), Qt.AlignLeft | Qt.AlignBottom, Qt.white)



        #if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        #    QtGui.QMessageBox.critical(None, "Systray",
        #            "Couldn't detect any system tray on this system.")
        #    sys.exit(1)

        QtGui.QApplication.setQuitOnLastWindowClosed(False)


        window = projectVFX_mainWindow()

        window.show()
        window.raise_()

        splash.finish(window)
        del splash


        sys.exit(app.exec_())
        ######################################
        if (shareMem.isAttached()):
            shareMem.detach()
        del shareMem

    except Exception,e:
        print str(e)
        #QtGui.QMessageBox.critical(None, 'Error', str(e).decode('UTF8'))
        log_(e)


if __name__ == '__main__':
    main()
