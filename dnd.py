import json
from wsgiref import headers
import requests

def redirect_to_gateway(data_response):

    url = "http://192.168.88.10/send_sms"

    param_list = []
    user_id = 0

    for param_recipient in data_response:

        user_id=user_id + 1

        param = {
            "number":param_recipient,
            "text_param":[
                "bj"
            ],
            "user_id":user_id
        }
        param_list.append(param)

        payload = json.dumps({
            "text":"Testing the DND locally",
            "port":[
                0,
                0
            ],
            "param":param_list

        })

        headers={
            "Content-Type":"applicatio/json",

        }

        response = requests.request("POST", url, headers=headers,data=payload, auth=requests.auth.HTTPDigestAuth("admin", "admin"))

        print("this is redirected to gateway response\n", response.text)

redirect_to_gateway(["+2348031346306"])