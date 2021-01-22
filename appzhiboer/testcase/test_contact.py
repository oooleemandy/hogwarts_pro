from appzhiboer.page.app import App


class TestWX:
    def setup(self):
        #实例化APP
        self.app = App()
        #拿到main的实例
        self.main = self.app.start().goto_main()
        pass
    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = "EE"
        gender = "男"
        phonenum = "13055555555"

        result = self.main.goto_contactlist().addmember().add_member_manul().edit_contact(name, gender, phonenum).verify_toast()
        assert '添加成功' == result


    def test_delcontact(self):
        name="EE"

        result = self.main.goto_contactlist().search_button().searchmember(name).clickmore().clickeditmem().afternum(name)
        assert result == 1