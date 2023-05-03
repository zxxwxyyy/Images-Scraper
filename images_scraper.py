import os
import requests
import argparse
from bs4 import BeautifulSoup


def get_image_urls(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')

    image_urls = [img_tag['src'] for img_tag in image_tags if 'src' in img_tag.attrs and img_tag['src'].startswith('http') and img_tag['src'].endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return image_urls


def download_images(image_urls, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for i, image_url in enumerate(image_urls):
        response = requests.get(image_url)

        if response.status_code != 200:
            print(f"Error downloading image {i + 1}: {response.status_code}")
            continue

        with open(f'{save_folder}/image_{i + 1}.jpg', 'wb') as f:
            f.write(response.content)


def main(url, save_folder):
    image_urls = get_image_urls(url)

    if not image_urls:
        print("No image URLs found.")
        return

    print(f"Found {len(image_urls)} image URLs.")
    download_images(image_urls, save_folder)


def c_main():
    parser = argparse.ArgumentParser(description="Download images from the URL.")
    parser.add_argument("url", help="The URL of the images to scrape")
    parser.add_argument("save_folder", help="The folder name to save the images")
    args = parser.parse_args()

    main(args.url, args.save_folder)


if __name__ == '__main__':
    c_main()
