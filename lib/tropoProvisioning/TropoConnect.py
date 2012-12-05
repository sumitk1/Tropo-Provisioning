'''
@author: sumitk
'''
import base64
import cookielib
import json
import re
import sys
import urllib
import urllib2
import pprint

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
    #return connect(userName, password, url, postVal, 'POST')
    return doBasicAuth(userName, password, url, postVal, 'POST', requestType)

def doPUT(userName, password, url, postVal, requestType):
    #return connect(userName, password, url, postVal, 'POST')
    return doBasicAuth(userName, password, url, postVal, 'PUT', requestType)

def doDELETE(userName, password, url, requestType):
    #return connect(userName, password, url, '', 'DELETE')
    return doBasicAuth(userName, password, url, '', 'DELETE', requestType)

def doGET(userName, password, url, requestType):
    #return connect(userName, password, url, '', 'GET')
    return doBasicAuth(userName, password, url, '', 'GET', requestType)

def doBasicAuth(userName, password, url, postVal = None, method = None, requestType = None, proxy = None):
    
    """
    This function helps in setting up the auth header and do the basic auth.
    """
    encodedstring = base64.encodestring("%s:%s" % (userName, password))[:-1]
    auth = "Basic %s" % encodedstring
    responseObj = {"responseCode" : "200", "responseValue" : "value"}
    
    opener = None
    cj = cookielib.LWPCookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cj)
    if proxy:
        proxy_handler = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(cookie_handler, proxy_handler)
    else:
        opener = urllib2.build_opener(cookie_handler)
    
    try:
        #req = urllib2.Request(url, postVal, {"Authorization": auth })
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
            #print "No Headers"
            req.add_header("accept", "application/json")
            req.add_header("content-type", "application/json")
            
        #print vars(req)
        handler = urllib2.urlopen(req)
        #handler = opener.open(req)
        
    except urllib2.HTTPError, e:
        responseObj[u'responseCode'] = e.code
        responseObj[u'responseValue'] = e 
        return responseObj
        
    #response = handler.read()
    if requestType == "JSON":
        response = json.load(handler)
    else:
        response = handler.read()
    
    code = (vars(handler))
    responseObj[u'responseCode'] = code[u'code']
    responseObj[u'responseValue'] = response 
    """print code
    print "--"
    print code[u'code']
    print "---"
    print responseObj
    print "-----"
    """
    return responseObj
        
def connect(userName, password, url, postVal = None, method = None):
    
    """
    This function makes two calls to the same URL. 
    This is to determine if the page is really protected by password.
    If it is then it will set the correct headers and again call the page.
    """
    postData = None
    if(postVal  != ''):
        postData = urllib.urlencode(postVal)
    
    if(method == ''):
        req = urllib2.Request(url, postData)
    else:
        req = RequestWithMethod(url, method, postData)
    
    try:
        handle = urllib2.urlopen(req)
    except IOError, e:
        # here we *want* to fail
        pass
    else:
        # If we don't fail then the page isn't protected
        print "This page isn't protected by authentication."
        sys.exit(1)
    
    if not hasattr(e, 'code') or e.code != 401:
        # we got an error - but not a 401 error
        print "This page isn't protected by authentication."
        print 'But we failed for another reason.'
        sys.exit(1)
    
    authline = e.headers['www-authenticate']
    # Gets the www-authenticate line from the headers which has the authentication scheme and realm in it
    
    authobj = re.compile(r'''(?:\s*www-authenticate\s*:)?\s*(\w*)\s+realm=['"]([^'"]+)['"]''', re.IGNORECASE)
    # Reg-Ex used to extract scheme and realm
    matchobj = authobj.match(authline)
    
    if not matchobj:
        # if the authline isn't matched by the regular expression then something is wrong
        print 'The authentication header is badly formed.'
        print authline
        sys.exit(1)
    
    scheme = matchobj.group(1)
    # realm = matchobj.group(2)
    # Extracted the scheme and the realm from the header
    if scheme.lower() != 'basic':
        print 'This can only works with BASIC authentication.'
        sys.exit(1)
    
    base64string = base64.encodestring('%s:%s' % (userName, password))[:-1]
    authheader =  "Basic %s" % base64string
    req.add_header("Authorization", authheader)
    req.add_header("accept", "application/json")
    req.add_header("content-type", "application/json")
    
    try:
        handle = urllib2.urlopen(req)
    except IOError, e:
        # here we shouldn't fail if the username/password is right
        print "goddammit.. something went wrong! We got the following error code from server:"
        print e.code
        print "Check the call to the web service API for correct parameters."
        sys.exit(1)
    response = handle.read()
    return response




