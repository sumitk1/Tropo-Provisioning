'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning

  

def testAddVoiceMessagingURL(username, password, url):
    requestBody = { "name":"new app", "voiceUrl":"http://website1.com", "messagingUrl":"http://website2.com", "platform":"scripting", "partition":"staging"}
    applicationId = "427278"
    
    voiceUrl = "http://website1.com"
    messagingUrl = "http://website1.com"
    tropoTest = TropoProvisioning()
    print tropoTest.add_voice_messaging_url(applicationId, voiceUrl, messagingUrl)

    voiceUrl = "http://website2.com"
    messagingUrl = "http://website2.com"
    tropoTest = TropoProvisioning(requestType="XML")
    print tropoTest.add_voice_messaging_url(applicationId, voiceUrl, messagingUrl)

    voiceUrl = "http://website3.com"
    messagingUrl = "http://website3.com"
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    print tropoTest.add_voice_messaging_url(applicationId, voiceUrl, messagingUrl)

def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testAddVoiceMessagingURL(username, password, url)
    
if __name__ == '__main__':
    main()
    