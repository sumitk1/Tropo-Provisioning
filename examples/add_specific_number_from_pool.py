'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format

def testAddSpecificNumber(username, password, url):
    applicationId = "427278"
    number = "4077969837"
    tropoTest = TropoProvisioning(username=username, password=password, url=url)
    print tropoTest.add_specific_number_from_pool(applicationId, number, data_format.JSON)
    
    number = "4077969844"
    tropoTest = TropoProvisioning(requestType="XML")
    print tropoTest.add_specific_number_from_pool(applicationId, number, data_format.XML)
    
    number = "4077969838"
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    print tropoTest.add_specific_number_from_pool(applicationId, number, data_format.FORM_ENCODED)
            
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddSpecificNumber(username, password, url)
    
if __name__ == '__main__':
    main()
    