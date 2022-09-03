import pyheif
from PIL import Image

from src.config import FILE_ROOT_PATH, FORMAT

def convertHeicImage(file_name: str):
    # transform first to jpg
    heif_file = pyheif.read(f"{FILE_ROOT_PATH}/in/{file_name}")
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    file_name_new = file_name.replace("HEIC","jpg")
    image.save(f"{FILE_ROOT_PATH}/out/{file_name_new}", FORMAT)

