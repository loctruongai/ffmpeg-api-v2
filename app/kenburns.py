import uuid
import subprocess
import requests

def generate_kenburns(image_url):
    filename = f"/tmp/{uuid.uuid4().hex}.jpg"
    output = f"/tmp/{uuid.uuid4().hex}.mp4"

    # Tải ảnh về
    with open(filename, "wb") as f:
        f.write(requests.get(image_url).content)

    # Chạy FFMPEG để tạo chuyển động
    command = [
        "ffmpeg", "-y", "-loop", "1", "-i", filename,
        "-vf", "zoompan=z='min(zoom+0.0005,1.5)':d=150:s=1280x720",
        "-c:v", "libx264", "-t", "6", "-pix_fmt", "yuv420p", output
    ]

    try:
        subprocess.run(command, check=True)
        return {"status": "success", "video_path": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "detail": str(e)}
