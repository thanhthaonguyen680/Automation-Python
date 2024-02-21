import configparser

# Tạo một đối tượng ConfigParser
config = configparser.ConfigParser()

# Đọc tập tin cấu hình
config.read("/Users/nfqasia/PycharmProjects/Digiflow/Configurations/config.ini")

class ReadConfig:
    @staticmethod
# Lấy giá trị từ tập tin cấu hình
    def getAplicationURL():
        url = config.get('common infor', 'BaseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common infor', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common infor', 'password')
        return password


# # Lấy giá trị từ tập tin cấu hình
# database_host = config.get('database', 'host')
# database_port = config.get('database', 'port')
#
# # Sử dụng giá trị trong ứng dụng
# print(f"Database host: {database_host}")
# print(f"Database port: {database_port}")
