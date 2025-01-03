import os
import subprocess

video_folder = './'
output_folder = './'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all video files in the video folder
for filename in os.listdir(video_folder):
    if filename.endswith('.mp4'):
        video_path = os.path.join(video_folder, filename)
        thumbnail_name = os.path.splitext(filename)[0] + '-thumbnail.jpg'
        thumbnail_path = os.path.join(output_folder, thumbnail_name)

        # Run FFmpeg command to generate the thumbnail
        subprocess.run(['ffmpeg', '-i', video_path, '-ss', '00:00:01.000', '-vframes', '1', thumbnail_path])
        print(f"Generated thumbnail for {filename}: {thumbnail_name}")
