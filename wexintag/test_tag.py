import json
import requests
import pytest

# 企业标签库接口测试
from wexintag.tag import Tag


class TestTag():

    def setup_class(self):
        # 初始化Tag
        self.tag = Tag()
        # 拿到token
        self.tag.get_token()

    # 测试查看标签列表
    def test_tag_list(self):
        # 获取新列表 进行校验
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    # 参数化
    @pytest.mark.parametrize("group_name,tag_names", [
        ["group_demo_leemandy2", [{'name': 'tag_demo_leemandy2'}]],
        ["group_demo_leemandy2", [{'name': 'tag_demo_leemandy2'}]],
        ["group_demo_leemandy2", [{'name': 'tag_demo_leemandy2'}, {'name': 'tag_demo_leemandy3'}]],

    ])
    def test_tag_add(self, group_name, tag_names):
        # 增加标签组
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        r = self.tag.list()
        # python列表表达式
        # 校验 找taggroup下面有没有新建的groupname
        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        # 校验 找taggroup下tag下的name是不是我刚刚新建的
        tags = [{'name': tag['name']} for tag in group['tag']]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tag_names

    # 测试删除标签
    @pytest.mark.parametrize("tag_name", [
        "tag1", "tag2", "tag3"
    ])
    def test_tag_delete(self, tag_name):
        r = self.tag.delete_by_tagname(tag_name)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
