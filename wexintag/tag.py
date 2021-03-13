'''
封装基本业务操作。业务层
'''

# 从“我的企业”，最下面企业ID获取的
import json

import requests

corpid = 'ww8565ff9c58bd74ad'
# 从客户联系 客户里获取
corpsecret = 'LGp1Zfet7VQ_oGiwMoHhWgeBrjYwF91HeKnch1CB0L0'


class Tag:
    # 获取token
    def __init__(self):
        self.token = ""

    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        print(json.dumps(r.json(), indent=2))
        # 取出token 放到实例里 后面都可以用
        self.token = r.json()['access_token']

    # 发起标签组一个list
    def list(self):
        # 获取企业标签库
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            # 参数
            params={'access_token': self.token},
            # 请求体
            json={
                'tag_id': []
            }
        )
        # 格式化的一个东西，间距为2
        print(json.dumps(r.json(), indent=2))
        # 返回一个内容
        return r

    # 添加一个标签，需要标签组名字和tag这两个参数
    def add(self, group_name, tags):
        # 添加企业客户标签
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            # 请求体
            json={
                'group_name': group_name,
                'tag': tags
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete_by_tagname(self, tagname):
        tag_list, tag_id = self.get_tag(tagname)
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.get_token()},
            json={
                "tag_id": [tag_id]
                # "group_id": []
            }
        )
        return r
