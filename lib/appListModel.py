# -*- coding: utf-8 -*-
from projectVFX_Global import *

__all__ = ['appListModel']

class appListModel(QtCore.QAbstractListModel):
    def __init__(self, parent = None):
        super(appListModel,self).__init__(parent)
        self.currentShow = 'TST'
        
        self.__apps_name = []
        
    def setShow(self, show):
        self.currentShow = show
    

    def setApps(self, dict_):
        """self.setApps(dict) -> None.
        @return: None.
        """
        self.__apps = dict_
        
        self.__apps_name = [i for i in self.__apps.keys() if i != 'env']
        self.__apps_name.sort()
        
        self.__g_env = self.__apps['env']
        
        self.reset()
        
    def getAppName(self, index):
        row = index.row()
        return self.__apps_name[row]
        
    def getAppVer(self, index):
        row = index.row()
        return self.__apps[self.__apps_name[row]]['ver']
        
    def getAppExec(self, index):
        row = index.row()
        return self.__apps[ self.__apps_name[row] ] ['exec']
    
    def getAppEnv(self, index):
        row = index.row()
        return self.__apps[ self.__apps_name[row] ] ['env']
    
    def getGEnv(self, ):
        return self.__g_env
    
    
        
    def rowCount(self, parent):
        return len(self.__apps_name)
    
    
    def data(self, index, role):
        row = index.row()
        
        if role == Qt.DisplayRole:
            return self.getAppName(index) + '\n' + \
                    self.getAppVer(index)
        
        elif role == Qt.DecorationRole:
            pixmap = QtGui.QPixmap( ':/apps/%s' %(self.getAppName(index) + self.getAppVer(index)) )#opj(PJVFX_PATH_, 'images', 'apps',
                                    #    self.getAppName(index) + self.getAppVer(index)) )
            if pixmap.isNull():
                pixmap = QtGui.QPixmap( ':/apps/%s' % self.getAppName(index)  )#opj(PJVFX_PATH_, 'images', 'apps',
                                        #    self.getAppName(index)) )
                if pixmap.isNull():
                    return QtGui.QIcon(QtGui.QPixmap( ':/apps/%s' % 'null'))#opj(PJVFX_PATH_, 'images', 'apps', 'null') ) )
            return QtGui.QIcon(pixmap)
        
        elif role == Qt.ToolTipRole:
            return self.getAppName(index) + '\n' + \
                    self.getAppVer(index) + '\n' + \
                    self.getAppExec(index) + '\n' + \
                    'AE:\n' + \
                    '\n'.join([str(i) for i in self.getAppEnv(index)] ) + '\n' + \
                    'GE:\n' + \
                    '\n'.join([str(i) for i in self.getGEnv()] )


    

if __name__ == '__main__':
    import appSetting
    setting = appSetting.appSetting()
    setting.readXML('../test/init.xml')
    sw_code = setting.getSetting()
    
    model = appListModel()
    model.setApps(sw_code)
    print model.getAppName(QtCore.QModelIndex())
#sw_code = {
#'app' :
#    {'houdini' :
#        {'ver' : '12.0.581',
#         'path' : r'C:\Program Files\Side Effects Software\Houdini 12.0.581\bin\houdini.exe'
#        },
#    
#     'nuke' :
#        {'ver' : '6.3v4',
#         'path' : r'C:\Program Files\Nuke6.3v4\Nuke6.3.exe'
#        }
#    }
#}
#
#a = sw_code['app']
#print a