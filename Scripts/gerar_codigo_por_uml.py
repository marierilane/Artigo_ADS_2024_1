import pyautogui
import time

# Define a pausa entre as ações do pyautogui
pyautogui.PAUSE = 2

# Função para abrir o Astah usando a pesquisa do Windows
def open_astah_via_search():
    # Pressiona a tecla Windows para abrir o menu de início
    pyautogui.press('win')
    time.sleep(2)
    
    # Digita "Astah" para pesquisar
    pyautogui.write('Astah')
    time.sleep(2)
    
    # Pressiona Enter para abrir o Astah
    pyautogui.press('enter')
    print("Astah iniciado.")

# Abra o Astah via pesquisa do Windows
open_astah_via_search()

# Aguarde o Astah abrir
time.sleep(2)
pyautogui.press('enter')

# Clicar no menu "File"
file_menu_coords = (15, 29)
pyautogui.click(file_menu_coords)
time.sleep(1)

# Clicar na opção "Open"
open_option_coords = (63, 104) 
pyautogui.click(open_option_coords)
time.sleep(1)

# Clicar no file selecionado
file_coords = (804, 413) 
pyautogui.click(file_coords)
time.sleep(1)

# Abrir o File UML com enter
open_file = (1134, 6802)
pyautogui.press('enter')
time.sleep(1)

# Clicar no tools
tool_click = (271, 38)
pyautogui.click(tool_click)
time.sleep(1)

# Clicar na aopção java
java = (293, 94)
pyautogui.click(java)
time.sleep(1)

# Clicar na opção export java
export_java = (547, 107)
pyautogui.click(export_java)
time.sleep(1)

# Selecionar a pasta com enter
pyautogui.press('enter')
time.sleep(1)

#Selecionar pasta de projeto
diagram = (565, 246)
pyautogui.click(diagram)
time.sleep(1)

#Seleciobar diagraa UML com dois cliks
umlSelect = (845, 265)
pyautogui.doubleClick(umlSelect)
time.sleep(1)

#Gerar código
codeGenereator = (1147, 847)
pyautogui.click(codeGenereator)
time.sleep(1)

# Confirmar com enter
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')

