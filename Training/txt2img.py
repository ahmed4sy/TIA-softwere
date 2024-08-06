from PIL import Image, ImageDraw, ImageFont

def create_image_with_border(text, font_path, font_size, text_color, outline_color, outline_thickness, image_size, output_image_path):
    # إنشاء صورة فارغة
    image = Image.new("RGB", image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # تحميل الخط
    font = ImageFont.truetype(font_path, font_size)

    # حساب حجم النص وموقعه
    text_width, text_height = draw.textsize(text, font=font)
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

    # رسم التحديد (outline)
    for dx in range(-outline_thickness, outline_thickness + 1):
        for dy in range(-outline_thickness, outline_thickness + 1):
            if dx != 0 or dy != 0:
                draw.text((position[0] + dx, position[1] + dy), text, font=font, fill=outline_color)

    # رسم النص
    draw.text(position, text, font=font, fill=text_color)

    # حفظ الصورة بصيغة TIFF
    image.save(output_image_path, format='TIFF')

    # كتابة ملف .box
    box_file_path = output_image_path.replace('.tif', '.box')
    write_box_file(text, font, position, box_file_path, image_size)
    print(f"Image and box file saved to {output_image_path} and {box_file_path}")

def write_box_file(text, font, position, box_file_path, image_size):
    with open(box_file_path, 'w') as f:
        x, y = position
        for char in text:
            # الحصول على حجم الحرف
            width, height = font.getsize(char)
            # حساب إحداثيات الزاوية اليسرى العليا واليمنى السفلى
            x1, y1 = x, y
            x2, y2 = x + width, y + height
            # كتابة إحداثيات الصندوق في الملف
            f.write(f"{char} {x1} {image_size[1] - y2 -2} {x2} {image_size[1] - y1+1} 0\n")
            x += width  # تحريك المؤشر إلى اليمين بمقدار عرض الحرف
    print(f"Box file written to {box_file_path}")


# text = "Chapter 61:"
# font_path = "/usr/share/fonts/truetype/msttcorefonts/Impact.ttf"
# font_size = 32
# text_color = (255, 255, 255)  # اللون الأحمر
# outline_color = (0, 0, 0)  # اللون الأسود
# outline_thickness = 2
# image_size = (700, 250)
# output_image_path = "output_with_border.tif"

# create_image_with_border(text, font_path, font_size, text_color, outline_color, outline_thickness, image_size, output_image_path)

