import unittest
from unittest import TestCase
from shopify_tools import ShopifyTools
from rename import rename_images
import shopify_template
import create_dicts
class TestSnowflakes(TestCase):

    def test_get_snowflake_type(self):
        st = ShopifyTools()
        assert st.is_two_inch('ADW-CMC-FWJ-JWW.stl') == False
        assert st.is_two_inch('ADW-CMC-FWJ-JWW_2x.stl') == True
        assert st.is_two_inch('AAS-SGC-TMW-NIO_2x.stl') == True
        
    def test_rendered_filename(self):
        st = ShopifyTools()
        assert st.get_rendering_filename('AAS-SGC-TMW-NIO.stl') == 'AAS-SGC-TMW-NIO.SilverTextured.jpg'
        print(st.get_rendering_filename('AAS-SGC-TMW-NIO_2x.stl'))
        assert st.get_rendering_filename('AAS-SGC-TMW-NIO_2x.stl') == 'AAS-SGC-TMW-NIO.ShapewaysWhite.jpg'

    def test_rename_images(self):
        assert rename_images('AAS-SGC-TMW-NIO.stl_Shapeways White_.jpg') == None
        assert rename_images('AAS-SGC-TMW-NIO.stl_Silver Textured_.jpg') == 'AAS-SGC-TMW-NIO.SilverTextured.jpg'
        assert rename_images('AAS-SGC-TMW-NIO_Shapeways White.jpg') == 'AAS-SGC-TMW-NIO.ShapewaysWhite.jpg'
        assert rename_images('AAS-SGC-TMW-NIO_Silver Textured.jpg') ==  'AAS-SGC-TMW-NIO.SilverTextured.jpg'
        assert rename_images('YYK-WFA-QAG-VRO_Shapeways White.jpg') == 'YYK-WFA-QAG-VRO.ShapewaysWhite.jpg'
        assert rename_images('YYK-WFA-QAG-VRO_Silver Textured.jpg') == 'YYK-WFA-QAG-VRO.SilverTextured.jpg'

    def test_templates(self):
        st = ShopifyTools()
        one_inch_row : dict= st.create_one_inch_row('AAA-BBB-CCC-DDD', 'http://foo.com')
        canonical_one_inch_row = create_dicts.create_one_inch_row('AAA-BBB-CCC-DDD', 'http://foo.com')
        len_one_inch = len(set(one_inch_row.keys()))
        len_canonical_one_inch = len(set(canonical_one_inch_row.keys()))
        print(set(one_inch_row.keys()) - set(canonical_one_inch_row.keys()))
        print(f" {len_one_inch}, {len_canonical_one_inch}")
        assert (len(set(one_inch_row.keys()))) == len(set(canonical_one_inch_row.keys()))
if __name__ == '__main__':
    unittest.main()