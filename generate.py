import qrcode
from PIL import Image, ImageDraw, ImageFont
import sys

def generate_qr_code(link, title):
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=3)
    qr.add_data(link)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")

    # Create frame image
    frame_width = qr_image.size[0] + 20
    frame_height = qr_image.size[1] + 45
    frame_image = Image.new("RGB", (frame_width, frame_height), "white")

    # Paste QR code onto frame image
    qr_pos = ((frame_width - qr_image.size[0]) // 2, 10)
    frame_image.paste(qr_image, qr_pos)

    # Add title below QR code
    draw = ImageDraw.Draw(frame_image)
    title_font = ImageFont.truetype("Arial Unicode.ttf", 24)
    title_width, title_height = draw.textsize(title, font=title_font)
    
    # Adjust the vertical position of the title
    title_offset = 5  # Adjust this value to move the title up or down
    title_pos = ((frame_width - title_width) // 2, qr_pos[1] + qr_image.size[1] + title_offset)
    draw.text(title_pos, title, font=title_font, fill="black")

    # Save the final frame image
    filename = title.lower().replace(" ", "_") + ".png"
    frame_image.save(filename)
    print(f"QR code frame saved as {filename}.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate.py <link> <title>")
        sys.exit(1)
        
    link = sys.argv[1]
    title = sys.argv[2]
    generate_qr_code(link, title)

