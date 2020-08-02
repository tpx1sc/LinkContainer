# LinkContainer é un programma che encripta i link con crittografia rot13 e li salva in plaintext
# ATTENZIONE[!]: é ancora una beta, potrebbero verificarsi bug ed in generale il programma non é molto utile
# l'ho fatto solo per il gusto di farlo
# COSE DA AGGIUNGERE: una GUI

import os # Modulo os per eseguire comandi da console (cmd)
import codecs # Modulo che serve ad encriptare i link
import pyperclip

enc_link = 0

nome_del_file = 'links.txt' # Nome del file nel quale verrano salvati i link

file_saved = 0 # status del file, quindi se é salvato o meno

def save(): # Funzione che salva il link criptato
    global enc_link
    f = open(nome_del_file, "a") # apre il file nel quale verranno salvati i link in modalita' append, dunque aggiunta
    f.write('{}\n'.format(enc_link)) # aggiunge la variabile 'enc_link' al file

while True: # loop principale
    if os.path.exists(nome_del_file): # se il file nel quale verranno salvate le password é esiste, prosegue con il loop
        file_saved = True
        pass
    else: # se il file risulta assente, verra' creato in modalita' 'x' dunque creazione forzata
        print("creazione del file in corso...")
        try:
            f = open(nome_del_file, 'x')
        except error as e: # se il file é gia esistente, manda in output l'errore
            print("file gia' esistente: {}".format(e))
    os.system("cls")
    print("LinkContainer===================================================================\n")
    print("1) Aggiungi un link\n2) Mostra i link salvati\n3) Decripta i link\n\n\n0) Esci\n")
    x = input("> ")
    if x == '1':
        print("========================================")
        print("Digita il link che desideri nascondere\n")
        link = input("> ")
        enc_link = codecs.encode(link, 'rot_13') # funzione che encripta la variabile link in rot13
        save()
    if x == '2':
        f = open(nome_del_file, 'r')
        print("=======================")
        print(f.read())
        print("=======================")
        pause = input("Premi un tasto per tornare al menu' principale...\n")
    if x == '3':
        if file_saved:
            print("=================================================")
            print("Adesso verranno mandati in output i link criptare")
            print("selezionare i link e fare ctrl-c, ctrl-v")
            print("=================================================\n")
            f = open(nome_del_file, 'r')
            print(f.read())
            print("========================================\n")
            decripta = input("Digita il link da decifrare: ")

            decrl = codecs.encode(decripta, 'rot_13') # funzione che decripta il link del'user
            print("\n================================")
            print(decrl)
            print("\n================================")
            copy_to_clipboard = input("Desideri salvare il link nella clipboard (si/no):\n>")
            if copy_to_clipboard == "si": # il programma chiede all'user se desidera salvare il link decriptato nella clipboard
                pyperclip.copy(decrl) # funzioni che salvano la variabile decrl nella clipboard
                pyperclip.paste()
            else: # se la risposta é no: sospende il loop finché l'user non dara' un input
                pause = input("Premi un tasto per tornare al menu' principale...\n")
                pass
        else:
            print("=============================")
            print("non hai salvato alcun link[!]")
            print("=============================")

    if x == '0':
        exit()
