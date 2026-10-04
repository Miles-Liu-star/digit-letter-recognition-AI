from pathlib import Path
import sys

import numpy as np
from PIL import Image


def main():
	image_path = Path(__file__).resolve().parent / "test-images" / "2.png"  # 此处在选取不同图片用于测试时需更改路径
	with Image.open(image_path) as image:
		# Convert to grayscale; each value is a pixel's brightness (0-255).
		brightness_array = np.asarray(image.convert("L"))

	print(brightness_array)
	print(f"Array shape (height, width): {brightness_array.shape}")


if __name__ == "__main__":
	main()
