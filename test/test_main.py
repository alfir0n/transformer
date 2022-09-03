from os import remove
from os.path import exists

from src.config import FILE_ROOT_PATH
from src.conv import convertHeicImage

OUTPUT_FILE: str = "lawn-backyard.jpg"


def teardown_function():
    remove(f"{FILE_ROOT_PATH}/out/{OUTPUT_FILE}")

def test_image_conversion():
    input_file = "lawn-backyard.HEIC"

    convertHeicImage(input_file)

    assert exists(f"{FILE_ROOT_PATH}/out/{OUTPUT_FILE}")
