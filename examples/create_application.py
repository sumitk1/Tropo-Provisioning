'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning
import data_format

def testCreateApplication(userName, password, url):
    
    name = "new app2"
    voiceUrl = "http://website2.com"
    messagingUrl = "http://website1.com"
    platform = "scripting"
    partition = "staging"
    
    tropoTest = TropoProvisioning()
    testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition, data_format.JSON)
    print "Resp = %s"% testResp
    
    name = "new app2"
    tropoTest = TropoProvisioning(requestType="XML")
    testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition, data_format.XML)
    print "Resp = %s"% testResp
    
    name = "new app3"
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition, data_format.FORM_ENCODED)
    print "Resp = %s"% testResp
    

def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testCreateApplication(username, password, url)
    
if __name__ == '__main__':
    main() 
    
    