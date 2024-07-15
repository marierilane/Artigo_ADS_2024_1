import os

def contar_linhas_de_codigo(arquivo_java):
    try:
        with open(arquivo_java, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            total_linhas = len(linhas)
            linhas_de_codigo = sum(1 for linha in linhas if linha.strip() and not linha.strip().startswith('//') and not linha.strip().startswith('/*') and not linha.strip().startswith('*') and not linha.strip().startswith('*'))
        return total_linhas, linhas_de_codigo
    except FileNotFoundError:
        print(f"Arquivo {arquivo_java} não encontrado.")
        return 0, 0

def contar_linhas_em_pasta(pasta):
    resultados = []
    for root, dirs, files in os.walk(pasta):
        for file in files:
            if file.endswith('.java'):
                caminho_arquivo = os.path.join(root, file)
                total_linhas, linhas_de_codigo = contar_linhas_de_codigo(caminho_arquivo)
                resultados.append((caminho_arquivo, total_linhas, linhas_de_codigo))
    return resultados

pasta = 'C:\\Users\\Victor Pinheiro\\Downloads\\es\\codigos'
resultados = contar_linhas_em_pasta(pasta)

with open('resultados.txt', 'w', encoding='utf-8') as resultado_arquivo:
    for arquivo, total, codigo in resultados:
        resultado_arquivo.write(f"Arquivo: {arquivo}\n")
        resultado_arquivo.write(f"Total de linhas: {total}\n")
        resultado_arquivo.write(f"Linhas de código: {codigo}\n")
        resultado_arquivo.write("\n")

    total_arquivos = len(resultados)
    total_linhas = sum(total for _, total, _ in resultados)
    total_linhas_codigo = sum(codigo for _, _, codigo in resultados)

    resultado_arquivo.write(f"Total de arquivos: {total_arquivos}\n")
    resultado_arquivo.write(f"Total de linhas: {total_linhas}\n")
    resultado_arquivo.write(f"Total de linhas de código: {total_linhas_codigo}\n")
    resultado_arquivo.write(f"Soma de todas as linhas de código: {total_linhas_codigo}\n")
