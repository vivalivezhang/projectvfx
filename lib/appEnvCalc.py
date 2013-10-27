# -*- coding: utf-8 -*-
from projectVFX_Global import *

__all__ = ['appEnvCalc']


if SYS_TYPE_ == 'win':
    envSep_ = ';'
else:
    envSep_ = ':'

class appEnvCalc(object):
    def __init__(self, settingEnvs = []):
        '''
        setting = []
        '''
        
        self.settingEnvs = settingEnvs
        
        self.finalEnvs = os.environ.copy()
        
        self.calc()
    
    
    
    def calc(self):
        #if self.settingEnvs:
            for settingEnv in self.settingEnvs:
                #log_(settingEnv)
                key = settingEnv[0]
                value = settingEnv[1]
                mode = settingEnv[2]
    
                if mode == 'append_head':
                    if not self.finalEnvs.has_key(key):
                        self.finalEnvs[key] = value
                    else:
                        keyCulc = self.finalEnvs[key]
                        keyCulc = value + envSep_ + keyCulc
                        self.finalEnvs[key] = keyCulc
                elif mode == 'append_tail':
                    if not self.finalEnvs.has_key(key):
                        self.finalEnvs[key] = value
                    else:
                        keyCulc = self.finalEnvs[key]
                        keyCulc = keyCulc + envSep_ + value
                        self.finalEnvs[key] = keyCulc
                        
                elif mode == 'replace':
                    self.finalEnvs[key] = value

    
    def getResult(self, ):
        return self.finalEnvs
    
    

if __name__ == '__main__':
    finalEnv = appEnvCalc([('NUKE_PATH', '/All/Oxygen/util/nuke/7.0_test:/All/Oxygen/cpp/eclipse_test/ndk_test_1/so', 'append_tail'),('TEST', '/All/Oxygen/util/nuke/6.3_test', 'append_tail'),('PATH','HAHA','append_head'),('PATH','HAHA','append_tail')]).getResult()
    print finalEnv
