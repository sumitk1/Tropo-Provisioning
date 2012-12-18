'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format
          
def testAddIMAccount(username, password, url):
    '''Need to enter a valid IM username and password.
       IM application (gtalk, aim, yahoo etc) needs to give access to Tropo.
    '''
    
    applicationId = "427278"
    tropoTest = TropoProvisioning(requestType=data_format.JSON)
    accountType = "yahoo"
    username = ""
    password = ""
    print tropoTest.add_IM_account(applicationId, accountType, username, password, data_format.JSON)

def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddIMAccount(username, password, url)
    
if __name__ == '__main__':
    main()
    