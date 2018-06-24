from selenium import webdriver
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
        self.fail('Finish the test!')

        # she is invited to enter a to-do item immediately

        # she types 'buy peacock feathers' into a text box

        #  when she hits enter, the page updates and now lists
        #  '1: Buy peacock feathers' as an item in a to-do list

        # there is still a text box inviting her to add another item
        # she enters 'use peacock feathers to make a fly' (fly fishing hobby)

        # the page updates again, and now shows both items on the list

        # she wonders whether the site will remember her list.
        # then she sees that the site has generated a unique URL for her
        # there is some explanatory text to that effect.

        # she visits that URL - her to-do list is still there.

        # satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')