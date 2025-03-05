import subprocess
import os

def create_video_with_ffmpeg(image_file, audio_file, subtitle_file, output_file='outputs/output_video.mp4'):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    command = [
 "ffmpeg", "-loop", "1", "-f", "image2", "-i", image_file,
    "-f", "mp3", "-i", audio_file,
    "-vf", f"subtitles={subtitle_file},scale=1080:1920:flags=lanczos",
    "-c:v", "libx264", "-b:v", "1500k", "-preset", "veryslow",
    "-c:a", "aac", "-b:a", "192k", "-ac", "2",
    "-pix_fmt", "yuv420p", "-shortest", "-y", output_file
    ]
    
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if process.returncode != 0:
        print("FFmpeg Error:")
        print(process.stderr)
    else:
        print(f"Video saved as {output_file}")
    
    return output_file
