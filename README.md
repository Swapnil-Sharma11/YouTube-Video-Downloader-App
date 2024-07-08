# YouTube-Video-Downloader-App

The provided Python script uses Streamlit to create a user interface for downloading YouTube videos or audio files.
It imports the YouTube class from pytube for fetching video metadata and streams, along with requests for downloading video streams in chunks.
The main function, downloadfn, verifies user confirmation before proceeding with the download.
For videos, it fetches the highest resolution stream, calculates file size, displays progress with a Streamlit progress bar, and saves the file locally.
Audio downloads directly using download.
The interface includes input fields for URL and download path, a dropdown for choosing video or audio, and a checkbox for confirmation.
It provides warnings for invalid inputs or unconfirmed downloads and success/error messages upon completion or failure, enhancing user interaction and feedback throughout the download process.
