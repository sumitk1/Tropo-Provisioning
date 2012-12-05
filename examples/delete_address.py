'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning


def testDeleteAddress(username, password, url):
    applicationId = "427278"
    addressType = "number"
    addressValue = "+14077969891"
    tropoTest = TropoProvisioning()
    print tropoTest.delete_address(applicationId, addressType, addressValue)
        
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testDeleteAddress(username, password, url)
    
if __name__ == '__main__':
    main()
    