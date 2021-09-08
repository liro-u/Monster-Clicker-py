from cx_Freeze import setup, Executable

includefiles=[
    "resources",
    "classes",
    "detail_jam_message.txt"
    ]
    
    

target = Executable(
    script="main.py",
    icon="logo_monster_clicker.ico"
    )

setup(
    name="Monster Clicker",
    version="1.0",
    description="le meilleur cliqueur de 2020!!!",
    author="Noailles Valentin, Vuillaume Axel, Arette-Hourquet Jean-Loup",
    options = {'build_exe' : {'include_files':includefiles}},
    executables=[target]
    )
