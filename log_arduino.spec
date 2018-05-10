# -*- mode: python -*-

block_cipher = None


a = Analysis(['log_arduino.py'],
             pathex=['C:\\python35\\coding\\log_arduino'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='log_arduino',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
