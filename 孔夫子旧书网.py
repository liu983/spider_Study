# -*- encoding:utf-8 -*-
import requests
from urllib.parse import unquote_plus
from Crypto.PublicKey import RSA

headers = {
"Cookie":"randomcodekey=srck31161856325090jri568; randomcode=084936269723; randomcodesign=Y1RNhG%2B5mC263cYz4lUOpQBlQL80FuJ2I1FKptqtaKtIcG5rr45EiX4BZvIgrgwEPvyE6uoivxIg1S6Lus5mAw%3D%3D; kfz_uuid=ef4b54d9-5003-4d7a-ba05-b1db856b7a4b; reciever_area=1006000000; shoppingCartSessionId=f006bc822ed14f64a2ceae4505896856; kfz-tid=76b77323bd2a6484561c2cb1bfc9f67a; utm_source=101002007000; PHPSESSID=2ua6jvg4p06vtt1m605fob2rb0; acw_tc=276077c216908508636491345ebfb1313737c2272f275f750c3badbeedcb37; kfz_trace=ef4b54d9-5003-4d7a-ba05-b1db856b7a4b|0|e897ab25367aa672|101002007000; TY_SESSION_ID=3ee12a8d-de24-4d98-b438-8449c939d316",
"Host":"search.kongfz.com",
"Referer":"https://search.kongfz.com/product_result/?key=9787115429674&status=0&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
"X-Tingyun-Id": "OHEPtRD8z8s;r=850989133"
}
params = {
    "key": "9787115429674",
    "status": "0",
    "_stpmt": "eyJzZWFyY2hfdHlwZSI6Imhpc3RvcnkifQ==",
    "pagenum": "2",
    "ajaxdata": "1",
    "type": "1",
    "_": "1690858399669"
}
publicKey = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMiU6MWuUemPQkPAZSfYUBD6qfgQfM/jY3OEBbdNlOm0SBjX4Z1GMSg0Jhk70NQlxNfrbz4oN0A+jVhoH7gEyY8CAwEAAQ=="

url = 'https://search.kongfz.com/product_result/?key=9787115429674&status=0&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9&pagenum=2&ajaxdata=1&type=1&_=1690850973637'
resp = requests.get(url, headers=headers, params=params)
print(resp.status_code)

print(resp.text)