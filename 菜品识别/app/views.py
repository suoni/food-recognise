from django.shortcuts import render

import sys
import ssl
# Create your views here.

def index(req):
    from urllib import request
    from urllib import parse
    import base64
    import json

    img_name=''
    similarity = ''
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=27T6DUb1owj5e3UAQQqAjp6T&client_secret=tvasEC3x7DGp9liyVobBDKWmwKrx8kER '
    request01 = request.Request(url)
    request01.add_header('Content-Type', 'application/json; charset=UTF-8')
    content = request.urlopen(request01).read()
    if (content):
        data = content.decode('utf-8')

        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish?access_token="+ json.loads(data)['access_token']
        f= open('static/img/pidan.jpg','rb')
        img=base64.b64encode(f.read())
        params= {'image': img, 'top_num': 5}
        params = parse.urlencode(params).encode()

        img_req = request.Request(url=request_url, data=params)
        img_req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req_data = request.urlopen(img_req).read()
        if req_data:
            result = json.loads(req_data.decode())['result'][0]
            img_name = result['name']
            similarity = round(float(result['probability']) * 100,2)
            print(round(float(result['probability']) * 100,2))





    return render(req,'index.html',{'name': img_name, 'similarity': similarity})