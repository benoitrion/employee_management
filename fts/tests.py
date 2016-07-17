from django.test import LiveServerTestCase
from selenium import webdriver

class EmpMgmtTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_emp_via_admin_site(self):
        # Access admin page
        self.browser.get(self.live_server_url + '/admin/login/?next=/admin/')

        # Assert we are on admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # TODO : Create an employee
        self.fail('finish this test')
