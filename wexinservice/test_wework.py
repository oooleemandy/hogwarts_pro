import json
import requests

# 从“我的企业”，最下面企业ID获取的
corpid = 'ww8565ff9c58bd74ad'
# 从客户联系 客户里获取
corpsecret = 'LGp1Zfet7VQ_oGiwMoHhWgeBrjYwF91HeKnch1CB0L0'


# 企业标签库接口测试
def test_tag_get():
    # 获取access_token
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    print(json.dumps(r.json(), indent=2))
    # 取出token
    token = r.json()['access_token']

    # 获取企业标签库
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        # 参数
        params={'access_token': token},
        # 请求体
        json={
            'tag_id': []
        }
    )
    # 格式化的一个东西，间距为2
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    # 添加企业客户标签
    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                      params={'access_token': token},
                      # 请求体
                      json={
                          'group_name': 'group_demo_leemandy',
                          'tag': [
                              {
                                  'name': 'tag_demo_leemandy'
                              }
                          ]
                      }

                      )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
