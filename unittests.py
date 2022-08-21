import unittest
from unittest import TestCase
from shopify_tools import ShopifyTools
from rename import rename_images
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
if __name__ == '__main__':
    unittest.main()