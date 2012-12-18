'''
@author: sumit
'''

from TropoLogger import TropoLogger
import ConfigParser
import TropoConnect
import TropoException
import data_format
import json
import os
import sys
import urllib

__all__ = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'MyLibrary']
[DEBUG, INFO, WARNING, ERROR] = range(4)

            
class TropoProvisioning(object):
    '''
    TropoProvisioning class is a wrapper that provides an easy way to access Tropo Provisioning REST API.
    It defines a set of methods to create, update, retrieve or delete different kind of resources.
    '''
    
    def __init__(self, **kwargs):
        '''
        
        The object of this class can now be instantiated in two ways:
        
        1. Having no arguments in the constructor:
            tropoTest = TropoProvisioning()
        
        2. Having variable number of named arguments in the constructor (in any order):
            tropoTest = TropoProvisioning(userName="xxx", password="yyy")
            tropoTest = TropoProvisioning(userName="xxx", password="yyy", url="www")
            tropoTest = TropoProvisioning(url="www", userName="xxx", password="yyy",  requestType="type")
            tropoTest = TropoProvisioning(url="www", requestType="type")
        
        The default values if not specified in the constructor will be taken from the config.cfg
        
        requestType can be one of these three - JSON, XML, FORM-ENCODED and defaults to JSON
        '''
       
        config = ConfigParser.ConfigParser()
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.cfg')
        config.read(config_path)
        
        if(kwargs.get('userName') is None):
            self.userName = config.get('tropo_api_config', 'userName')
        else:
            self.userName = kwargs.get('userName')
        
        if(kwargs.get('password') is None):
            self.password = config.get('tropo_api_config', 'password')
        else:
            self.password = kwargs.get('password')
            
        if(kwargs.get('url') is None):
            self.url = config.get('tropo_api_config', 'url')
        else:
            self.url = kwargs.get('url')
        
        if(kwargs.get('requestType') is None):
            self.requestType = config.get('tropo_api_config', 'requestType')
        else:
            self.requestType = kwargs.get('requestType')
        
        self.log_level = DEBUG
        self.tropo_logger_inst = TropoLogger(self.userName, self.custom_logger)    

    def custom_logger(self, severity, string):
        '''
        Logger implementation
        '''
        if severity >= self.log_level:
            print string
            
    def preconditionCheck(self):
        '''
        Precondition check before calling each API to make sure the auth credentials are set properly.
        Throws exception if credentials not set.
        '''
        try:
            if (self.userName is None) or (not self.userName):
                raise TropoException.UserNameNotSetException("UserName is not set")
            if (self.password is None) or (not self.password):
                raise TropoException.PasswordNotSetException("Password is not set")
            if (self.url is None) or (not self.url):
                raise TropoException.UrlNotSetException("URL is not set")
        except TropoException.UserNameNotSetException, (instance):
            print "Exception Caught: " + instance.parameter
            raise instance
        except TropoException.PasswordNotSetException, (instance):
            print "Exception Caught: " + instance.parameter
            raise instance
        except TropoException.UrlNotSetException, (instance):
            print "Exception Caught: " + instance.parameter
            raise instance

    '''
    REST API for Session
    '''

    def start_session(self, method, token=None, customerName=None, numberToDial=None, msg=None, request_format=None):
        """ 
        Create a new Application
        
        @param token               The token for the session
        @param customerName        The name of the customer
        @param numberToDial        The number to dial
        @param msg                 The message body
        
        @return: Dict response      The response from the REST API call as a dict containing token
        """
        self.preconditionCheck()
        if(token is None):
            return "Token is not set."
        if(request_format is not None):
            self.requestType = request_format
            
        postBody = ""
        resource = "https://api.tropo.com/1.0/sessions"
        
        if (method == "POST"):
            
            if self.requestType == data_format.JSON:
                postBody = {"token": token, "customerName": customerName, "numberToDial": numberToDial, "msg": msg}
                print postBody
                response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
            
            elif self.requestType == data_format.XML:
                postBody = "<session><token>%s</token><var name=\"customerName\" value=\"%s\"></var><var name=\"numberToDial\" value=\"%s\"></var><var name=\"msg\" value=\"%s\"></var></session>" % (token, customerName, numberToDial, msg)
                response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                                 
            elif self.requestType == data_format.FORM_ENCODED:
                postBody = "token=%s&customerName=%s&numberToDial=%s&msg=%s" % (token, customerName, numberToDial, msg) 
                response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
            else:
                return "Bad request type."
            
            self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
            self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
            
            if (response[u'responseCode'] == 200):
                if(self.requestType == data_format.JSON):
                    result = response[u'responseValue']
                    return result               # returns a list
                else:
                    result = response[u'responseValue']
                return result
            else:        
                return "Starting Session failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
            
             
        if (method == "GET"):
            params = urllib.urlencode({"token": token, "customerName": customerName, "numberToDial": numberToDial, "msg": msg})
            resource = resource + "?action=create&%s" % (params)
            print resource
            response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
            
            self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
            self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
            
            if (response[u'responseCode'] == 200):
                if(self.requestType == data_format.JSON):
                    result = response[u'responseValue']
                    return result               # returns a list
                else:
                    result = response[u'responseValue']
                return result
            else:        
                return "Starting Session failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        
               
    def start_session_webApi(self, method, token=None, request_format=None):
        """ 
        Create a new WebApi Session
        
        @param token        The body of the request
        
        @return: Dict response      The response from the REST API call as a dict containing token
        """
        self.preconditionCheck()
        if(token is None):
            return "Token is not set."
        if(request_format is not None):
            self.requestType = request_format
            
        resource = "https://api.tropo.com/1.0/sessions"
        # resource = "https://api.tropo.com/1.0/sessions?action=create&token=TOKEN&numberToDial=4075551212&customerName=John+Dyer&msg=the+sky+is+falling"
        
        if (method == "POST"):
            
            if self.requestType == data_format.JSON:
                postBody = {"token": token}
                print postBody
                response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
            
            elif self.requestType == data_format.XML:
                postBody = "<session><token>%s</token></session>" % (token)
                response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                                 
            elif self.requestType == data_format.FORM_ENCODED:
                postBody = "token=%s" % (token) 
                response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
            else:
                return "Bad request type."
            
            self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
            self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
            
            if (response[u'responseCode'] == 200):
                if(self.requestType == data_format.JSON):
                    result = response[u'responseValue']
                    return result               # returns a list
                else:
                    result = response[u'responseValue']
                return result
            else:        
                return "Starting Session-WebApi failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
            
             
        if (method == "GET"):
            resource = resource + "?action=create&token=" + token
            print resource
            response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
            
            self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
            self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
            
            if (response[u'responseCode'] == 200):
                if(self.requestType == data_format.JSON):
                    result = response[u'responseValue']
                    return result               # returns a list
                else:
                    result = response[u'responseValue']
                return result
            else:        
                return "Starting Session-WebApi failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        
    
    '''
    REST API for Provisioning
    '''           
    def create_application(self, name=None, voiceUrl=None, messagingUrl=None, platform=None, partition=None, request_format=None):
        """ 
        Create a new Application
        
        @param name            The name of the application
        @param voiceUrl        The name of the application
        @param messagingUrl    The name of the application
        @param platform        The name of the application
        @param partition       The name of the application
        
        @return: String application       The ID of the new application created if request-type is JSON. Full response with application url otherwise.
        """
        self.preconditionCheck()
        
        # if(name is None and voiceUrl is None and messagingUrl is None and platform is None and partition is None):
        #    return "Create Application failed as none of the field is set"
        
        if(request_format is not None):
            self.requestType = request_format
        
        resource = self.url + "applications" 
        
        if self.requestType == data_format.JSON:
            
            postBody = {"name": name, "voiceUrl": voiceUrl, "messagingUrl": messagingUrl, "platform": platform, "partition": partition}
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            print "here"
            postBody = "<application><name>%s</name><voiceurl>%s</voiceurl><messagingurl>%s</messagingurl><platform>%s</platform><partition>%s</partition></application>" % (name, voiceUrl, messagingUrl, platform, partition)
            print postBody
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "name=%s&voiceURL=%s&messagingURL=%s&platform=%s&partition=%s" % (name, voiceUrl, messagingUrl, platform, partition)
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Create Application failed."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Create Application failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
               

    def add_single_number_from_pool(self, applicationId, prefix, request_format=None):
        """ 
        Add a number to the Application
        
        @param applicationId       The ID of the application to which the number has to be added
        @param prefix              The country prefix where you want to have a single number

        @return response          The number added to the application if headers is JSON. Full response body otherwise.
        """
        
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId + "/addresses"
        
        if self.requestType == data_format.JSON:
            postBody = {"type":"number", "prefix":prefix}
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            postBody = "<address><type>number</type><prefix>%s</prefix></address>" % (prefix)
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "type=number&prefix=%s" % (prefix) 
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Adding Number to an Account failed."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Adding Number to an Account failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
               
        
    def add_multiple_numbers_from_pool(self, applicationId, prefix, count, request_format=None):
        """ 
        Add multiple numbers to the Application
        
        @param applicationId       The ID of the application to which the number has to be added
        @param prefix              The country prefix where the numbers will be added
        @param count               The count of numbers that will be added to the application
        
        @return: Array response         The array of the numbers added to the application if Headers is JSON. Array of full response body otherwise.
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        response = []
        if(count > 0):
            for i in range(count):
                response.append(self.add_single_number_from_pool(applicationId, prefix, self.requestType))
        
        return response
    

    def add_specific_number_from_pool(self, applicationId, number, request_format=None):
        """ 
        Add a specific number to the Application
        
        @param applicationId     The ID of the application to which the number has to be added
        @param number            The number to be added
        
        @return: response        The number added to the application if headers is JSON. Full response body otherwise.
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId + "/addresses"
        
        if self.requestType == data_format.JSON:
            postBody = {"type":"number", "number":number}
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            postBody = "<address><type>number</type><number>%s</number></address>" % (number)
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "type=number&number=%s" % (number) 
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Bad request type."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Adding Specific Number to an Account failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        
                

    def add_tollFree_number(self, applicationId, prefix, request_format=None):
        """ 
        Add a toll-free number to the Application
        
        @param applicationId     The ID of the application to which the number has to be added
        @param prefix            The prefix for the toll free number
        
        @return: response        The toll free number added to the application if headers is JSON. Full response body otherwise.
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId + "/addresses"
        
        if self.requestType == data_format.JSON:
            postBody = {"type":"number", "prefix":prefix}
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            postBody = "<address><type>number</type><prefix>%s</prefix></address>" % (prefix)
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "type=number&prefix=%s" % (prefix) 
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Bad request type."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Adding Toll Free Number to an Account failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
               

    def add_international_number_from_pool(self, applicationId, prefix, request_format=None):
        """ 
        Add an international number to the Application
        
        @param applicationId       The ID of the application to which the number has to be added
        @param prefix              The country code prefix where the number will be added
        
        @return: response         The international number added to the application if Headers is JSON. Full response body otherwise.
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId + "/addresses"
        
        if self.requestType == data_format.JSON:
            postBody = {"type":"number", "prefix":prefix}
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            postBody = "<address><type>number</type><prefix>%s</prefix></address>" % (prefix)
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "type=number&prefix=%s" % (prefix) 
            print postBody
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Bad request type."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Adding International Number failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
                   

    def add_IM_account(self, applicationId, accountType, username, password, request_format=None):
        """ 
        Add an IM account (Gmail / AIM / Yahoo etc) to the Application
        
        @param applicationId       The ID of the application to which the IM account has to be added
        @param accountType         The type of the IM account that needs to be added
        @param username            The username of that IM account
        @param password            The password to that IM account
        
        @return: response          The URL of the IM account added
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId + "/addresses"
        
        if self.requestType == data_format.JSON:
            postBody = {"type":accountType, "username":username, "password":password}
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            postBody = "<address><type>%s</type><username>%s</username><password>%s</password></address>" % (accountType, username, password)
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "type=%s&username=%s&password=%s" % (accountType, username, password) 
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Bad request type."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href']
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Add IM Account failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        

    def add_voice_token(self, applicationId, field_type, field_channel, request_format=None):
        """ 
        Add a voice token to the Application
        
        @param applicationId         The ID of the application to which the voice token has to be added
        @param field_type            The type 
        @param field_channel         The channel 
        
        @return: response            The token for that channel if headers is JSON. Full URL for that voice token otherwise.
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId + "/addresses"
        
        if self.requestType == data_format.JSON:
            postBody = {"type":field_type, "channel":field_channel}
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            postBody = "<address><type>%s</type><channel>%s</channel></address>" % (field_type, field_channel)
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "type=%s&channel=%s" % (field_type, field_channel) 
            response = TropoConnect.doPOST(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Bad request type."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Adding Voice Token failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        

    def add_voice_messaging_url(self, applicationId, voiceUrl=None, messagingUrl=None, request_format=None):
        """ 
        Add a voice and message URL to the Application
        
        @param applicationId        The ID of the application to which the voice & message url has to be added
        @param voiceUrl             The Voice URL for that application
        @param messagingUrl         The Messaging URL for that application
        
        @return: string response         The applicationID is headers is JSON. Full response body otherwise.
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        if(voiceUrl is None and messagingUrl is None):
            return "Adding Voice & Messaging URLs failed as there is nothing to add"
        
        resource = self.url + "applications/" + applicationId 
        
        if self.requestType == data_format.JSON:
            if(voiceUrl is not None and messagingUrl is not None):
                postBody = {"voiceUrl":voiceUrl, "messagingUrl":messagingUrl}
            elif(voiceUrl is not None):
                postBody = {"voiceUrl":voiceUrl}
            elif(messagingUrl is not None):        
                postBody = {"messagingUrl":messagingUrl}
            
            response = TropoConnect.doPUT(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            if(voiceUrl is not None and messagingUrl is not None):
                postBody = "<application><voiceurl>%s</voiceurl><messagingurl>%s</messagingurl></application>" % (voiceUrl, messagingUrl)
            elif(voiceUrl is not None):
                postBody = "<application><voiceurl>%s</voiceurl></application>" % (voiceUrl)
            elif(messagingUrl is not None):        
                postBody = "<application><messagingurl>%s</messagingurl></application>" % (messagingUrl)
            
            response = TropoConnect.doPUT(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            if(voiceUrl is not None and messagingUrl is not None):
                postBody = "voiceURL=%s&messagingURL=%s" % (voiceUrl, messagingUrl)
            elif(voiceUrl is not None):
                postBody = "voiceURL=%s" % (voiceUrl)
            elif(messagingUrl is not None):        
                postBody = "messagingURL=%s" % (messagingUrl)
            
            response = TropoConnect.doPUT(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Bad request type."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Adding Voice & Messaging URLs failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        

    def update_application(self, applicationId, name=None, platform=None, partition=None, request_format=None):
        """ 
        Update the Application
        
        @param applicationId        The ID of the application which has to be updated
        @param name                 The name of the application
        @param platform             The platform of the application
        @param partition            The partition of the application
        
        @return: response         The applicationID if headers is JSON. Full response body otherwise.
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        if(name is None and platform is None and partition is None):
            return "At least one of the parameter (name, platform, partition) needs to be set."
        
        resource = self.url + "applications/" + applicationId 
        
        if self.requestType == data_format.JSON:
            postBody = {"name": name, "platform": platform, "partition": partition}
            print postBody
            response = TropoConnect.doPUT(self.userName, self.password, resource, postBody, self.requestType)
        
        elif self.requestType == data_format.XML:
            postBody = "<application><name>%s</name><platform>%s</platform><partition>%s</partition></application>" % (name, platform, partition)
            response = TropoConnect.doPUT(self.userName, self.password, resource, postBody, self.requestType)
                             
        elif self.requestType == data_format.FORM_ENCODED:
            postBody = "name=%s&platform=%s&partition=%s" % (name, platform, partition) 
            response = TropoConnect.doPUT(self.userName, self.password, resource, postBody, self.requestType)
        else:
            return "Bad request type."
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'href'].rpartition('/')[2]
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Update Application failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
                       

    def delete_application(self, applicationID, request_format=None):
        """ 
        Delete Application
        
        @param applicationId     The ID of the application which has to be deleted
        
        @return: response         The response message
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationID
        response = TropoConnect.doDELETE(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue'][u'message']
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Delete Application failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        
       
        
    def delete_address(self, applicationID, addressType, addressValue, request_format=None):
        """ 
        Delete an address from the Application
        
        @param applicationId       The ID of the application from which the address has to be deleted
        @param addressType         The type of the address to be deleted
        @param addressValue        The value of the address to be deleted
        
        @return: response         The response message
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationID + "/addresses/" + addressType + "/" + addressValue
        response = TropoConnect.doDELETE(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue']
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Delete Address failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
                

    def get_all_applications(self, request_format=None):
        """ 
        Get all the Application associated with the account
        
        @return: List response         The list of all the Applications with all their details.
        """
                 
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications"
        response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue']
                return result               # returns a list
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Getting All Applications failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
                       
        
    def get_application(self, applicationId, request_format=None):
        """ 
        Get all the Application associated with the account
        
        @param applicationId      The ID of the application 
        
        @return: List response         The list of all the details for that application
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId
        response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue']
                return result               # returns a list
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Getting Application failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])     
        
        
    def get_application_addresses(self, applicationId, request_format=None):
        """ 
        Get all the Application's addresses associated with it
        
        @param applicationId           The ID of the application 
        
        @return: List response         The list of all the addresses associated with an application
        """
        
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "applications/" + applicationId + "/addresses"
        response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue']
                return result               # returns a list
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Getting Application Addresses failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
                

    def get_all_addresses_for_account(self, request_format=None):
        """
        Get all the addresses associated with the account
        
        @return: Array response         The response from the REST API call
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "addresses"
        response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue']
                return result               # returns a list
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Getting All Addresses failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
                

    def get_all_available_exchanges_for_account(self, request_format=None):
        """ 
        Get all the exchanges associated with the account
        
        @return: List response         The list of all the exchanges
        """
                   
        self.preconditionCheck()
        if(request_format is not None):
            self.requestType = request_format
            
        resource = self.url + "exchanges"
        response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue']
                return result               # returns a list
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Getting All Available Exchanges failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])
        
        
    def get_all_available_prefixes_for_account(self, prefix, request_format=None):
        """ 
        Get all the available prefixes for the account
        
        @return: string response         The response from the REST API call
        """
                   
        self.preconditionCheck()
        
        if(prefix is None):
            return "Prefix is not set. Please set it and try again!"
        if(request_format is not None):
            self.requestType = request_format
        
        resource = self.url + "addresses?available&prefix=" + prefix
        response = TropoConnect.doGET(self.userName, self.password, resource, self.requestType)
        
        self.tropo_logger_inst.logger(DEBUG, "ResponseCode = %s" % response[u'responseCode'])
        self.tropo_logger_inst.logger(DEBUG, "ResponseValue = %s" % response[u'responseValue'])   
        
        if (response[u'responseCode'] == 200):
            if(self.requestType == data_format.JSON):
                result = response[u'responseValue']
                return result               # returns a list
            else:
                result = response[u'responseValue']
            return result
        else:        
            return "Getting All Available Prefixes failed with the following reason: (Error Code = %s) (Error msg = %s)" % (response[u'responseCode'], response[u'responseValue'])




