'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format


def testAddNumberFromPool(username, password, url):
        applicationId = "427278"
        prefix = 1407
        tropoTest = TropoProvisioning()
        print tropoTest.add_single_number_from_pool(applicationId, prefix, data_format.JSON)
        
        tropoTest = TropoProvisioning()
        print tropoTest.add_single_number_from_pool(applicationId, prefix, data_format.XML)
        
        tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
        print tropoTest.add_single_number_from_pool(applicationId, prefix, data_format.FORM_ENCODED)
        

def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddNumberFromPool(username, password, url)
    
if __name__ == '__main__':
    main()
    