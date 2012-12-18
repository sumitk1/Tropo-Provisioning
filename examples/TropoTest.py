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
        print "Response = %s"% testResp
        result = testResp.find("failed")
        self.assertNotEqual(result, -1)

    def test_AddInternationalNumber_successful(self):
        applicationId = "430603"
        prefix = 31
        tropoTest = TropoProvisioning()
        response = tropoTest.add_international_number_from_pool(applicationId, prefix, data_format.JSON)    
        print "Response = %s"% response
        result = response.find("+31")
        self.assertNotEqual(result, -1)
        
    def test_AddNumberFromPool(self):
        applicationId = "430603"
        prefix = 1407
        tropoTest = TropoProvisioning()
        response = tropoTest.add_single_number_from_pool(applicationId, prefix, data_format.JSON)
        print "Response = %s"% response
        result = response.find("+1407")
        self.assertNotEqual(result, -1)
        
    def testAddMultipleNumbersFromPool(self):
        applicationId = "430603"
        prefix = 1407
        count = 2
        tropoTest = TropoProvisioning()
        response = tropoTest.add_multiple_numbers_from_pool(applicationId, prefix, count, data_format.JSON)
        print response 
        result = response[0].find("+1407")
        self.assertNotEqual(result, -1)
        
    def test_AddSpecificNumberFromPool(self):
        applicationId = "430603"
        number = "4077969837"
        tropoTest = TropoProvisioning()
        response = tropoTest.add_specific_number_from_pool(applicationId, number, data_format.JSON)
        print response 
        result = response.find("+14077969837")
        self.assertEqual(response, "+14077969837")
     
    def test_AddTollFreeNumber(self):
        applicationId = "430603"
        prefix = "1866"
        tropoTest = TropoProvisioning()
        response = tropoTest.add_tollFree_number(applicationId, prefix, data_format.JSON)    
        print "Response = %s"% response
        result = response.find("+1866")
        self.assertNotEqual(result, -1)    
   
    def test_AddVoiceMessagingURL(self):
        applicationId = "430603"
        voiceUrl = "http://website1.com"
        messagingUrl = "http://website1.com"
        tropoTest = TropoProvisioning()
        response = tropoTest.add_voice_messaging_url(applicationId, voiceUrl, messagingUrl, data_format.JSON)
        print "Response = %s"% response
        self.assertEqual(response, "430603")
        
    def test_DeleteAddress_successful(self):
        applicationId = "430603"
        addressType = "number"
        addressValue = "+14076800746"
        tropoTest = TropoProvisioning()
        response = tropoTest.delete_address(applicationId, addressType, addressValue, data_format.JSON)    
        print response
        result = {"message": "delete successful"}
        self.assertEqual(response, result)
        
    def test_DeleteAddress_failed(self):
        applicationId = "430603"
        addressType = "number"
        addressValue = "+14074873572"
        tropoTest = TropoProvisioning()
        response = tropoTest.delete_address(applicationId, addressType, addressValue, data_format.JSON)    
        print response
        result = response.find("failed")
        self.assertNotEqual(result, -1)
        
"""    

    def testUpdateApplication(self):
        requestBody = { "name":"new app updated22", "platform":"webapi", "partition":"production" }
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.update_application(requestBody, applicationId)

    def testDeleteApplication(self):
        tropoTest = TropoProvisioning(TropoTest.USER_NAME, TropoTest.PASSWORD)
        tropoTest.delete_application("422446")
        
        
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

