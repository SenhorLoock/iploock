#!/usr/lib/python
import requests
import os
#banner
def banner():
    os.system('clear')
    print ("""\033[1;35m
              \033[4;32mIPLOOCK\033[m\033[1;35m
\033[1;33m[GITHUB]:\033[4;32mhttps://github.com/SenhorLoock\033[m\033[1;35m
     `\|||/              
      (o o)      
\033[1;31m___\033[1;35mooO\033[1;31m_\033[1;35m(\033[1;31m_\033[1;35m)\033[1;31m_\033[1;35mOoo\033[1;31m______________________
_____|_____|_____|_____|_____|_____|
__|_____|_____|_____|_____|_____|
_____|_____|_____|_____|_____|\033[m
                  \033[4;32mby:Loock\033[m
""")

banner()
try:
#GERENCIANDO A API
    verif = input("\033[4;31mDIGITE O IP:\033[m ")
    search = requests.get("http://ip-api.com/json/{}".format(verif))
    dados = search.json()
#MOSTRANDO DADOS DO IP NO CONSOLE
    print ("\033[1;33mBUSCANDO IP: {}\033[m".format(verif))
    print ("\033[4;33mCidade:\033[1;32m {}\033[m".format(dados['city']))
    print ("\033[4;33mRegiao:\033[1;32m {}\033[m".format(dados['region']))
    print ("\033[4;33mlatitude:\033[1;32m {}\033[m".format(dados['lat']))
    print ("\033[4;33mlongitude:\033[1;32m {}\033[m".format(dados['lon']))
    print ("\033[4;33mTimeZone:\033[1;32m {}\033[m".format(dados['timezone']))
    print ("\033[4;33mNome Da Rede:\033[1;32m {}\033[m".format(dados['as']))
    print ("\033[4;33mStatus:\033[1;32m {}\033[m".format(dados['status']))
    end = input("\033[7;31mDeseja Fazer Mais Pesquisas ? Digite S/Para Sim Ou N/Para Não:\033[m ")
    if end == 's' or end == 'S' :
        os.system('python iploock.py')
    elif end == 'n' or end == 'N':
        banner()
        print ("\033[1;32mEXIT...\033[m")
except:
#CASO OCORRA ERRO ESSA FUNÇAO SERA ATIVADA
    print ("\033[7;31mERRO !!!\033[m")
    print ("\033[7;31mIP INVALIDO OU IMTERRUPIÇOES\033[m")
    os.system('sleep 3.0')
    exit()
