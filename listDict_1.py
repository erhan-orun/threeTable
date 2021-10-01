import numpy as np
import datetime as dt
import cnfOperations as cnf
import connectModbus_1 as cm_1


class ListDict():
    @staticmethod
    def list_to_dict():
        con = cm_1.ConnectModbus()
        regs_count = len(cnf.cnfOperation.readSensorNo_1())

        value = [[num for num in range(1, 1 + regs_count)], cnf.cnfOperation.readSensorNo_1(), con.connect_modbus()]

        data = np.array(value).T.tolist()

        products = data
        arr = []
        for product in products:
            vals = {}
            vals["Sensor No"] = str(int(product[1]))
            vals["Temp"] = str(round(product[2], 4))
            vals["Time"] = str(dt.datetime.now().strftime('%Y-%m-%d %X'))
            arr.append(vals)
        return arr
