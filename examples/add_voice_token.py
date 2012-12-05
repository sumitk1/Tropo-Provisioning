'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning

  
def testAddVoiceToken(username, password, url):
    
    applicationId = "427278"
    field_type = "token" 
    field_channel = "voice"
    
    tropoTest = TropoProvisioning()
    print tropoTest.add_voice_token(applicationId, field_type, field_channel)
    
    tropoTest = TropoProvisioning(requestType="XML")
    print tropoTest.add_voice_token(applicationId, field_type, field_channel)
    
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    print tropoTest.add_voice_token(applicationId, field_type, field_channel)
    
def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddVoiceToken(username, password, url)
    
if __name__ == '__main__':
    main()
    