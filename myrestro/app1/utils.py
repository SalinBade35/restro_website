import qrcode
import os

def generate_qr_code(url, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image in the static/images directory
    image_path = os.path.join("app1/static/images", filename)
    img.save(image_path)  # Save the QR code image
    
    return f"images/{filename}"  # Return the relative path for template usage
