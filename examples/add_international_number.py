'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format


def testAddInternationalNumber(username, password, url):
    applicationId = "427279"
    prefix = 31
    tropoTest = TropoProvisioning(requestType=data_format.JSON)
    print tropoTest.add_international_number_from_pool(applicationId, prefix)    
    
    tropoTest = TropoProvisioning(requestType=data_format.XML)
    print tropoTest.add_international_number_from_pool(applicationId, prefix)    
    
    # It's always giving 400
    tropoTest = TropoProvisioning(requestType=data_format.FORM_ENCODED)
    print tropoTest.add_international_number_from_pool(applicationId, prefix)    
          
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddInternationalNumber(username, password, url)
    
if __name__ == '__main__':
    main()
    
    
