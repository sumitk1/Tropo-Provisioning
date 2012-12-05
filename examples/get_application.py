'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning


def testGetApplication(username, password, url):
    applicationId = "427278"
    tropoTest = TropoProvisioning(username=username, password=password, url=url, requestType="JSON")
    print type(tropoTest.get_application(applicationId))
                
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testGetApplication(username, password, url)
    
if __name__ == '__main__':
    main()
    