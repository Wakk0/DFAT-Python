import requests
from bs4 import BeautifulSoup as bs

def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email
    # thanks to https://usamaejaz.com/cloudflare-email-decoding/

headers= { 'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; nl; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13'}

dfat_base_url = 'https://protocol.dfat.gov.au/'
all_missions_path = 'Public/MissionsInAustralia/'
ou_path = 'ou=Embassies,ou=AddressBook,dc=domain,dc=com'

# Helper Functions
def parsePerson(data):
	fullperson = []
	if(data):
		html_parsed = data.find_all('p')
		list_name = list(html_parsed[0].stripped_strings)
		full_name = f'{list_name[0]} {list_name[1]}'
		fullperson.append(full_name)
		list_role = list(html_parsed[1].stripped_strings)
		role = list_role[0].strip().replace('\n',' ')
		fullperson.append(role)
		if(str(html_parsed[2]) != '<p class="pl-4"> <strong></strong></p>'):
			list_partner = list(html_parsed[2].stripped_strings)
			partner_name = f'{list_partner[0]} {list_partner[1]}'
			fullperson.append(partner_name)
		else:
			fullperson.append('No partner')
		return fullperson
	else:
		return ['No data','No data','No data']

def parseAddress(data):
	addresses = []
	for address in data:
		if(address.find('p',class_='h5')):
			data_site = address.find_all('p')
			if(len(data_site) == 2):
				site_address = list(data_site[1].stripped_strings)
				addresses.append([data_site[0].string, site_address[1].replace('\n',' ').replace(' , ',', ')])
			else:
				addresses.append([data_site[0].string, 'No Address Registered'])
	return addresses

# Helper Functions END

missions_index_html = requests.get(dfat_base_url+all_missions_path,headers=headers)

index = bs(missions_index_html.content,'html.parser')
missions = index.select('p a')

for country in missions:
	mission_html = requests.get(dfat_base_url+country.get('href'), headers=headers)
	mission_data = bs(mission_html.content, 'html.parser')

	emails = mission_data.find_all('span', class_='__cf_email__')
	for i in range(len(emails)):
		the_country = country.string.replace(',','')
		email = cfDecodeEmail(emails[i].get('data-cfemail'))
		sites = mission_data.find_all('div', class_='col-lg-6 col-md-12')
		people = mission_data.find('div', class_='list-group-item')
		embassy = mission_data.find('h4',class_='text-primary')
		address = parseAddress(sites)
		# for person in people:
		data_person = parsePerson(people)

		print(f'dn: cn={the_country}{i},{ou_path}')
		print(f'ou: {address[0][0]}')
		print(f'cn: {embassy.string}')
		print(f'sn: {embassy.string}')
		print(f'mail: {email}')
		print(f'givenName: {data_person[0]}')
		print(f'o: {country.string}')
		print(f'title: {data_person[1]}')
		print(f'description: {data_person[2]}')
		print(f'postalAddress: {address[0][1]}')
		print('objectClass: top')
		print('objectClass: inetOrgPerson')
		print('')