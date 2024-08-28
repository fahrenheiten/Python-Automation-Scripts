import os


def get_image_files(directory, img_extensions):
    """Генератор, возвращающий пути изображений в заданной директории и её поддиректориях."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().split('.')[-1] in img_extensions:
                yield root, file


def rename_images(directory, img_extensions):
    """Переименовывает изображения, используя их тип и индекс."""
    for index, (root, file) in enumerate(get_image_files(directory, img_extensions)):
        old_path = os.path.join(root, file)
        extension = file.lower().split('.')[-1]
        new_name = f'{index}.{extension}'
        new_path = os.path.join(root, new_name)

        os.rename(old_path, new_path)
        print(f"Файл '{file}' переименован в '{new_name}'.")


def main():
    """Основная функция."""
    img_extensions = ['jpg', 'png', 'jpeg']
    base_directory = '.'
    rename_images(base_directory, img_extensions)
    print("Переименование изображений завершено.")


if __name__ == "__main__":
    main()

