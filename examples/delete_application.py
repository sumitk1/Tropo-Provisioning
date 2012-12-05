'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning

  
def testDeleteApplication(username, password, url):
    applicationId = "427728"
    tropoTest = TropoProvisioning()
    print tropoTest.delete_application(applicationId)
    
    # 423373 423325 423315  423244 423198 423196 423194 423132

def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testDeleteApplication(username, password, url)
    
if __name__ == '__main__':
    main()
    