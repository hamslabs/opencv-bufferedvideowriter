# OpenCV BufferedVideoWriter

**OpenCV BufferedVideoWriter** is an extension of the classic `VideoWriter` class in OpenCV. It addresses synchronization issues with frames per second (fps) by providing a buffered approach.

## Features

- Seamless integration with OpenCV.
- Solves synchronization problems commonly encountered with `VideoWriter` fps settings.
- Easy-to-use: Simply instantiate it like the parent class `VideoWriter`, but use `BufferedVideoWriter`, and provide `start()` and `stop()` methods.

## Installation

You can install `opencv-bufferedvideowriter` via pip:

```bash
pip install opencv-bufferedvideowriter
```

## Usage

1. Import `BufferedVideoWriter`:

```python
from opencv_bufferedvideowriter import BufferedVideoWriter
```

2. Instantiate `BufferedVideoWriter`:

```python
output_file = 'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
frame_size = (640, 480)

writer = BufferedVideoWriter(output_file, fourcc, fps, frame_size)
```

3. Start writing frames:

```python
# Start the video writing process
writer.start()

# Write frames
for frame in frames:
    writer.write(frame)

# Stop the video writing process
writer.stop()
```

## Example

```python
import cv2
from opencv_bufferedvideowriter import BufferedVideoWriter

output_file = 'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
frame_size = (640, 480)

# Example frames
frames = [...]  # Your frames here

# Instantiate BufferedVideoWriter
writer = BufferedVideoWriter(output_file, fourcc, fps, frame_size)

# Start the video writing process
writer.start()

# Write frames
for frame in frames:
    writer.write(frame)

# Stop the video writing process
writer.stop()
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
