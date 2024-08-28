import os
import shutil
from collections import defaultdict


def categorize_files():
    """Возвращает словарь с категориями файлов и их соответствующими расширениями."""
    return {
        'images': [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm"],
        'music': [".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw"],
        'videos': [".webm", ".mp4"],
        'executables': [".exe", ".msi", ".deb", ".dmg"],
        'archives': [".rar", ".tar", ".zip", ".gz"],
        'torrents': [".torrent"],
        'documents': [".txt", ".pdf", ".docx", ".doc"],
        'code': [".py", ".php", ".html", ".css", ".js"],
        'design_files': [".psd", ".ai"],
    }


def organize_files(base_dir, categories):
    """Организация файлов в папки по категориям."""
    files_moved = defaultdict(int)  # Счётчик перемещённых файлов по категориям

    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)
        if os.path.isfile(file_path):
            for category, extensions in categories.items():
                if file.lower().endswith(tuple(extensions)):
                    target_dir = os.path.join(base_dir, category)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, target_dir)
                    files_moved[category] += 1
                    break

    return files_moved


def main():
    """Основная функция."""
    base_directory = os.getcwd()
    categories = categorize_files()
    try:
        print("Начинаем организацию ваших файлов по категориям...")
        files_moved = organize_files(base_directory, categories)

        for category, count in files_moved.items():
            print(f"{count} файл(ов) перемещено в папку '{category}'.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("Организация файлов завершена.")


if __name__ == "__main__":
    main()
