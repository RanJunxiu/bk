# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context,render_json
import requests


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def demo(request):
    """
    demo
    """
    return render_mako_context(request, '/home_application/demo.html')

def orm(request):
    """
    demo
    """
    return render_mako_context(request, '/home_application/orm.html')

"""
def data(request):
#    request.post
    a = request.POST.dict()
    print(a)
    return render_json({
    "code":0,
    "result": True,
    "messge":"success",
    "data": {
        "series":[{
            "color": "#f9ce1d",
            "name":"项目一",
            "data": [10, 180, 190, 150, 125, 76, 135, 162, 32, 20, 6, 3]
        }],
        "categories": ["07:10", "07:10", "07:10", "07:10", "07:10", "07:10", "07:10", "07:10", "07:10", "07:10", "07:10", "07:10"]
    }
})
"""

"""
from conf.default import APP_ID, APP_TOKEN
def orm(request):
    data = {
        'bk_app_code': APP_ID,
        'bk_app_secert': APP_TOKEN,
        'bk_token': request.COOKIES.get('bk_token'),
        'bk_biz_id': request.GET.get('id')
    }

    res = requests.post(url = "http://paas.bkds.com/api/c/compapi/v2/job/fast_execute_script/",
                   json = data
                   )
    return render_json(res.content)
"""

from conf.default import APP_ID, APP_TOKEN
import json
def orm(request):
    url = "http://paas.bkds.com/api/c/compapi/v2/cc/search_business/"
    data = {
        'bk_app_code': APP_ID,
        'app_secret': APP_TOKEN,
        'bk_username': "admin"
    }
    res = requests.post(url, data)
    print APP_ID
    print APP_TOKEN
    result = json.loads(res.content)
    print result
    return render_json(res.content)