# SATE OF HEALTH BATTERY PREDICTION USING NASA DATASETS

# NASA Battery Dataset Preprocessing: Charge & Discharge + RUL

This repository contains two Python scripts that extract and process charge and discharge cycle data from the **NASA Battery Aging Dataset**. It prepares the data for machine learning tasks such as State of Health (SOH) prediction and Remaining Useful Life (RUL) estimation.

---

# Repository Contents

- `matocsvcharge.py` – Extracts **charge cycles** and computes RUL.
- `matocsvdischarge.py` – Extracts **discharge cycles** with capacity, load data, and RUL.
- Output: `.csv` files for each battery (`B0005`, `B0006`, `B0007`, `B0018`).

---

# Output Files

For each `.mat` file, the scripts generate:
```
B0005_charge.csv
B0005_discharge.csv
B0006_charge.csv
...
```

Each CSV contains time-series data per cycle, including:

## Charge File Columns:
- `cycle`
- `ambient_temperature`
- `voltage_measured`
- `current_measured`
- `temperature_measured`
- `time`
- `RUL`

## Discharge File Columns:
- `cycle`
- `ambient_temperature`
- `capacity`
- `voltage_measured`
- `current_measured`
- `temperature_measured`
- `current_load`
- `voltage_load`
- `time`
- `RUL`

---

# Requirements

- Python 3.7+
- `scipy`
- `numpy`
- `pandas`
- `.mat` files from the NASA Battery Dataset

Install required packages:
```bash
pip install numpy pandas scipy
```

---

# Usage

1. **Place your `.mat` files** in this folder:
   ```
   C:/Users/KIIT/Downloads/naza/Mat
   ```

2. **Run the scripts**:
   ```bash
   python matocsvcharge.py
   python matocsvdischarge.py
   ```

---

# Dataset Source

NASA Ames Prognostics Data Repository:  
[https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository](https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository)

---

## 👤 Author

**Keyradin Ayub Wariyo**  
Erasmus Mundus Scholar – Electric Propulsion and Control  
[GitHub Profile](https://github.com/Keyradin)

---

## License

MIT License (you can edit this based on your preference)
