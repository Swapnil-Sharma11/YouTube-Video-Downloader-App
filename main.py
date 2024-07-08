from pytube import YouTube
import streamlit as st
import requests

def helper_size(stream):
    if stream:
        return round(stream.filesize / (1024 * 1024), 2)
    else:
        return None

def downloadfn(url, download_folder, type, confirmed):
    try:
        if confirmed:
            if type == "Video":
                yt = YouTube(url)
                streams = yt.streams.filter(progressive=True, file_extension="mp4")
                hires = streams.get_highest_resolution()
                file_size = helper_size(hires)
                st.text(f"Video Size: {file_size} MB")
                st.text("Video Downloading...")
                progress_bar = st.progress(0)

                with open(download_folder + "/video.mp4", 'wb') as f:
                    total_length = hires.filesize
                    bytes_written = 0
                    for chunk in requests.get(hires.url, stream=True).iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            bytes_written += len(chunk)
                            progress_bar.progress(min(bytes_written / total_length, 1.0))

                st.success("Video Downloaded Successfully!")
                st.text("Ready to watch? Your download is complete.")

            elif type == "Audio":
                yt = YouTube(url)
                hires_audio = yt.streams.filter(only_audio=True).first()
                file_size = helper_size(hires_audio)
                st.text(f"Audio Size: {file_size} MB")
                st.text("Audio Downloading...")
                hires_audio.download(output_path=download_folder)
                st.success("Audio Downloaded Successfully!")
                st.text("Ready to listen? Your audio file is downloaded.")

        else:
            st.warning("Please confirm the download before proceeding.")

    except Exception as e:
        if type == "Audio":
            st.error(f"Audio cannot be downloaded: {e}")
        else:
            st.error(f"Video cannot be downloaded: {e}")

custom_css = """
    <style>
        body, .stApp {
            font-family: Verdana, Geneva, sans-serif;
        }
    </style>
"""

def main():
    st.title("YouTube Video Downloader")
    st.markdown(custom_css, unsafe_allow_html=True)
    url = st.text_input("Paste the URL")
    download_folder = st.text_input("Enter the download path")
    types = ["Video", "Audio"]
    type = st.selectbox("Select Your Choice", types)
    confirmed = st.checkbox("Yep, I'm ready to download.")

    if st.button("Download"):
        if url and download_folder and confirmed:
            downloadfn(url, download_folder, type, confirmed)
        elif not confirmed:
            st.warning("Please confirm the download before proceeding.")
        else:
            st.warning("Please enter a valid URL and download path.")

if __name__ == "__main__":
    main()
