'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format


def testGetApplication(username, password, url):
    applicationId = "430603"
    tropoTest = TropoProvisioning(username=username, password=password, url=url, requestType="JSON")
    print tropoTest.get_application(applicationId, data_format.JSON)
                
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testGetApplication(username, password, url)
    
if __name__ == '__main__':
    main()
    