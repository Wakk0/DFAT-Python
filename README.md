# Python DFAT LDAP Address Book Creator
* (DFAT: Department of Foreign Affairs and Trade)
* (LDAP: Lightweight Directory Access Protocol)

This python script is to create an ldap entries from data colected from DFAT webpage missions in Australia.
It collects emails, address, First contact (usually who is in charge) and partner as well as the role.

## Installation

Using Debian's package manager:
```bash
apt install python3-bs4 python3-requests
```
Probably this packages are already installed on your linux distribution.

Or using python pip package (on debian python3-pip):
```bash
pip (or pip3) install bs4
pip install requests
```

## Configuration

The only configurable thing is the ou you want to generate
```python
ou_path = 'ou=Embassies,ou=AddressBook,dc=domain,dc=com'
```

## Usage

```bash
python scraper.py > my-ldif-file.ldif
```
## Copyrights

All content generated from this script is attributed to the Department of Foreign Affairs and Trade website - [www.dfat.gov.au](https://www.dfat.gov.au)

From the DFAT's webpage all content generated https://www.dfat.gov.au/about-us/about-this-website/copyright
> "Content from this website should be attributed as Department of Foreign Affairs and Trade website – www.dfat.gov.au"
This script has no intent of misuse of the information. Actually I think is an excellent idea that DFAT offers an LDAP addressbook for all embassies as this information is heavily use for comunication purposes. Browsing/searching on the Web directory is a waste of time to get a contact/phone/email/address/role etc.

## ToDo

- [x] Create the script (hehe).
- [ ] Collect telephone numbers.
- [ ] Clean the code (I think this code is fully tuneable).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GPL-v3](https://choosealicense.com/licenses/gpl-3.0/)