from moviepy.editor import TextClip, CompositeVideoClip
import cv2

def create_video_from_text(text, output_file="output_video.mp4"):
    # Text clip setup
    clip = TextClip(text, fontsize=70, color='white', bg_color='black', size=(1280, 720))
    clip = clip.set_duration(5)
    
    # Exporting
    video = CompositeVideoClip([clip])
    video.write_videofile(output_file, fps=24)

# Example usage
create_video_from_text("Harish, aapka video ready hai!")
