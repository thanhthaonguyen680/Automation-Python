import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger('hihi')
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Tạo một file log để lưu lại thông tin
        file_handler = logging.FileHandler('/Users/nfqasia/PycharmProjects/Digiflow/Logs/your_page_object_logs.log')
        file_handler.setFormatter(log_format)
        # Đưa file handler vào logger
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger








