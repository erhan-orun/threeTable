import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
import datetime as dt
import pandas as pd
import pymongo
import cnfOperations as cnf
import recordMongo_3 as rm_3
import sys
import plotly.express as px
import numpy as np


class ModbusOop(object):
    def __init__(self):
        self.regs_count = len(cnf.cnfOperation.readSensorNo_3())
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.style.map("Treeview", foreground=self.fixed_map("foreground"), background=self.fixed_map("background"))
        self.tree_3 = ttk.Treeview(self.root)

    def fixed_map(self, option):
        return [elm for elm in self.style.map("Treeview", query_opt=option) if elm[:2] != ("!disabled", "!selected")]

    def on_double_click(self, event):
        item = self.tree_3.identify('item', event.x, event.y)

        print(self.tree_3.item(item, "text"))

        myclient = pymongo.MongoClient(cnf.cnfOperation.readMongoDb())
        mydb = myclient[cnf.cnfOperation.readMy_Db()]
        mycol = mydb[cnf.cnfOperation.readMy_Col_3()]

        xs_doc = list(
            mycol.find(
                {"$and": [{"Sensor No": self.tree_3.item(item, "text")},
                          {"Time": {"$gte": "2021-05-31 13:14:58",
                                    "$lt": dt.datetime.now().strftime('%Y-%m-%d %X')}}]},
                {'_id': 0}))

        xs_res = [list(idx.values()) for idx in xs_doc]

        df = pd.DataFrame(list(xs_doc))
        df['Temp'] = df['Temp'].astype(np.float64)

        for index1, row in enumerate(xs_res):
            for index2, item in enumerate(row):
                try:
                    xs_res[index1][index2] = (float(item))
                except ValueError:
                    pass
        df = pd.DataFrame(xs_doc)
        df['Temp'] = df['Temp'].astype(np.float64)
        fig = px.line(df, x='Time', y='Temp', title='Temperature °C - Time', color='Sensor No')

        fig.update_xaxes(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=3, label="3m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        return fig.show()

    def _quit(event):
        sys.exit()

    def window_table(self):

        self.root.title("Sensor's Temperatures °C")
        self.root.geometry("480x630")
        self.root.grid()

        self.tree_3.pack(side='top', fill=tkinter.BOTH, expand=True)

        verscrlbar = ttk.Scrollbar(self.root,
                                   orient="vertical",
                                   command=self.tree_3.yview)

        self.tree_3.configure(xscrollcommand=verscrlbar.set)

        self.tree_3["columns"] = ("1", "2", "3")

        self.tree_3['show'] = 'headings'

        self.tree_3.column("1", width=125, minwidth=30, anchor='c')
        self.tree_3.column("2", width=65, minwidth=30, anchor='c')
        self.tree_3.column("3", width=115, minwidth=30, anchor='c')

        self.tree_3.heading("1", text="Time")
        self.tree_3.heading("2", text="Sensor No")
        self.tree_3.heading("3", text="Temperature °C")

        self.tree_3.bind("<Double-1>", self.on_double_click)

        rem = rm_3.RecordMongo
        start_range = 0
        id_count = 1

        self.tree_3.tag_configure('high', foreground='red')
        self.tree_3.tag_configure('low', foreground='black')

        for record in rem.record_mongo()[-(self.regs_count):]:
            sensor_id = record[0]
            temperature = record[1]
            date_time = record[2]
            if float(temperature) > 30.0:
                self.tree_3.insert("", index='end', text="%s" % int(sensor_id), iid=start_range,
                                   values=(str(date_time), int(sensor_id), float(temperature)), tags=('high',))
            else:
                self.tree_3.insert("", index='end', text="%s" % int(sensor_id), iid=start_range,
                                   values=(str(date_time), int(sensor_id), float(temperature)), tags=('low',))

            start_range += 1
            id_count += 1

        menu = Menu(self.root)
        self.root.config(menu=menu)
        menu.add_cascade(label='Quit', command=self._quit)

        self.tree_3.after(60000, self.update_window_table)
        return self.root.mainloop()

    def update_window_table(self):
        rem = rm_3.RecordMongo
        start_range = 0
        id_count = 1

        for i in self.tree_3.get_children():
            self.tree_3.delete(i)

        for record in rem.record_mongo()[-(self.regs_count):]:
            sensor_id = record[0]
            temperature = record[1]
            date_time = record[2]
            if float(temperature) > 30.0:
                self.tree_3.insert("", index='end', text="%s" % int(sensor_id), iid=start_range,
                                   values=(str(date_time), int(sensor_id), float(temperature)), tags=('high',))
            else:
                self.tree_3.insert("", index='end', text="%s" % int(sensor_id), iid=start_range,
                                   values=(str(date_time), int(sensor_id), float(temperature)), tags=('low',))

            start_range += 1
            id_count += 1

        self.root.update()
        self.root.update_idletasks()
        self.tree_3.after(60000, self.update_window_table)
        return self.root.mainloop()
