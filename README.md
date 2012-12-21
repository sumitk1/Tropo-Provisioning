Tropo-Provisioning
==================

Tropo Provisioning API Python Library

	Build on Python version - 2.7.3
	set PYTHONPATH to have Tropo/lib/tropoProvisioning 
	
lib/tropoProvisioning/config.cfg - is used to specify some default values for the project. These values are like:

	[tropo_api_config]
	url = https://api.tropo.com/v1/
	username=xxxxx
	password=yyyyy
	requestType = JSON
	platform = scripting
	partition = staging

The TropoProvisioning object if created without any parameters takes its values from this config.cfg file

	tropoTest = TropoProvisioning()

If the TropoProvisioning object is created with parameters then the values from the config file is overridden

	tropoTest = TropoProvisioning(url="www", userName="xxxxx", password="yyyyy", requestType="type")

data_format.py - This file describes the various methods supported by our Tropo Python API


	 