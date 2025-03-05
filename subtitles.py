from datetime import timedelta

def generate_srt(subtitle_text, audio_duration, output_file='outputs/subtitles.srt'):
    lines = [line.strip() for line in subtitle_text.split('. ') if line.strip()]  # Remove empty lines
    num_lines = len(lines)

    min_display_time = 3  # Minimum subtitle duration in seconds
    avg_time_per_line = max(audio_duration / num_lines, min_display_time)  # Ensuring minimum display time

    srt_content = []
    start_time = 0

    for i, line in enumerate(lines):
        end_time = start_time + avg_time_per_line
        srt_content.append(f"{i+1}\n")
        srt_content.append(f"{format_time(start_time)} --> {format_time(end_time)}\n")
        srt_content.append(f"{line}.\n\n")  # Ensure each subtitle ends with a period
        start_time = end_time

    # Save the SRT content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(srt_content)

    print(f"Subtitles saved as {output_file}")
    return output_file

def format_time(seconds):
    # Format seconds into hh:mm:ss,mmm format
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    milliseconds = int((td.total_seconds() - total_seconds) * 1000)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
