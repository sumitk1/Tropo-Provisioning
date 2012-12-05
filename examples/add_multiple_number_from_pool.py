'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning

def testAddMultipleNumbersFromPool(username, password, url):
    applicationId = "427278"
    prefix = 1407
    count = 2
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    print tropoTest.add_multiple_numbers_from_pool(applicationId, prefix, count)
        

def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddMultipleNumbersFromPool(username, password, url)
    
if __name__ == '__main__':
    main()
    