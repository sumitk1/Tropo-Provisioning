'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format

  
def testUpdateApplication(username, password, url):
    applicationId = "427278"
    name = "new app updated11"
    platform = "webapi"
    partition = "staging"
    
    tropoTest = TropoProvisioning()
    print tropoTest.update_application(applicationId, name, platform, partition, data_format.JSON)

    
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testUpdateApplication(username, password, url)
    
if __name__ == '__main__':
    main()
    