import sys
import time
import os
import shutil

#Para usar estas clases do módulo watchdog é necessário importar primeiro no terminal:
# pip install watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "DIGITE O CAMINHO DA PASTA DE DOWNLOAD (USE " / ") no VSC"
# to_dir = "DIGITE A PASTA DE CAMINHO DE DESTINO (USE " / ") no VSC"
from_dir = "C:/Users/cinti/Downloads"
to_dir = "C:/Users/cinti/Desktop/Arquivos_baixados"

# Possíveis extensões de acordo com o tipo de arquivo
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos - FileSystemEventHandler (classe predefinida)
# Classe Gerenciadora de movimentação de arquivos
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        #print(event)
        #print(event.src_path)

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Baixado " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Diretório Existe...")
                    print("Movendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Criando Diretório...")
                    os.makedirs(path2)
                    print("Movendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)


# Inicializando a Classe "Gerenciadora de Eventos" com uma variável chamada: gerenciador de eventos
event_handler = FileMovementHandler()

# Criando o objeto chamado Observer, que irá começar a observar o gerenciador de eventos
observer = Observer()

# Agendando o Observer - o monitoramento de caminho 
# (nome da nossa classe gerenciadora de arquivos, caminho do diretório a ser monitorado, true: permite observar as alterações em todo caminho fornecido)
observer.schedule(event_handler, from_dir, recursive=True)

# Iniciando o Observer
observer.start()

#Condição para imprimir "executando ... " para mostrar que o programa está em ação
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()
