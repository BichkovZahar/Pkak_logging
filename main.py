import logging
def write_file(fill_path , data):
    try:
        with open(fill_path , 'w') as file:
            logger = logging.getLogger("File")
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler())
            file.write(data)
            logger.info("Успішно записали файл")
    except Exception as a:
        logger.error(f"В вашему файлі '{fill_path}' трапилась помилка -> {a}")
logging.basicConfig(level=logging.INFO)
write_file("output.txt" , input("Введіть що треба вписати файл: "))