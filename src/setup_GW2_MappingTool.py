import sys
from cx_Freeze import setup, Executable

base = None

#Necessary for 32-bit systems
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("GW2_MappingTool.py", base=base, targetName="GW2_MappingTool.exe", icon = "assets\\gw2_icon.ico")]

#Any packages that need to be added for compilation.
#Some may work but if not include them here
# packages = ["Client"]
packages = []

options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    #EXE NAME HERE
    name = "GW2_MappingTool",
    options = options,
    version = "0.1",
    description = 'GW2 Mapping Tool',
    executables = executables
)