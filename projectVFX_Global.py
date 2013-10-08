# -*- coding: utf-8 -*-

from projectVFX_Include import *

#
global version_
version_ = '1.0.1'
#
global com_
com_ = 'BaseFX'
#
global doDebug_
doDebug_ = False
if (os.getenv("PROJECTVFX_DEBUG") != None):
    doDebug_ = True
#

#
global log_
def log_(string):
    if (doDebug_):

            sys.stderr.write ("DEBUG:  %s\n" % str(string) )
            sys.stderr.flush()

#

# SYS_TYPE_
global SYS_TYPE_
#SYS_TYPE_ = ''
if platform.platform().startswith('Linux'):
    SYS_TYPE_ = 'linux'
elif platform.platform().startswith('Darwin'):
    SYS_TYPE_ = 'mac'
elif platform.platform().startswith('Windows'):
    SYS_TYPE_ = 'win'
else:
    log_('SYS_TYPE_ Error')
#


# osOpen_
global osOpen_
def osOpen_(path):
    if SYS_TYPE_ == 'linux':
        os.system('gnome-open %s' % path)
    elif SYS_TYPE_ == 'mac':
        os.system('open %s' % path)
    elif SYS_TYPE_ == 'win':
        path = path.replace("/", "\\")
        subprocess.Popen('explorer ' + path)
#

# nuke cmd
global opj, opb, opd
opj = os.path.join
opb = os.path.basename
opd = os.path.dirname

    
# SYS_TYPE_seq
global SEP_, QQC_
SEP_ = QtCore.QDir.separator()
#
QQC_ = QtCore.QDir.convertSeparators


global BASE_PATH_F_, BASE_PATH_S_
if SYS_TYPE_ in ('linux', 'mac'):
    BASE_PATH_F_ = '/ibrix3' + SEP_
else:
    BASE_PATH_F_ = 'Y:' + SEP_
    
global PJVFX_PATH_
PJVFX_PATH_ = os.path.dirname(sys._getframe().f_code.co_filename)

