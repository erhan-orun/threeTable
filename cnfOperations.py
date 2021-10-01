import configparser
import ast


class cnfOperation():

    @staticmethod
    def readModBusHost():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Modbus_host']['host']

    @staticmethod
    def readSensorTypeNo_1():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Sensor_Type_No_1']['sensorTypeNo_1']

    @staticmethod
    def readLineNo_1():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Line_No_1']['lineNo_1']

    @staticmethod
    def readSensorNo_1():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return ast.literal_eval(config.get("Sensor_No_1", "sensorNo_1"))

    @staticmethod
    def readSensorTypeNo_2():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Sensor_Type_No_2']['sensorTypeNo_2']

    @staticmethod
    def readLineNo_2():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Line_No_2']['lineNo_2']

    @staticmethod
    def readSensorNo_2():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return ast.literal_eval(config.get("Sensor_No_2", "sensorNo_2"))

    @staticmethod
    def readSensorTypeNo_3():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Sensor_Type_No_3']['sensorTypeNo_3']

    @staticmethod
    def readLineNo_3():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Line_No_3']['lineNo_3']

    @staticmethod
    def readSensorNo_3():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return ast.literal_eval(config.get("Sensor_No_3", "sensorNo_3"))

    @staticmethod
    def readMongoDb():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['Mongo_DB']['client']

    @staticmethod
    def readMy_Db():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['My_DB']['my_client']

    @staticmethod
    def readMy_Col_1():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['My_Col_1']['My_db_1']

    @staticmethod
    def readMy_Col_2():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['My_Col_2']['My_db_2']

    @staticmethod
    def readMy_Col_3():
        config = configparser.ConfigParser()
        config.read('Config.ini')
        return config['My_Col_3']['My_db_3']
