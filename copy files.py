import os
import shutil


def create_target_folder(folder_name):
    """Создание целевой папки для копирования файлов."""
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return folder_name


def find_and_copy_files(source_directory, target_directory, extensions):
    """Поиск и копирование файлов с определёнными расширениями."""
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(tuple(extensions)):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(target_directory, file)
                shutil.copy2(source_path, destination_path)
                print(f"Файл '{file}' скопирован в '{target_directory}'.")


def main():
    """Основная функция."""
    target_folder = create_target_folder('destination_folder')
    find_and_copy_files('.', target_folder, ['.jpg', '.pdf'])
    print("Все файлы успешно скопированы.")


if __name__ == "__main__":
    main()