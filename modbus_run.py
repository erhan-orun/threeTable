import modbus_oop as mop
import getMongo_1 as gm_1
import getMongo_2 as gm_2
import getMongo_3 as gm_3
import sys


def main():
    while True:
        rn = mop.ModbusOop()
        rn.window_table()
        rn.update_window_table()
        gvm_1 = gm_1.GetMongo()
        gvm_1.get_value_mongo()
        gvm_2 = gm_2.GetMongo()
        gvm_2.get_value_mongo()
        gvm_3 = gm_3.GetMongo()
        gvm_3.get_value_mongo()
        sys.exit()


if __name__ == '__main__':
    main()
