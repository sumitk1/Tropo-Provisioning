'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning


def testGetAllAvailablePrefixesForAccount(username, password, url):
    prefix = "9723"
    tropoTest = TropoProvisioning()
    print tropoTest.get_all_available_prefixes_for_account(prefix)[2]
    
    
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testGetAllAvailablePrefixesForAccount(username, password, url)
    
if __name__ == '__main__':
    main()
    