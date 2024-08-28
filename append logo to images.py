import os
from PIL import Image

def get_logo_and_folder():
    """Получение имени логотипа и создание новой папки для изображений с логотипом."""
    logo_name = input("Введите название файла с логотипом (с расширением): ")
    folder_name = input("Введите имя новой папки для сохранения изображений: ")
    if not os.path.exists(logo_name):
        raise FileNotFoundError(f"Логотип '{logo_name}' не найден.")
    os.makedirs(folder_name, exist_ok=True)
    return logo_name, folder_name

def process_images(logo_path, output_folder):
    """Обработка изображений: добавление логотипа и сохранение в новую папку."""
    logo = Image.open(logo_path)
    for file in (f for f in os.listdir() if f.lower().endswith(('.png', '.jpg')) and f != logo_path):
        add_logo_to_image(file, logo, output_folder)

def add_logo_to_image(image_path, logo, output_folder):
    """Добавление логотипа на изображение и сохранение результата."""
    img = Image.open(image_path)
    position = (img.width - logo.width, img.height - logo.height)
    img.paste(logo, position, logo)
    img.save(os.path.join(output_folder, image_path))
    print(f"Логотип добавлен на '{image_path}'.")

def main():
    """Основная функция."""
    try:
        logo_filename, new_folder = get_logo_and_folder()
        process_images(logo_filename, new_folder)
        print("Все изображения успешно обработаны!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
