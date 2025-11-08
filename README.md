# Multi Conv

Multi Conv is a terminal utility for quickly converting image and video files without fussing with online tools. It wraps Pillow and MoviePy to batch those one-off format changes into a tiny menu-driven CLI.

## Features

- Convert between most Pillow-friendly image formats (JPEG, PNG, WEBP, TIFF, etc.)
- Transcode common video containers (MP4, MOV, MKV, WEBM, GIF) using ffmpeg via MoviePy
- Simple text UI with input validation so you don’t accidentally overwrite files

## Requirements

- Python 3.9+
- [Pillow](https://python-pillow.org/)
- [MoviePy](https://zulko.github.io/moviepy/)
- [ffmpeg](https://ffmpeg.org/) available on your `PATH`

Quick install:

```bash
pip install -r requirements.txt  # or: pip install pillow moviepy
```

## Usage

```bash
python main.py
```

1. Pick `Image` or `Video` conversion from the menu.
2. Provide the source file path (local file only; drag-and-drop into the terminal works).
3. Enter the desired output filename, including the extension that matches your target format.
4. Wait for the conversion message and repeat as needed.

## Notes

- Video conversions rely on ffmpeg codecs. For formats beyond MP4/WebM/GIF, edit `converters/video_converter.py` to tweak codec settings.
- If conversion fails, check the terminal output for MoviePy/ffmpeg errors—they usually point to missing codecs or unsupported combinations.

## License

MIT © nzxi (see `LICENSE`).
