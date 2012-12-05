'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning

def testStartSession(userName, password, url):
    
    token="TOKEN123123"
    
    tropoTest = TropoProvisioning(requestType="XML")
    testResp = tropoTest.start_session_webApi("POST", token)
    print "Resp = %s"% testResp
    
    #tropoTest = TropoProvisioning(requestType="XML")
    #tropoTest.start_session(requestXML, "POST")
    
    #tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    #tropoTest.start_session(requestFormEncoded, "POST")
    
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    print tropoTest.start_session_webApi("GET", token)


def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testStartSession(username, password, url)
    
if __name__ == '__main__':
    main() 
    
    