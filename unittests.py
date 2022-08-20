import unittest
from unittest import TestCase
from shopify_tools import ShopifyTools
class TestSnowflakes(TestCase):
    def test_get_snowflake_type(self):
        st = ShopifyTools()
        assert st.is_one_inch('ADW-CMC-FWJ-JWW.stl') == True
        assert st.is_one_inch('ADW-CMC-FWJ-JWW_2x.stl') == False


if __name__ == '__main__':
    unittest.main()