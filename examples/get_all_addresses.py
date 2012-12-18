'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning


def testGetAllAddressesForAccount(username, password, url):
    tropoTest = TropoProvisioning(username=username, password=password)
    print tropoTest.get_all_addresses_for_account()                    

def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testGetAllAddressesForAccount(username, password, url)
    
if __name__ == '__main__':
    main()
    