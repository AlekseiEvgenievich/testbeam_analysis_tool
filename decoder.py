import struct
import csv
import matplotlib.pyplot as plt
import os
import pandas as pd
import sys
import numpy as np
import time
#100*10-9
class DataHandler:
    def __init__(self, file_path, stairs=False):
        self.file_path = file_path
        self.stairs = stairs
        self.fieldnames = self.get_fieldnames()
        self.data_ts = []
        self.time_init = 0
        self.temp_hg = []
        self.temp_lg = []

    def get_fieldnames(self):
        fieldnames = ['TIMES. ABS. (10ns)', 'TIMES. (1ms)', 'TRIGGERID', 'DAQ ID 1', 'TRIGGER COUNTS 1', 'VALID 1', 'FLAG 1', 'VALIDATED 1', 'LOST 1', 'DAQ ID 2', 'TRIGGER COUNTS 2', 'VALID 2', 'FLAG 2', 'VALIDATED 2', 'LOST 2']
        for x in range(4):
            for y in range(32):
                fieldnames.append(f'DAQ1_Asic{x}_CH{y}_HG')
                fieldnames.append(f'DAQ1_Asic{x}_CH{y}_LG')
        for x in range(4):
            for y in range(32):
                fieldnames.append(f'DAQ2_Asic{x}_CH{y}_HG')
                fieldnames.append(f'DAQ2_Asic{x}_CH{y}_LG')
        return fieldnames

    def write_data_csv(self, data):
        with open(self.file_path + '.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames, delimiter=';')
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def decode_data_buffer(self, data_buffer):
        timestamp = int((data_buffer[0]-self.time_init)/100000)
        self.time_init = data_buffer[0]
        trigger_id = data_buffer[1]

        daq1_id = (data_buffer[2] & 0xFFFFFFFF)
        trigger1_counts = (data_buffer[2] >> 32)
        valid1 = (data_buffer[3] & 0xFFFFFFFF)
        flag1 = (data_buffer[3] >> 32)

        for i in range (4, 68):
            self.temp_hg.append(data_buffer[i] & 0x3FFF)
            self.temp_lg.append(data_buffer[i] >> 14 & 0x3FFF)
            self.temp_hg.append((data_buffer[i] >> 32) & 0x3FFF)
            self.temp_lg.append((data_buffer[i] >> 32) >> 14 & 0x3FFF)

        lost1 = data_buffer[68]
        validated1 = data_buffer[69]

        daq2_id = (data_buffer[70] & 0xFFFFFFFF)
        trigger2_counts = (data_buffer[70] >> 32)
        valid2 = (data_buffer[71] & 0xFFFFFFFF)
        flag2 = (data_buffer[71] >> 32)

        for i in range (72, 136):
            self.temp_hg.append(data_buffer[i] & 0x3FFF)
            self.temp_lg.append(data_buffer[i] >> 14 & 0x3FFF)
            self.temp_hg.append((data_buffer[i] >> 32) & 0x3FFF)
            self.temp_lg.append((data_buffer[i] >> 32) >> 14 & 0x3FFF)

        lost2 = data_buffer[136]
        validated2 = data_buffer[137]

        new_data = {'TIMES. ABS. (10ns)': self.time_init, 'TIMES. (1ms)':timestamp, 'TRIGGERID': trigger_id,
                    'DAQ ID 1': str(hex(daq1_id)), 'TRIGGER COUNTS 1': trigger1_counts, 'VALID 1': valid1, 'FLAG 1': flag1, 'VALIDATED 1': validated1, 'LOST 1': lost1,
                    'DAQ ID 2': str(hex(daq2_id)), 'TRIGGER COUNTS 2': trigger2_counts, 'VALID 2': valid2, 'FLAG 2': flag2, 'VALIDATED 2': validated2, 'LOST 2': lost2}
                    
        for x in range(4):
            for y in range(32):
                asic_ch_hg = f'DAQ1_Asic{x}_CH{y}_HG'
                asic_ch_lg = f'DAQ1_Asic{x}_CH{y}_LG'
                new_data[asic_ch_hg] = self.temp_hg[(x*32)+(y)]
                new_data[asic_ch_lg] = self.temp_lg [(x*32)+(y)]
        
        for x in range(4):
            for y in range(32):
                asic_ch_hg = f'DAQ2_Asic{x}_CH{y}_HG'
                asic_ch_lg = f'DAQ2_Asic{x}_CH{y}_LG'
                new_data[asic_ch_hg] = self.temp_hg[(x*32)+(y)+128]
                new_data[asic_ch_lg] = self.temp_lg [(x*32)+(y)+128]
                
        self.data_ts.append(new_data)
        self.temp_hg.clear()
        self.temp_lg.clear()

    def open_data(self):
        with open(self.file_path + ".bin", "rb") as file:
            data = file.read()

        if self.stairs:
            packet_size = struct.calcsize("I" * 288)
        else:
            packet_size = struct.calcsize("Q" * 138)

        offset = 0

        while offset + packet_size <= len(data):
            packet_data = data[offset:offset + packet_size]
            if self.stairs:
                data_buffer = struct.unpack("I" * 288, packet_data)
                self.decode_stairs_buffer(data_buffer)
            else:
                data_buffer = struct.unpack("Q" * 138, packet_data)
                self.decode_data_buffer(data_buffer)

            offset += packet_size

 #   def decode_stairs_buffer(self, data_buffer):
        # Processing code here...

if __name__ == '__main__':
    handler = DataHandler("./data")
    handler.open_data()
    handler.write_data_csv(handler.data_ts)

