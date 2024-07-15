import pyautogui
import time
import psutil

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

# Função para coletar métricas do sistema
def coletar_metricas():
    return {
        'cpu': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'interrupt': psutil.cpu_stats().interrupts,
        'network': psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv,
        'swap': psutil.swap_memory().percent,
        # 'cpu_temp': psutil.sensors_temperatures().get('coretemp', [])[0].current if psutil.sensors_temperatures() else 0,
        'process_count': len(psutil.pids())
    }

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

#Selecionar diagrama UML com dois cliques
umlSelect = (845, 265)
pyautogui.doubleClick(umlSelect)
time.sleep(1)

# Coletar métricas antes de gerar o código
metricas_iniciais = coletar_metricas()

# Gerar código
codeGenereator = (1147, 847)
pyautogui.click(codeGenereator)
time.sleep(1)

# Confirmar com enter
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')

# Coletar métricas após gerar o código
metricas_finais = coletar_metricas()

# Exibir métricas
print("Métricas antes de gerar o código:")
print(metricas_iniciais)
print("Métricas após gerar o código:")
print(metricas_finais)

# Salvar métricas em um arquivo
with open('metricas.txt', 'w', encoding='utf-8') as metricas_arquivo:
    metricas_arquivo.write("Métricas antes de gerar o código:\n")
    for chave, valor in metricas_iniciais.items():
        metricas_arquivo.write(f"{chave}: {valor}\n")
    metricas_arquivo.write("\nMétricas após gerar o código:\n")
    for chave, valor in metricas_finais.items():
        metricas_arquivo.write(f"{chave}: {valor}\n")
