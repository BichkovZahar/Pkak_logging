import logging
import random

def real_data(file_path):
    try:
        with open(file_path , "w") as file:
            logger = logging.getLogger("File")
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler())
            random_number = [str(random.randint(1 , 100)) for i in range(5)]
            file.write("\n".join(random_number))
            logger.info("Успішно записали файл")
    except Exception as a:
        logger.error(f"В файлі {file_path} трапилась помилка {a}")
logging.basicConfig(level=logging.INFO)
real_data(input("Введіть назву файла: "))