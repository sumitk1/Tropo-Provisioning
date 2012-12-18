'''
@author: sumitk
'''

import unittest 
import sys

from TropoProvisioning import TropoProvisioning
import TropoLogger
import data_format

class TropoTest(unittest.TestCase):

    # Use your credentials 

    URL = 'https://api.tropo.com/v1/applications'
    USER_NAME = 'sumitk85'
    PASSWORD = 'qazwsx123'  
    POST_VAL = {"name":"sumitk5", 
          "voiceUrl":"http://website.com", 
          "messagingUrl":"http://website2.com",
          "platform":"scripting", 
          "partition":"staging"}
            
    def test_CreateApplication_successful(self):
        name = "new app1"
        voiceUrl = "http://website1.com"
        messagingUrl = "http://website1.com"
        platform = "scripting"
        partition = "staging"
        
        tropoTest = TropoProvisioning()
        testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition, data_format.JSON)
        print "Resp = %s"% testResp
        result = testResp.find("failed")
        self.assertEqual(result, -1)

    def test_CreateApplication_failed(self):
        name = "new app1"
        voiceUrl = "http://website1.com"
        messagingUrl = "http://website1.com"
        platform = "scripting"
        partition = "staging"
        
        tropoTest = TropoProvisioning()
        testResp = tropoTest.create_application(name, voiceUrl, messagingUrl, platform, partition, "data_format.JSON")
        print "Resp = %s"% testResp
        result = testResp.find("failed")
        self.assertNotEqual(result, -1)

    def test_AddInternationalNumber_successful(self):
        applicationId = "430603"
        prefix = 31
        tropoTest = TropoProvisioning()
        response = tropoTest.add_international_number_from_pool(applicationId, prefix, data_format.JSON)    
        print "Response = %s"% response
        
        
            
"""    def testAddNumberFromPool(self):
        requestBody = {"type":"number", "prefix":"1407"}
        applicationId = "422451"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.add_single_number_from_pool(requestBody, applicationId)

    def testAddMultipleNumbersFromPool(self):
        requestBody = {"type":"number", "prefix":"1407"}
        applicationId = "422451"
        count = 5
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.add_multiple_numbers_from_pool(requestBody, applicationId, count)

    def testAddSpecificNumber(self):
        requestBody = {"type":"number", "number":"4077969880"}
        applicationId = "422446"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.add_specific_number_from_pool(requestBody, applicationId)

    def testAddTollFreeNumber(self):
        requestBody = {"type":"number", "prefix":"1866"} # Need to have production account to test
        applicationId = "422446"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.add_tollFree_number(requestBody, applicationId)



    def testAddVoiceToken(self):
        requestBody = { "type":"token", "channel":"voice"}
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.add_voice_token(requestBody, applicationId)

    def testAddVoiceMessagingURL(self):
        requestBody = { "name":"new app", "voiceUrl":"http://website1.com", "messagingUrl":"http://website2.com", "platform":"scripting", "partition":"staging"}
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.add_voice_messaging_url(requestBody, applicationId)

    def testUpdateApplication(self):
        requestBody = { "name":"new app updated22", "platform":"webapi", "partition":"production" }
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.update_application(requestBody, applicationId)

    def testDeleteApplication(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.delete_application("422446")
        
    def testDeleteAddress(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.delete_address("422451", "number", "+14077969905")
        
    def testGetAllApplications(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.get_all_applications()
        
    def testGetApplication(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.get_application('422451')

    def testGetApplicationAddresses(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.get_application_addresses('422451')

    def testGetAllAddressesForAccount(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.get_all_addresses_for_account()

    def testGetAllAvailableExchangesForAccount(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.get_all_available_exchanges_for_account()

    def testGetAllAvailablePrefixesForAccount(self):
        prefix = "9723"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.get_all_available_prefixes_for_account(prefix)
"""
"""
Sample usage

tropoClientConnect = TropoTest()
tropoClientConnect.testCreateApplication() 
tropoClientConnect.testGetAllApplications()
tropoClientConnect.testGetApplication()
tropoClientConnect.testAddNumberFromPool()
tropoClientConnect.testAddMultipleNumbersFromPool()
tropoClientConnect.testAddSpecificNumber()
tropoClientConnect.testAddTollFreeNumber()
tropoClientConnect.testAddInternationalNumber()
tropoClientConnect.testAddIMAccount()
tropoClientConnect.testAddVoiceToken()
tropoClientConnect.testAddVoiceMessagingURL()
tropoClientConnect.testUpdateApplication()
tropoClientConnect.testDeleteApplication()
tropoClientConnect.testDeleteAddress()
tropoClientConnect.testGetApplicationAddresses()
tropoClientConnect.testGetAllAddressesForAccount()
tropoClientConnect.testGetAllAvailableExchangesForAccount()
tropoClientConnect.testGetAllAvailablePrefixesForAccount()

"""


