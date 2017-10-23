### Adding XGBoost path to g++ ###

import os
mingw_path = "C:\\Program Files\\mingw-w64\\x86_64-7.2.0-posix-seh-rt_v5-rev0\\mingw64\\bin"
os.environ['PATH'] = mingw_path + ';' + os.environ['PATH']
