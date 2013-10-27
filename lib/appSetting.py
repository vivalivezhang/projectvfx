# -*- coding: utf-8 -*-

from projectVFX_Global import *

class appSetting():
    def __init__(self, ):
        self.app_setting = {}
        

    def readXML(self, xmlFile):
        self.app_setting = {'env':[]}
        
        Et = ElementTree.parse(xmlFile)
        root = Et.getroot()
        appNodes = root.findall('./app')
        for appNode in appNodes:
            appName = appNode.find('name').text
            appVer = appNode.find('ver').text
            appExec = appNode.find('exec').text
            appEnvs = appNode.find('env').getchildren()

            #print appName,appVer,appExec,appEnvs
            self.app_setting[appName] = {'ver' : appVer, 'exec': appExec,
                                         'env' : [(appEnv.tag, appEnv.text, appEnv.get('mode')) for appEnv in appEnvs] }

        for gEnv in root.find('./env').getchildren():
            self.app_setting['env'].append( (gEnv.tag, gEnv.text, gEnv.get('mode') ) )
            
        #log_( self.app_setting)
        
    def getSetting(self, ):
        return self.app_setting
    

if __name__ == '__main__':
    setting = appSetting()
    setting.readXML('../test/init.xml')
