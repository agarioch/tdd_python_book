from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user goes to check out homepage of a new online to-do app
        self.browser.get('http://localhost:8000')

        # she notices that it mentions to-do lists in the header and title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types 'buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        #  when she hits enter, the page updates and now lists
        #  '1: Buy peacock feathers' as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # there is still a text box inviting her to add another item
        # she enters 'use peacock feathers to make a fly' (fly fishing hobby)
        self.fail('Finish the tests!')

        # the page updates again, and now shows both items on the list

        # she wonders whether the site will remember her list.
        # then she sees that the site has generated a unique URL for her
        # there is some explanatory text to that effect.

        # she visits that URL - her to-do list is still there.

        # satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')