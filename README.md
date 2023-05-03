# Images-Scraper

 Helpful tool to scrap images from online with python. 

 `Python version = 3.9.7`

## Installation

1. Clone the repository or download the script files:

```sh
git clone https://github.com/zxxwxyyy/Images-Scraper.git
```

2. Change to the project directory:

```sh
cd Images-Scraper/
```

3. Install the required libraries using pip:

```sh
pip install -r requirements.txt
```

## Usage

To use the script, run the following command with the URL and folder name:

```sh
python images_scraper.py "https://REPLACE.WITH.YOUR.URL" "YOUR_FOLDER_NAME"
```

Replace the `https://REPLACE.WITH.YOUR.URL` and `YOUR_FOLDER_NAME` with your desired values.

To run in it Google Colab or Jupyter Notebook: 

```sh 
from images_scraper import main

url = 'https://REPLACE.WITH.YOUR.URL'
save_folder = 'YOUR_FOLDER_NAME'

main(url, save_folder)
```