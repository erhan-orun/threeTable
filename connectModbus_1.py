import numpy as np
import math
from pyModbusTCP.client import ModbusClient
import cnfOperations as cnf


class ConnectModbus():

    @staticmethod
    def connect_modbus():
        global host, portNo, regs
        regNoList = []
        resultList = []
        for i in cnf.cnfOperation.readSensorNo_1():
            host = cnf.cnfOperation.readModBusHost()
            groupNo = math.floor(((int(cnf.cnfOperation.readLineNo_1()) - 1) / 256)) + 1
            portNo = 10000 + (int(cnf.cnfOperation.readSensorTypeNo_1()) - 1) * 10 + groupNo - 1
            regNo = (((int(cnf.cnfOperation.readLineNo_1()) - 1) * 128 + (int(i) - 1)) * 2) % 65536
            regNoList.append(regNo)

        for x in regNoList:
            sensor_no = ModbusClient(host=host, port=portNo, unit_id=1, auto_open=True)
            sensor_no.open()
            regs = sensor_no.read_holding_registers(x, 2)
            if regs:
                print(regs)
            else:
                print("read error")

            regs[0], regs[1] = regs[1], regs[0]
            data_bytes = np.array(regs, dtype=np.uint16)
            result = data_bytes.view(dtype=np.float32)
            resultList.append(result[0])

        data_as_float = resultList
        return data_as_float
