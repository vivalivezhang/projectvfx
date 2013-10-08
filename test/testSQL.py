
import sqlite3
import cPickle as pickle

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row

    sw_code = {
'app' :
    {'houdini' :
        {'ver' : '12_0_581',
         'path' : r'C:\Program Files\Side Effects Software\Houdini 12.0.581\bin\houdini.exe'
        },

     'nuke' :
        {'ver' : '6_3v4',
         'path' : r'C:\Program Files\Nuke6.3v4\Nuke6.3.exe --nukex'
        },

     'maya' :
        {'ver' : '2012',
         'path' : r'C:\Program Files\Autodesk\Maya2012\bin\maya.exe'
        },

     'rv' :
        {'ver' : '3_12_18',
         'path' : '/All/Oxygen/APP/rv-Linux-x86-64-3.12.18/bin/rv'
        },
    },
'env' :
    {
        
    }
    
}

    b = pickle.dumps(sw_code)
    #print pickle.loads(b)
    
    db.execute('insert into tst (app) values %s' % b)
    db.commit()
    a = db.execute('select nuke,houdini from tst', )
    for i in a:
        print (i['nuke'], i['houdini'])

if __name__ == '__main__':
    main()
