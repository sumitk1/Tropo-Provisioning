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
        result = "delete successful"
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


    def test_DeleteApplication_successful(self):
        applicationId = "430678"
        tropoTest = TropoProvisioning()
        response = tropoTest.delete_application(applicationId, data_format.JSON)
        print response
        result = "delete successful"
        self.assertEqual(response, result)

    def test_DeleteApplication_failed(self):
        applicationId = "43067112"
        tropoTest = TropoProvisioning()
        response = tropoTest.delete_application(applicationId, data_format.JSON)
        print response
        result = response.find("failed")
        self.assertNotEqual(result, -1)
   
    def test_UpdateApplication(self):
        applicationId = "430603"
        name = "new app updated11"
        platform = "webapi"
        partition = "staging"
    
        tropoTest = TropoProvisioning()
        response = tropoTest.update_application(applicationId, name, platform, partition, data_format.JSON)     
        print response
        self.assertEqual(response, "430603")

