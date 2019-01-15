
url = "http://localhost/api/v3/requests/"
techkey = "9481D00C-B591-4A2F-8103-D819969922F7"

import requests
import json
import sys

# Construct JSON input data
inputdata = '''{
    "request": {
		"is_fcr": "true",
        "resolution":{
        	"content": "User was provided with a temporary password which they changed at first logon."},
		"status":{
        	"name": "closed"},
		"closure_info":{
            "requester_ack_resolution": true,
            "requester_ack_comments": "User has successfully logged in.",
            "closure_comments": "Provided the user with a temporary password.",
            "closure_code":{
                "name": "success"}
        }
        }
}'''

param = {
	"TECHNICIAN_KEY":techkey,
	"input_data":inputdata,
	"format":"json"
}


try:
	woid = sys.argv[1]
    # Modify RESTAPI operation
	r = requests.request("PUT", url + str(woid), params = param )
	if r.json()["response_status"]["status"] == "success":
        # Successful status message
		print ("Ticket has automatically been updated.")

	else:
		print (r.json()["response_status"]["messages"])

except Exception as e:
	print ("Update failed with Error: {}".format(str(e)))

	