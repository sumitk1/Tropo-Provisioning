'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format


def testAddTollFreeNumber(username, password, url):
    '''
    Need to have production account but its working on a staging account.
    '''
    applicationId = "427278"
    prefix = "1866"
    tropoTest = TropoProvisioning()
    print tropoTest.add_tollFree_number(applicationId, prefix, data_format.JSON)
    
    prefix = "1866"
    tropoTest = TropoProvisioning()
    print tropoTest.add_tollFree_number(applicationId, prefix, data_format.XML)
    
    prefix = "1866"
    tropoTest = TropoProvisioning()
    print tropoTest.add_tollFree_number(applicationId, prefix, data_format.FORM_ENCODED)
          
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddTollFreeNumber(username, password, url)
    
if __name__ == '__main__':
    main()
    