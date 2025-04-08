# Screenshot-Scraper-Experimental

🔍 Download random screenshots from prnt.sc in bulk with this Python script!

## ✨ Description

This project is a Python script that automates the process of downloading random screenshots from the popular screenshot hosting website, prnt.sc. It uses concurrent downloads to speed up the scraping process and saves the images locally.

## 🚀 Features

- **Concurrent Downloads:** Utilizes 4 worker threads for efficient image fetching.
- **Random Screenshot Selection:** Automatically selects random screenshots from prnt.sc.
- **Automatic Directory Creation:** Creates a "screenshots" directory if it doesn't exist.
- **Rate Limit Bypass:** Uses `cloudscraper` to bypass prnt.sc's rate limits.

## 🛠️ Installation

To get started, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/gag3301v/Screenshot-Scraper-Experimental.git
   cd Screenshot-Scraper-Experimental
   ```

2. Install the required dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```

## 📦 Usage

Here's how you can use the script:

```python
# Import necessary modules
from screenshot_downloader import ScreenshotDownloader

# Initialize the downloader
downloader = ScreenshotDownloader()

# Download 1000 random screenshots
downloader.download_images(1000)
```

## 🔧 Configuration

No environment variables are required for this script.

## 🧪 Tests

This project does not include tests at the moment. Feel free to contribute by adding some!

## 📁 Project Structure

```plaintext
Screenshot-Scraper-Experimental/
├── main.py
├── screenshot_downloader.py
├── requirements.txt
└── README.md
```

## 👩‍💻 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](https://github.com/gag3301v/Screenshot-Scraper-Experimental/blob/main/CONTRIBUTING.md) file for guidelines on how to contribute.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/gag3301v/Screenshot-Scraper-Experimental/blob/main/LICENSE) file for details.