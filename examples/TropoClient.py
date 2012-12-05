'''
@author: sumitk

DONT USE THIS SCRIPT TO RUN THE TESTS.
USE THE INDIVIDUAL SCRIPTS. THIS WILL BE USED FOR UNIT TESTS.

'''
from TropoProvisioning import TropoProvisioning
import TropoLogger

class TropoClient(object):
    '''
    classdocs
    '''
    # Use your credentials 
    URL = 'https://api.tropo.com/v1/applications'
    USER_NAME = 'sumitk85'
    PASSWORD = 'qazwsx123'  
    POST_VAL = {"name":"sumitk5", 
          "voiceUrl":"http://website.com", 
          "messagingUrl":"http://website2.com",
          "platform":"scripting", 
          "partition":"staging"}
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def testCreateApplication(self):
        requestBody = { "name":"sumitk6", "voiceUrl":"http://website.com", "messagingUrl":"http://website2.com", "platform":"scripting", "partition":"staging" }
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.create_application(requestBody)
        
    def testAddNumberFromPool(self):
        requestBody = {"type":"number", "prefix":"1407"}
        applicationId = "422451"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_single_number_from_pool(requestBody, applicationId)

    def testAddMultipleNumbersFromPool(self):
        requestBody = {"type":"number", "prefix":"1407"}
        applicationId = "422451"
        count = 5
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_multiple_numbers_from_pool(requestBody, applicationId, count)

    def testAddSpecificNumber(self):
        requestBody = {"type":"number", "number":"4077969880"}
        applicationId = "422446"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_specific_number_from_pool(requestBody, applicationId)

    def testAddTollFreeNumber(self):
        requestBody = {"type":"number", "prefix":"1866"} # Need to have production account to test
        applicationId = "422446"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_tollFree_number(requestBody, applicationId)

    def testAddInternationalNumber(self):
        requestBody = {"type":"number", "prefix":"31"}
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_international_number_from_pool(requestBody, applicationId)

    def testAddIMAccount(self):
        '''Not working. Getting 400 from Tropo. 
           Need to enter a valid IM username and password.
           IM application (gtalk, aim, yahoo etc) needs to give access to Tropo.
        '''
        requestBody = {"type":"gtalk", "username":"sumitk85", "password":""}
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_IM_account(requestBody, applicationId)

    def testAddVoiceToken(self):
        requestBody = { "type":"token", "channel":"voice"}
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_voice_token(requestBody, applicationId)

    def testAddVoiceMessagingURL(self):
        requestBody = { "name":"new app", "voiceUrl":"http://website1.com", "messagingUrl":"http://website2.com", "platform":"scripting", "partition":"staging"}
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.add_voice_messaging_url(requestBody, applicationId)

    def testUpdateApplication(self):
        requestBody = { "name":"new app updated22", "platform":"webapi", "partition":"production" }
        applicationId = "422445"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.update_application(requestBody, applicationId)

    def testDeleteApplication(self):
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.delete_application("422446")
        
    def testDeleteAddress(self):
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.delete_address("422451", "number", "+14077969905")
        
    def testGetAllApplications(self):
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.get_all_applications()
        
    def testGetApplication(self):
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.get_application('422451')

    def testGetApplicationAddresses(self):
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.get_application_addresses('422451')

    def testGetAllAddressesForAccount(self):
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.get_all_addresses_for_account()

    def testGetAllAvailableExchangesForAccount(self):
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.get_all_available_exchanges_for_account()

    def testGetAllAvailablePrefixesForAccount(self):
        prefix = "9723"
        tropoTest = TropoProvisioning(TropoClient.USER_NAME, TropoClient.PASSWORD)
        tropoTest.get_all_available_prefixes_for_account(prefix)

"""
Sample usage

tropoClientConnect = TropoClient()
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


