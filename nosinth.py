from lxml import html
import requests
import webbrowser
import os


def intro():
	print('\033[1;31;49m' + '\n               .oooooo.    .oooooo..o ooooo ooooo      ooo ooooooooooooo oooo' + '\x1b[0m')
	print('\033[1;31;49m' + '              d8P   `Y8b  d8P     `Y8 `888  `888b.     `8  8    888   `8 `888' + '\x1b[0m')
	print('\033[1;37;49m' + ' ooo. .oo.   888      888 Y88bo.       888   8 `88b.    8       888       888 .oo.' + '\x1b[0m')
	print('\033[1;34;49m' + '  888P Y88b  888      888  ` Y8888o.   888   8   `88b.  8       888       888P"Y88' + '\x1b[0m')
	print('\033[1;37;49m' + '  888   888  888      888      `"Y88b  888   8     `88b.8       888       888   888' + '\x1b[0m')
	print('\033[1;31;49m' + '  888   888  `88b    d88 oo      .d8P  888   8       `888       888       888   888' + '\x1b[0m')
	print('\033[1;31;49m' + ' o888o o888o  `Y8bood8P    888888P    o888o o8o        `8      o888o     o888o o888o' + '\x1b[0m')
	print('\x1b[1;34;49m' + '>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	print('\x1b[1;33;49m' + '         Norwegian Open Source Intelligence Harvester v.1.0 - AFL 2018' + '\x1b[0m')
	print('\x1b[1;34;49m' + '>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')

	print('\x1b[1;32;49m' + '\n Conducts a name search in the Norwegian postal address database,\n national organizations register and telephone register.' + '\x1b[0m')
	print('\x1b[1;32;49m' + ' Searches in the Norid WHOIS database and Aksjonaerregisteret (stock owners)\n available in web browser after search.' + '\x1b[0m')


def posten():
	#Output from https://adressesok.posten.no
	print('\x1b[1;31;49m' + '\n>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	print('\x1b[1;31;49m' + '* Results from Posten - adressesok.posten.no' + '\x1b[0m')
	print('\x1b[1;31;49m' + '>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	page = requests.get('http://adressesok.posten.no/nb/persons/search?utf8=%E2%9C%93&q='+name+'&token=')
	tree = html.fromstring(page.content)
	result = tree.xpath('//td[@class="address"]/text()')
	for item in result:
		print(item)


def brreg():
	#Output from brreg.no
	print('\x1b[1;35;49m' + '\n>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	print('\x1b[1;35;49m' + '* Top 10 results from Bronnoysundsregistrene - brreg.no' + '\x1b[0m')
	print('\x1b[1;35;49m' + '>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	page = requests.get('https://w2.brreg.no/enhet/sok/treffliste.jsp?navn='+name+'&orgform=0&fylke=0&kommune=0')
	tree = html.fromstring(page.content)
	brreg = tree.xpath('//div[@class="liste col-sm-5"]/a/text()')
	brreglist = brreg[:10]
	for item in brreglist:
	        print(item)


def gulesider():
	#Output from gulesider.no
	print('\x1b[1;33;49m' + '\n>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	print('\x1b[1;33;49m' + '* Top 10 results from Telefonkatalogen Gule Sider  - gulesider.no' + '\x1b[0m')
	print('\x1b[1;33;49m' + '>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	page = requests.get('https://www.gulesider.no/person/resultat/'+name)
	tree = html.fromstring(page.content)
	gsname = tree.xpath('//span[@class="hit-name-ellipsis"]/a/text()')
	#gstlf = tree.xpath('//span[@class="hit-phone-number type-phone_normal_mobile"]/text()')
	gsnamelist = gsname[:10]
	#gstlflist = gstlf
	#space = ', '
	#tlflist = []
	#for i in gsnamelist:
	#    for j in gstlflist:
	#        tlflist.append(i+space+j)
	#tlf10 = tlflist
	#for item in tlf10:
	#        print(item)
	#print(gsname)
	#print(gstlf)
	for item in gsnamelist:
	        print(item)


def browser1():
	webbrowser.open('http://adressesok.posten.no/nb/persons/search?utf8=%E2%9C%93&q='+name+'&token=')
        webbrowser.open('https://w2.brreg.no/enhet/sok/treffliste.jsp?navn='+name+'&orgform=0&fylke=0&kommune=0')
        webbrowser.open('https://www.gulesider.no/person/resultat/'+name)


def browser2():
	webbrowser.open('http://adressesok.posten.no/nb/persons/search?utf8=%E2%9C%93&q='+name+'&token=')
        webbrowser.open('https://w2.brreg.no/enhet/sok/treffliste.jsp?navn='+name+'&orgform=0&fylke=0&kommune=0')
        webbrowser.open('https://www.gulesider.no/person/resultat/'+name)
        webbrowser.open('https://www.norid.no/no/domenenavnbaser/whois/?query='+name+'&sok=S%C3%B8k')
        webbrowser.open('https://www.aksjeeiere.no/?utf8=%E2%9C%93&year=2016&q='+name)


# Start program

while True:
	os.system('clear')
	intro()
	name = raw_input('\x1b[1;33;49m' + '\n>-------[ Name of person or organization: ' + '\x1b[0m')
        posten()
        brreg()
        gulesider()
	print('\x1b[1;31;49m' + '\n>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
        print('\x1b[1;32;49m' + '1. New search' + '\x1b[0m')
	print('\x1b[1;33;49m' + '2. Open search in webbrowser' + '\x1b[0m')
	print('\x1b[1;34;49m' + '3. Open search in webbbrowser, include Norid(whois) and Aksjonaerregisteret(stock)' + '\x1b[0m')
	print('\x1b[1;31;49m' + '4. Quit nOSINTh' + '\x1b[0m')
	print('\x1b[1;31;49m' + '>------------------------------------------------------------------------------+-+-+' + '\x1b[0m')
	valg = input('\x1b[1;33;49m' + '\n>-------[ ' + '\x1b[0m')
        if valg == 1:
                pass
	if valg == 2:
		browser1()
		break
	elif valg == 3:
		browser2()
		break
        elif valg == 4:
		break
        else:
       	    print('\x1b[1;31;49m' + '>-------[ SYNTAX-ERROR-DOES-NOT-COMPUTE\n' + '\x1b[0m')
print('\x1b[1;36;49m' + '\n>---------------------------------------------------ThankYouComeAgain!---------+-+-+\n' + '\x1b[0m')

# End of the line

