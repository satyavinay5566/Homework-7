import os
import qrcode
from datetime import datetime

print(">>> Starting app.py <<<")

try:
    repo_url = os.getenv("GITHUB_REPO_URL", "https://github.com/satyavinay5566/Homework-7")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"Output_img{timestamp}.png"
    output_dir = "Output_img"

    os.makedirs(output_dir, exist_ok=True)

    img = qrcode.make(repo_url)

    full_path = os.path.join(output_dir, file_name)
    print(f"Saving to: {os.path.abspath(full_path)}")
    img.save(full_path)

    print(f"✅ QR code saved to {full_path}")

except Exception as e:
    print(f"❌ Error: {e}")
