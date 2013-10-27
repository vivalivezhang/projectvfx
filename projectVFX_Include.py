# -*- coding: utf-8 -*-
# import system
import os, sys
import time
import ConfigParser
#try:
#    import nuke
#except:
#    if (os.getenv("PROJECTVFX_DEBUG") != None):
#        sys.stderr.write("%s\n" % 'Could not load nuke module')
#        sys.stderr.flush()
#
#try:
#    import nukescripts
#except:
#    if (os.getenv("PROJECTVFX_DEBUG") != None):
#        sys.stderr.write("%s\n" % 'Could not load nukescripts module')
#        sys.stderr.flush()
    
import glob
import re
import cPickle as pickle
import platform
try:
    import pwd
except ImportError:
    if (os.getenv("PROJECTVFX_DEBUG") != None):
        sys.stderr.write("%s\n" % 'Could not load pwd module')
        sys.stderr.flush()

import stat
import threading
import thread
import subprocess
try:
    import ConfigParser
except ImportError:
    if (os.getenv("PROJECTVFX_DEBUG") != None):
        sys.stderr.write ("%s\n" % "Could not load ConfigParser module, sticky settings will not be loaded/saved")
        sys.stderr.flush()
from xml.etree import ElementTree
import random




# import PySide or PyQt4

import sip
for mod in ("QString","QTextStream"):
#for mod in ("QDateTime", "QString", "QTextStream", "QTime", "QUrl", "QVariant"):
    sip.setapi(mod, 2)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4 import QtXml, QtWebKit, QtNetwork
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot



#import PyQt Stylesheet
import lib.darkorangeStylesheet
# resource
import projectVFX_ReSource_rc
import images.imagesResource_rc
