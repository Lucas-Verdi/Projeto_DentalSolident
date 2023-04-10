from cx_Freeze import setup, Executable

setup(
    name="Auto-Formatação de pedidos",
    version="1.0",
    description='''Separador de Pedidos
Autor: Lucas Arnaut Verdi
Versão: 2.0
Data: 10/04/2023''',
    executables=[Executable("SeparadorDePedidos.py", base="Win32GUI")],
)

#cxfreeze SeparadorDePedidos.py --target-dir Separador-Separador1.2

#python setup.py build