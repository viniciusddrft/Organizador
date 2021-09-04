############################################
#########created by viniciusddrft###########
############################################
###created by a developer for developers####
############################################
import glob
import re
import os
import shutil


def create_folders():
    directories = []
    test = 0
    for file in glob.glob('*.*'):
        extensions = re.findall(r'\.\w+', file)
        directories.append(extensions)

    for directorie in directories:
        if '.py' in directorie:
            test += 1
            if test > 1: 
                try:
                    os.mkdir('Python')
                    print('criando pasta -> Python')
                except:
                    pass
    #-------------------------------------------------------
        elif '.dart' in directorie:
            try:
                os.mkdir('Dart')
                print('criando pasta -> Dart')
            except:
                pass
    #-------------------------------------------------------
        elif '.scala' in directorie or '.sc' in directorie:
            try:
                os.mkdir('Scala')
                print('criando pasta -> Scala')
            except:
                pass
    #-------------------------------------------------------
        elif '.rb' in directorie:
            try:
                os.mkdir('Ruby')
                print('criando pasta -> Ruby')
            except:
                pass
    #-------------------------------------------------------
        elif '.c' in directorie:
            try:
                os.mkdir('Linguagem_C')
                print('criando pasta -> Linguagem C')
            except:
                pass
    #-------------------------------------------------------
        elif '.cpp' in directorie:
            try:
                os.mkdir('Linguagem_C++')
                print('criando pasta -> Linguagem C++')
            except:
                pass
    #-------------------------------------------------------       
        elif '.js' in directorie:
            try:
                os.mkdir('JavaScript')
                print('criando pasta -> JavaScript')
            except:
                pass
    #-------------------------------------------------------
        elif '.sh' in directorie:
            try:
                os.mkdir('Shell_Script')
                print('criando pasta -> Shell_Script')
            except:
                pass
    #-------------------------------------------------------   
        elif '.cs' in directorie:
            try:
                os.mkdir('Linguagem_C#')
                print('criando pasta -> Linguagem_C#')
            except:
                pass
    #-------------------------------------------------------
        elif '.css' in directorie:
            try:
                os.mkdir('CSS')
                print('criando pasta -> CSS')
            except:
                pass
    #-------------------------------------------------------
        elif '.html' in directorie:
            try:
                os.mkdir('HTML')
                print('criando pasta -> HTML')
            except:
                pass
    #-------------------------------------------------------
        elif '.pl' in directorie or '.pm' in directorie:
            try:
                os.mkdir('Perl')
                print('criando pasta -> Perl')
            except:
                pass
    #-------------------------------------------------------
        elif '.go' in directorie:
            try:
                os.mkdir('Golang')
                print('criando pasta -> Golang')
            except:
                pass
    #-------------------------------------------------------
        elif '.jar' in directorie:
            try:
                os.mkdir('Java')
                print('criando pasta -> Java')
            except:
                pass
    #-------------------------------------------------------
        elif '.txt' in directorie:
            try:
                os.mkdir('Texto_Puro')
                print('criando pasta -> Texto_Puro')
            except:
                pass
    #-------------------------------------------------------
    #Imagens
        elif '.jpeg' in directorie or '.gif' in directorie or '.bmp' in directorie or '.png' in directorie or '.psd' in directorie or '.tiff' in directorie or '.svg' in directorie or '.jpg' in directorie:
            try:
                os.mkdir('Imagens')
                print('criando pasta -> Imagens')
            except:
                pass
    #-------------------------------------------------------
    #Videos
        elif '.mp4' in directorie or '.mkv' in directorie or '.mov' in directorie or '.avi' in directorie or '.flv' in directorie or '.wmv' in directorie:
            try:
                os.mkdir('Videos')
                print('criando pasta -> Videos')
            except:
                pass
    #-------------------------------------------------------
    #Musicas
        elif '.mp3' in directorie or '.wma' in directorie or '.ogg' in directorie or '.aac' in directorie or '.wav' in directorie or '.pcm' in directorie:
            try:
                os.mkdir('Musicas')
                print('criando pasta -> Musicas')
            except:
                pass
    #-------------------------------------------------------
    #Documentos
        elif '.doc' in directorie or '.docx' in directorie or '.odt' in directorie or '.pdf' in directorie or '.xml' in directorie or '.csv' in directorie or '.xls' in directorie or '.potx' in directorie or '.ppsx' in directorie or '.pptx' in directorie or '.odp' in directorie or '.xlsx' in directorie or '.ppt' in directorie:
            try:
                os.mkdir('Documentos')
                print('criando pasta -> Documentos')
            except:
                pass
    #-------------------------------------------------------
    #Arquivos_Compactados
        elif '.zip' in directorie or '.tar' in directorie or '.gzip' in directorie or '.bz2' in directorie or '.rar' in directorie or '.gz' in directorie or '.xz' in directorie:
            try:
                os.mkdir('ArquivosCompactados')
                print('criando pasta -> ArquivosCompactados')
            except:
                pass
    #-------------------------------------------------------
        elif '.iso' in directorie:
            try:
                os.mkdir('Iso')
                print('criando pasta -> Iso')
            except:
                pass


def move_files():

    for name_file in os.listdir(os.getcwd()):
        name, extensions = os.path.splitext(name_file)


        if extensions == '.py':
            try:
                full_name = name+extensions
                if full_name != 'organizador.py':
                    shutil.move(full_name, 'Python')
                    print('Movendo arquivos Python para pasta -> Python')
            except:
                pass
    #-------------------------------------------------------

        if extensions == '.dart':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Dart')
                print('Movendo arquivos em Dart para pasta -> Dart')
            except:
                pass
    #-------------------------------------------------------
        if extensions == '.scala' or extensions == '.sc':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Scala')
                print('Movendo arquivos em Scala para pasta -> Scala')
            except:
                pass
    #-------------------------------------------------------
        if extensions == '.c':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Linguagem_C')
                print('Movendo arquivos em C para pasta -> Linguagem_C')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.cpp':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Linguagem_C++')
                print('Movendo arquivos em C++ para pasta -> Linguagem_C++')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.js':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'JavaScript')
                print('Movendo arquivos JavaScript para pasta -> JavaScript')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.rb':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Ruby')
                print('Movendo arquivos Ruby para pasta -> Ruby')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.cs':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Linguagem_C#')
                print('Movendo arquivos em Linguagem_C# para pasta -> Linguagem_C#')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.sh':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Shell_Script')
                print('Movendo arquivos em Shell_Script para pasta -> Shell_Script')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.css':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'CSS')
                print('Movendo arquivos em CSS para pasta -> CSS')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.html':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'HTML')
                print('Movendo arquivos em HTML para pasta -> HTML')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.go':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Golang')
                print('Movendo arquivos em Golang para pasta -> Golang')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.pl' or extensions == '.pm':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Perl')
                print('Movendo arquivos em Perl para pasta -> Perl')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.txt':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Texto_Puro')
                print('Movendo arquivos em Texto_Puro para pasta -> Texto_Puro')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.jar':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Java')
                print('Movendo arquivos em Java para pasta -> Java')
            except:
                pass
    #-------------------------------------------------------
    #Imagens
        elif extensions == '.jpeg' or extensions == '.gif' or extensions == '.bmp' or extensions == '.png' or extensions == '.psd' or extensions == '.tiff' or extensions == '.svg' or extensions == '.jpg':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Imagens')
                print('Movendo Imagens para pasta -> Imagens')
            except:
                pass
    #-------------------------------------------------------
    #Videos
        elif extensions == '.mp4' or extensions == '.mkv' or extensions == '.mov' or extensions == '.avi' or extensions == '.flv' or extensions == '.wmv':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Videos')
                print('Movendo Videos para pasta -> Videos')
            except:
                pass
    #-------------------------------------------------------
    #Musicas
        elif extensions == '.mp3' or extensions == '.wma' or extensions == '.ogg' or extensions == '.aac' or extensions == '.wav' or extensions == '.pcm':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Musicas')
                print('Movendo Musicas para pasta -> Musicas')
            except:
                pass
    #-------------------------------------------------------
    #Documentos
        elif extensions == '.doc' or extensions == '.docx' or extensions == '.odt' or extensions == '.pdf' or extensions == '.xml' or extensions == '.csv' or extensions == '.xls' or extensions == '.potx' or extensions == '.ppsx' or extensions == '.pptx' or extensions == '.odp' or extensions == '.xlsx' or extensions == '.ppt':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Documentos')
                print('Movendo Documentos para pasta -> Documentos')
            except:
                pass
    #-------------------------------------------------------
    #Arquivos_Compactados
        elif extensions == '.zip' or extensions == '.tar' or extensions == '.gzip' or extensions == '.bz2' or extensions == '.rar' or extensions == '.gz' or extensions == '.xz':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'ArquivosCompactados')
                print('Movendo Arquivos Compactados para pasta -> ArquivosCompactados')
            except:
                pass
    #-------------------------------------------------------
        elif extensions == '.iso':
            try:
                full_name = name+extensions
                shutil.move(full_name, 'Iso')
                print('Movendo arquivos em Iso para pasta -> Iso')
            except:
                pass




if __name__ == "__main__":
    create_folders()
    move_files()
    print('Pronto tudo organizado!!!')
    
