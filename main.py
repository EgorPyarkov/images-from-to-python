import os
from PIL import Image

# Получить список всех файлов в папке
for i in range(1, 48):
    # Путь до файлов
    files = os.listdir(f'путь/до/файлов/{i}')
    for file in files:
        ext = os.path.splitext(file)[1].lower()

        if ext in ['.png', '.webp']:
            im = Image.open(f'путь/до/файлов/{i}/' + file)
            rgb_im = im.convert('RGB')
            rgb_im.save(f'путь/до/файлов/{i}/' + file.replace(ext, '.jpg'))
            os.remove(f'путь/до/файлов/{i}/' + file)

