# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Kristopher Gaming PC\\desktop\\wowtoken\\WoWToken.py'],
             pathex=['C:\\Users\\Kristopher Gaming PC\\desktop\\wowtoken', 'C:\\Users\\Kristopher Gaming PC\\desktop\\wowtoken'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['e:\\python\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='win')
