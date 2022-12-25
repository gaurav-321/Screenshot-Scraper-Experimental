# Screenshot Downloader
This program is a simple script that downloads random screenshots from the internet using the prnt.sc website. It does this by generating random links, scraping the page for the screenshot image, and then saving the image to the screenshots directory.

## Requirements
To run this script, you will need to have the following packages installed:

- beautifulsoup4
- cloudscraper
- requests
You can install these packages using pip by running the following command:

Copy code
pip install beautifulsoup4 cloudscraper requests
## Usage
To use this script, simply run the following command:
```
python screenshot_downloader.py
```
The script will run and download 1000 random screenshots, saving them to the screenshots directory. If the directory does not exist, it will be created automatically.

## Notes
Please note that the prnt.sc website has rate limits and may block your IP if you make too many requests in a short period of time. To avoid this, the script uses the cloudscraper package to bypass these rate limits. However, there is still a chance that your IP could be blocked if you run the script for too long.

Additionally, please be aware that some of the images downloaded from the internet may contain inappropriate content. Use caution when downloading and viewing these images.
