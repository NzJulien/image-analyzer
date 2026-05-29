import anthropic
import base64
import sys
from pathlib import Path

def encode_image(image_path: str) -> tuple[str, str]:
    """Encode image to base64 and detect media type."""
    path = Path(image_path)
    ext = path.suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    media_type = media_types.get(ext, "image/jpeg")
    with open(image_path, "rb") as f:
        image_data = base64.standard_b64encode(f.read()).decode("utf-8")
    return image_data, media_type

def describe_image(image_path: str) -> str:
    """Send image to Claude and get a description/caption."""
    client = anthropic.Anthropic()

    image_data, media_type = encode_image(image_path)

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Please provide a detailed description and caption for this image. Include what you see, the mood, colors, and any notable details.",
                    },
                ],
            }
        ],
    )
    return message.content[0].text

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        print("Example: python main.py photo.jpg")
        sys.exit(1)

    image_path = sys.argv[1]

    if not Path(image_path).exists():
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    print(f"Analyzing image: {image_path}\n")
    print("=" * 50)
    description = describe_image(image_path)
    print(description)
    print("=" * 50)

if __name__ == "__main__":
    main()
