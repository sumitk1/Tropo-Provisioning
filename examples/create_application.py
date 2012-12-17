'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning

def testCreateApplication(userName, password, url):
    
    requestBody = { "name":"sumitk1", "voiceUrl":"http://website.com", "messagingUrl":"http://website2.com", "platform":"scripting", "partition":"staging" }
    requestXML =   "<application>\
                        <name>new app</name>\
                        <voiceurl>http://website.com</voiceurl>\
                        <messagingurl>http://website2.com</messagingurl>\
                        <platform>scripting</platform>\
                        <partition>staging</partition>\
                    </application>"
    requestFormEncoded = "name=new+app123&voiceURL=http%3A%2F%2Fwebsite.com&messagingURL=http%3A%2F%2Fwebsite2.com&platform=scripting&partition=staging"
    
    name = "new app2"
    voiceUrl = "http://website2.com"
    messagingUrl = "http://website1.com"
    platform = "scripting"
    partition = "staging"
    
    """tropoTest = TropoProvisioning()
    testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition)
    print "Resp = %s"% testResp
    
    name = "new app2"
    tropoTest = TropoProvisioning(requestType="XML")
    testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition)
    print "Resp = %s"% testResp"""
    
    name = "new app3"
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition, "XML")
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
    
    