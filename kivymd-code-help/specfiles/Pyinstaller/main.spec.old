# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = ['kivymd pillow']
hiddenimports += collect_submodules('kivy')
hiddenimports += collect_submodules('kivymd')
hiddenimports += collect_submodules('ffpyplayer')
hiddenimports += collect_submodules('gstreamer')
hiddenimports += collect_submodules('ffpyplayer_codecs')
hiddenimports += collect_submodules('pillow')


block_cipher = None


a = Analysis(['/home/lightning/Documents/compiler-zone/dexel/main.py'],
             pathex=['/home/lightning/Documents/compiler-zone/dexel'],
             binaries=[],
             datas=[],
             hiddenimports=hiddenimports,
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='res/pyicon.ico')
