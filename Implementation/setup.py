from cx_Freeze import setup, Executable

setup(name = "Scouting Database",
      version = "0.1",
      description = "Database program for scouting",
      executables = [Executable("main_window.py")])
