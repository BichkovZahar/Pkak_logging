import logging
def write_file(fill_path , data):
    try:
        with open(fill_path , 'w') as file:
            file.write(data)
            logging.basicConfig(level=logging.INFO,
                                filename="logss.log",
                                filemode='w',
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(f"Дані з файлу {fill_path} успішно додано")
        return data
    except Exception as e:
        logging.error(f'Сталася помилка під час  з файлу {fill_path}')
        return None

write_file("output.txt" , input("Введіть що треба вписати файл: "))
