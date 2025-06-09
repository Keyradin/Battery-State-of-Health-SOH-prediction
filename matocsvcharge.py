from scipy.io import loadmat
import os
import pandas as pd
import numpy as np


def load_data(mat_path, battery):
    mat = loadmat(mat_path)
    counter = 0
    dataset = []

    for i in range(len(mat[battery][0, 0]['cycle'][0])):
        row = mat[battery][0, 0]['cycle'][0, i]
        if row['type'][0] == 'charge':
            ambient_temperature = row['ambient_temperature'][0][0]
            data = row['data']
            #capacity = data[0][0]['Capacity'][0][0]
            capacity = np.nan  # No capacity available in charge cycles

            for j in range(len(data[0][0]['Voltage_measured'][0])):
                voltage_measured = data[0][0]['Voltage_measured'][0][j]
                current_measured = data[0][0]['Current_measured'][0][j]
                temperature_measured = data[0][0]['Temperature_measured'][0][j]
                #current_load = data[0][0]['Current_load'][0][j]
                #voltage_load = data[0][0]['Voltage_load'][0][j]
                time = data[0][0]['Time'][0][j]
                dataset.append([counter + 1, ambient_temperature,
                                voltage_measured, current_measured,
                                temperature_measured, time])
            counter = counter + 1

    return pd.DataFrame(data=dataset,
                        columns=['cycle', 'ambient_temperature',
                                 'voltage_measured',
                                 'current_measured', 'temperature_measured', 'time'])


def calculate_RUL(df):
    eol_cycle = df['cycle'].max()
    df['RUL'] = eol_cycle - df['cycle']
    return df


# Set the path to your folder containing the .mat files
base_path = r"C:\Users\KIIT\Downloads\naza\Mat"

datasets = ["B0005", "B0006", "B0007", "B0018"]
for name in datasets:
    print(f"Processing {name}...")
    file_path = os.path.join(base_path, f"{name}.mat")
    dataset = load_data(file_path, name)
    dataset_with_rul = calculate_RUL(dataset)

    csv_filename = f'{name}_charge.csv'
    dataset_with_rul.to_csv(csv_filename, index=False)
    print(f"Saved {csv_filename}")
