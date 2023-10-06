from unittest.mock import patch
from django.test import TestCase

from monitor.views import fetch_current_price


class FetchPriceTestCase(TestCase):

    @patch('monitor.views.requests.get')
    def test_fetch_current_price(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <body>
                <span class="a-price-whole">421</span>
            </body>
        </html>
        """

        url = ("https://www.amazon.in/SR-Robotics-Tesla-Project-Battery/dp/B07JK6Q191/ref=sr_1_5?crid=1OWQULDV9J57G"
               "&keywords=tesla+coil&qid=1696570765&sprefix=tesla%2Caps%2C214&sr=8-5")
        selector = "span.a-price-whole"

        result = fetch_current_price(url, selector)
        self.assertEqual(result, 421.0)
