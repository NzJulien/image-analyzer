# 🖼️ Image Analyzer

A Python CLI app that uses Claude's vision capabilities to generate detailed descriptions and captions for images.

## Features

- Accepts common image formats: JPG, PNG, GIF, WEBP
- Generates rich, detailed descriptions including mood, colors, and notable details
- Simple command-line interface

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/NzJulien/image-analyzer.git
   cd image-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Anthropic API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

```bash
python main.py <image_path>
```

**Examples:**
```bash
python main.py photo.jpg
python main.py /path/to/image.png
```

## Example Output

```
Analyzing image: sunset.jpg
==================================================
This stunning photograph captures a vibrant sunset over a calm ocean...
==================================================
```

## Requirements

- Python 3.8+
- Anthropic API key (get one at https://console.anthropic.com)

## License

MIT
