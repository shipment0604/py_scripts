#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: bboysoul
import requests
import json
import sys
import os
 
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=742ac61aed39205ed458bbeafc5917f4dad2f1b9242413e7f082f5af23c95932"
 
def msg(text):
    json_text= {
     "msgtype": "text",
        "at": {
            "atMobiles": [
                "17683884782"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
