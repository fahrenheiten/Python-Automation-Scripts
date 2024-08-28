import os
from PIL import Image

def resize_image(image, max_size):
    """Изменяет размер изображения, сохраняя пропорции, до заданного максимального размера."""
    width, height = image.size
    if width <= max_size and height <= max_size:
        return image

    if width > height:
        new_height = int((max_size / width) * height)
        new_size = (max_size, new_height)
    else:
        new_width = int((max_size / height) * width)
        new_size = (new_width, max_size)

    return image.resize(new_size, Image.ANTIALIAS)

def process_images(input_folder, output_folder, max_size):
    """Обрабатывает все изображения в указанной папке и сохраняет их с изменённым размером в новую папку."""
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if file.lower().endswith(('.png', '.jpg')) and os.path.isfile(file_path):
            image = Image.open(file_path)
            resized_image = resize_image(image, max_size)
            output_path = os.path.join(output_folder, file)
            resized_image.save(output_path)
            print(f"Изображение '{file}' изменено и сохранено в '{output_folder}'.")

def main():
    """Основная функция."""
    max_size = int(input("Введите максимальный размер для изображения: "))
    output_folder = input("Введите имя папки для сохранения изменённых изображений: ")
    input_folder = '.'  # Текущая директория

    process_images(input_folder, output_folder, max_size)
    print("Обработка всех изображений завершена.")

if __name__ == "__main__":
    main()
