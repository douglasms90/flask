ipeth='iso.3.6.1.2.1.4.24.4.1.5'			             ### Lista todas as interfaces (Virtuais ou não) ###
totalonline='1.3.6.1.4.1.2011.5.2.1.14.1.2'		         ### Lista numero total de usuarios online ###
usuario='1.3.6.1.4.1.2011.5.2.1.15.1.3'			         ### Lista todos os usuarios conectados ###
ip1='iso.3.6.1.4.1.2011.5.2.1.15.1.15'			         ### Lista os IPs de todos os usuarios ###
mac='iso.3.6.1.4.1.2011.5.2.1.15.1.17'			         ### Lista o MAC de todos os usuarios ##
eth='iso.3.6.1.4.1.2011.5.2.1.15.1.57'			         ### Lista a interface utilizada para autenticação ###
traf='iso.3.6.1.2.1.31.1.1.1.6'				             ### Lista trafego de todas as interfaces (IN) ###
trafup='1.3.6.1.2.1.31.1.1.1.10'			             ### Lista o trafego de todas as interfaces (OUT)
tempo='1.3.6.1.4.1.2011.5.2.1.16.1.18'			         ### Lista tempo da sessão
snmp_str='snmpwalk -v2c -c public_tapi 172.16.97.2 '	 ### Comando snmp ###
usr_downflw='1.3.6.1.4.1.2011.5.2.1.15.1.36'             ### Bytes recebidos pelo servidor do CLiente ###
usr_upflw='1.3.6.1.4.1.2011.5.2.1.15.1.37'               ### Bytes enviados pelo servidor ai cliente ####
lista_clientes='> clientes_tmp'                          ###

import os
import subprocess
import time

def cerbero():
    print ("\n\nSeja bem vindo!!! \n\nDigite a opção desejada:\n\n")
    opt = int (input("\n 1 - Listar todos os usuarios ONLINE\n 2 - Buscar usuario\n 3 - Total de usuarios online\n 4 - Atualizar banco de dados\n"))

    if opt == 1:
        os.system("cat clientes_tmp | awk '{print $4}'")
        cerbero()
    if opt == 2:

        usr = str(input("\n\n Digite o nome do usuario:\n"))
        print ("\nusuario@dominio")
        os.system("cat clientes_tmp | awk '{print $4}' | grep "+usr)
        id = os.popen("cat clientes_tmp | grep "+usr+ "| awk -F '.' '{print $14}' | awk '{print $1}'").read()
        id = id.replace("\n", "")


        print ("\nIP:")
        os.system(snmp_str+ip1+'.'+ str(id) +" | awk '{print $4}'")
        ip=os.popen(snmp_str+ip1+'.'+ str(id) +" | awk '{print $4}'").read()
        ip = ip.replace("\n","")


        print("\nMAC ADDRESS")
        os.system(snmp_str+mac+'.'+ str(id) +" | awk '{print $4,$5,$6,$7,$8,$9}'")

        print("\nInterface/VLAN")
        os.system(snmp_str+eth+'.'+ str(id) +" | awk '{print $4}'")

        print("\nTempo OnLine:")
        sec = os.popen(snmp_str+tempo+'.'+ str(id) +" | awk '{print $4}'").read()
        sec = sec.replace ("\n","")
        sec_convert = round(int(sec)/3600, 2)
        print(str(sec_convert) +" Horas")

        ethpoe=os.popen(snmp_str+ipeth+'.'+ str(ip) +" | awk '{print $4}'").read()

        next = input("\nPressione qualquer tecla para continuar:\n")

        print ("\nAguarde estamos estimando o consumo...\n")

        for count in range (0, 1000):

            bw1 = int(os.popen(snmp_str+usr_downflw+'.'+ str(id) +"| awk '{print $4}'").read()) 	### Trafego em valores brutos ###
            #bw1 = bw1.replace("\n", "")
            bw3 = int(os.popen(snmp_str+usr_upflw+'.'+ str(id) +"| awk '{print $4}'").read())
            #bw3 = bw3.replace("\n","")


            time.sleep(20)						### Necessario aguardar 20s para que se possa ter   ###

            bw2=int(os.popen(snmp_str+usr_downflw+'.'+ str(id) +"| awk '{print $4}'").read())	### 2 valores necessarios para o calculo da transf.###
            #bw2 = bw2.replace("\n", "")
            bw4=int(os.popen(snmp_str+usr_upflw+'.'+ str(id) +"| awk '{print $4}'").read())
            #bw4 = bw4.replace("\n", "")

            print("\n" * 130)
            bwup=round((bw2-bw1)*8/1024,0)
            bwup=round(bwup/2)
            #print(bwup)
            if bwup > 1024:
                bwup=(bwup/7812)
                print ("\nUp: ", round(bwup, 0), "Mbps\n")
            else:
                print ("\nUp: ", round(bwup, 0), "Kbps\n")

            bw=round((bw4-bw3)*8/1024,0)
            bw=round(bw/2)
            #print(str(bw4) +"-"+ str(bw3)+"="+ str(bw))
            if bw > 1024:
                bw=(bw/7812)
                print ("Down: ", round(bw, 0), "Mbps")
            else:
                print ("Down: ", round(bw, 0), "Kbps")

        cerbero()

    if opt == 3:
        print("\n\n TOTAL DE USUARIOS ONLINE:\n")
        os.system(snmp_str+totalonline+ "| awk '{print $4}'")
        cerbero()
    if opt == 4:
        print ('Aguarde enquanto atualizamos a lista de usuarios Online')
        os.system(snmp_str+usuario+lista_clientes)
        cerbero()
    else:
        print ("FIM!")
        cerbero()

cerbero()
