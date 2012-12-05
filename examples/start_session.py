'''
This is an example script which shows how to use the Tropo Python REST API
'''
from ConfigParser import SafeConfigParser
from TropoProvisioning import TropoProvisioning

def testStartSession(userName, password, url):
    
    requestBody = { "token":"TOKEN", "customerName":"John Dyer", "numberToDial":"4075551212", "msg":"the sky is falling." }
    requestXML =   '<session>\
                    <token>TOKEN</token>\
                    <var name="customerName" value="John Dyer"></var>\
                    <var name="numberToDial" value="4075551212"></var>\
                    <var name="msg" value="the sky is falling"></var>\
                    </session>'
    requestFormEncoded = "token=TOKEN&customerName=John+Dyer&numberToDial=4075551212&msg=the+sky+is+falling"
    token = "TOKEN1234"
    customerName = "John Dyer"
    numberToDial = "4075551212"
    msg = "message"
    
    tropoTest = TropoProvisioning(requestType="JSON")
    testResp = tropoTest.start_session("POST", token, customerName, numberToDial, msg)
    print "Resp = %s"% testResp
    
    #tropoTest = TropoProvisioning(requestType="XML")
    #tropoTest.start_session(requestXML, "POST")
    
    #tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    #tropoTest.start_session(requestFormEncoded, "POST")

    getBody = "action=create&token=TOKEN&numberToDial=4075551212&customerName=John+Dyer&msg=the+sky+is+falling"
    tropoTest = TropoProvisioning(requestType="FORM-ENCODED")
    print tropoTest.start_session("GET", token, customerName, numberToDial, msg)


def main():
    parser = SafeConfigParser()
    
    parser.read('example_config')
    username = parser.get('tropo_api_credentials', 'username')
    password = parser.get('tropo_api_credentials', 'password')
    url = parser.get('tropo_api_credentials', 'url')
    testStartSession(username, password, url)
    
if __name__ == '__main__':
    main() 
    
    