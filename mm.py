from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(input_path: str, output_path: str):
    input_path = input_path.strip()  # Bo'sh joylarni olib tashlash
    output_path = output_path.strip()  # Bo'sh joylarni olib tashlash
    
    # Video faylini yuklaymiz
    clip = VideoFileClip(input_path)
    
    # .mp4 formatga o'zgartiramiz
    clip.write_videofile(output_path, codec='libx264')
    
    # Video klipni yopamiz
    clip.close()

# Funksiyani ishlatish:
input_file = "D:\\dasturllash\\krdarama\\mmm\\IMG_2894.mov"
output_file = "D:\\dasturllash\\krdarama\\mmm\\IMG_2894.mp4"
convert_mov_to_mp4(input_file, output_file)
