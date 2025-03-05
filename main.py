import os
from tts import text_to_speech
from subtitles import generate_srt
from video_generator import create_video_with_ffmpeg

def validate_file(file_path, file_type):
    """Check if a file exists and print a debug message."""
    if not os.path.exists(file_path):
        print(f"[ERROR] {file_type} was not generated: {file_path}")
        return False
    print(f"[SUCCESS] {file_type} exists: {file_path}")
    return True

def generate_social_media_video(text, image_file):
    print("[INFO] Starting social media video generation...")

    # Step 1: Generate Audio
    print("[INFO] Generating audio...")
    audio_file = text_to_speech(text)
    if not validate_file(audio_file, "Audio file"):
        return None

    # Step 2: Generate Subtitles
    print("[INFO] Generating subtitles...")
    # Replace with an actual audio duration calculation if available
    audio_duration = 10  
    subtitle_file = generate_srt(text, audio_duration)
    if not validate_file(subtitle_file, "Subtitle file"):
        return None

    # Step 3: Create Video
    print("[INFO] Generating video...")
    try:
        video_file = create_video_with_ffmpeg(image_file, audio_file, subtitle_file)
        if not validate_file(video_file, "Video file"):
            return None
        print("[SUCCESS] Video generation completed.")
        return video_file
    except Exception as e:
        print(f"[ERROR] Video generation failed: {e}")
        return None

if __name__ == "__main__":
    # Example inputs
    text = (
        "Russian air defenses may have shot down an Azerbaijan Airlines flight after misidentifying it, according to US military sources. Two unnamed  officials who spoke to Sky News' US partner NBC News said America had  intelligence indicating Russia may have believed the flight was a drone  and engaged its air defences."
    )
    image_file = os.path.abspath("static/f35.jpeg")

    # Print paths for debugging
    print(f"[INFO] Using background image: {image_file}")
    print(f"[INFO] Working directory: {os.getcwd()}")

    # Run video generation
    video_path = generate_social_media_video(text, image_file)
    if video_path:
        print(f"[INFO] Generated video: {video_path}")
    else:
        print("[ERROR] Video generation failed.")
