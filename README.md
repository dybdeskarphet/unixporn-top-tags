# 📊 r/unixporn Top Tags

This script is designed to analyze and aggregate the tags used in post titles on the [/r/unixporn](https://www.reddit.com/r/unixporn/) subreddit. It fetches posts from Reddit, extracts tags from post titles, normalizes them, and then counts their occurrences, outputting the result in a CSV file.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- PRAW (Python Reddit API Wrapper)
- Pandas
- NumPy
- Matplotlib

### Installation

1. Clone the repository or download the source code.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Reddit API credentials (see the "Configuration" section below).

### Configuration

You need to create a Reddit API application to get your `client_id` and `client_secret`. Follow these steps:

1. Go to [Reddit's apps page](https://www.reddit.com/prefs/apps).
2. Click "Create App" or "Create Another App".
3. Fill in the details:
   - Name: Whatever you prefer
   - App type: Choose "script"
   - Description: Optional
   - About URL: Optional
   - Redirect URI: http://localhost:8080 (or another URI of your choice)
4. Click "Create app".
5. Note down the `client_id` (under the app name) and `client_secret`.

Create a file named `.env` in the same directory as the script with the following contents:

```plaintext
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
```

## 📝 Usage

### Create the data

Run the script using Python:

```bash
python tag_counter.py
```

The script will fetch data from the subreddit, process it, and output the results in a file named `tag_counts.csv`.

### Create graph from the data

Run the script using Python:

```bash
python tag_counter.py
```

This script will create a horizontal bar graph from the resulting data.

## 📚 Features

- Fetches top posts from /r/unixporn for each year since the subreddit's creation.
- Extracts and normalizes tags from post titles.
- Counts the occurrence of each tag.
- Outputs the result in a CSV file for easy analysis.
- Create a graph from the resulting CSV file.

## ⚙️ Customization

You can customize the script to analyze different subreddits or to change the normalization rules by editing the `normalize_tag` function.

## 📋 License

This project is open source and available under the [GNU GPLv3](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/dybdeskarphet/unixporn-top-tags/issues).

## 🌟 Acknowledgements

Special thanks to the Reddit community and the developers of PRAW for making this project possible.
