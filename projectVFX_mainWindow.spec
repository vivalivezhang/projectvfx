# -*- mode: python -*-
a = Analysis(['projectVFX_mainWindow.py'],
             pathex=['/mnt/disk_d/All/ibrix3/COM/gene/ple/projectVFX'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.linux2/projectVFX_mainWindow', 'projectVFX_mainWindow'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'projectVFX_mainWindow'))
