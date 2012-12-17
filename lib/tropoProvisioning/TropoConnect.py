'''
@author: sumitk
'''
import base64
import json
import urllib2

class RequestWithMethod(urllib2.Request):
    """Workaround for using DELETE with urllib2"""
    def __init__(self, url, method, data=None, headers={}, origin_req_host=None, unverifiable=False):
        self._method = method
        urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)

    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self)
   
   
def doPOST(userName, password, url, postVal, requestType):
    return doBasicAuth(userName, password, url, postVal, 'POST', requestType)

def doPUT(userName, password, url, postVal, requestType):
    return doBasicAuth(userName, password, url, postVal, 'PUT', requestType)

def doDELETE(userName, password, url, requestType):
    return doBasicAuth(userName, password, url, '', 'DELETE', requestType)

def doGET(userName, password, url, requestType):
    return doBasicAuth(userName, password, url, '', 'GET', requestType)

def doBasicAuth(userName, password, url, postVal = None, method = None, requestType = None, proxy = None):
    
    """
    This function helps in setting up the auth header and do the basic auth.
    """
    encodedstring = base64.encodestring("%s:%s" % (userName, password))[:-1]
    auth = "Basic %s" % encodedstring
    responseObj = {"responseCode" : "200", "responseValue" : "value"}
    
    try:
        
        postData = None
        if postVal is not None and requestType == "JSON":
            postData = json.dumps(postVal)
        else:
            postData = postVal

        req = RequestWithMethod(url, method, postData, {"Authorization": auth })
        
        if requestType=="JSON":
            req.add_header("accept", "application/json")
            req.add_header("content-type", "application/json")
        elif requestType=="XML":
            req.add_header("accept", "text/xml")
            req.add_header("content-type", "text/xml")
        elif requestType=="FORM-ENCODED":
            req.add_header("content-type", "application/x-www-form-urlencoded")
        else :
            req.add_header("accept", "application/json")
            req.add_header("content-type", "application/json")
            
        
        handler = urllib2.urlopen(req)
        
    except urllib2.HTTPError, e:
        responseObj[u'responseCode'] = e.code
        responseObj[u'responseValue'] = e 
        return responseObj
        
    if requestType == "JSON":
        response = json.load(handler)
    else:
        response = handler.read()
    
    code = (vars(handler))
    responseObj[u'responseCode'] = code[u'code']
    responseObj[u'responseValue'] = response 
    return responseObj
        
