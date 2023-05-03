import os
import shutil
import unittest
from images_scraper import get_image_urls, download_images


class TestImageDownloader(unittest.TestCase):

    def setUp(self):
        self.test_url = 'https://www.freeimages.com/'
        self.test_save_folder = 'test_images'

    def tearDown(self):
        if os.path.exists(self.test_save_folder):
            shutil.rmtree(self.test_save_folder)

    def test_get_image_urls(self):
        image_urls = get_image_urls(self.test_url)
        self.assertIsNotNone(image_urls)
        self.assertTrue(len(image_urls) > 0)
        self.assertTrue(all(url.startswith('http') and (
                    url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png') or url.endswith('.gif')) for
                            url in image_urls))

    def test_download_images(self):
        image_urls = get_image_urls(self.test_url)
        download_images(image_urls, self.test_save_folder)
        self.assertTrue(os.path.exists(self.test_save_folder))
        self.assertEqual(len(os.listdir(self.test_save_folder)), len(image_urls))


if __name__ == '__main__':
    unittest.main()
