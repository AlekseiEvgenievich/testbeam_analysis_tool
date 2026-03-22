# Zirettino Data Viewer

GUI tool for converting, loading, inspecting, and plotting detector data for the **Zirettino** project.

This application provides a simple desktop interface for:
- converting decoded binary data into CSV
- loading CSV files for **HG** and **LG** channels
- previewing tabular detector data
- plotting histograms for different detector subsystems:
  - **Calo**
  - **ACS / ACD**
  - **PST**

The program is implemented in **Python** using:
- `tkinter` for the GUI
- `pandas` for data handling
- `matplotlib` for plotting
- `numpy` for numerical operations

---

## Overview

This repository contains a lightweight visualization and inspection tool designed for detector studies in the **Zirettino** project.

The application supports:
1. reading decoded detector data from CSV
2. selecting either **high gain** (`_HG`) or **low gain** (`_LG`) channel data
3. renaming raw ASIC channel names into detector-readable labels
4. filtering columns and removing unused DAQ/ASIC branches
5. visualizing detector response through histogram windows

The GUI is intended for quick checks of detector channels and for exploratory analysis of the acquired data.

---

## Main Features

### 1. Binary-to-CSV conversion
The application can call the `DataHandler` class from `decoder.py` to:
- open raw data from the `./data` directory
- decode it
- save the decoded output as CSV

This is triggered in the GUI by the button:

- **Change bin into CSV**

---

### 2. CSV loading for HG and LG
The application allows the user to open a CSV file and process it in one of two modes:

- **Open CSV for _HG**
- **Open CSV for _LG**

Depending on the selected mode:
- the relevant columns are extracted
- DAQ2 columns are removed
- `DAQ1_` prefixes are stripped
- channel names are remapped to detector labels
- unsupported ASIC groups are dropped

---

### 3. Automatic detector channel mapping
Raw trigger channel names are converted into human-readable detector channel names.

Examples:
- `A_TRIG(...)`, `B_TRIG(...)`, `C_TRIG(...)`  
  are translated into:
- `Asic0_CHx_HG`, `Asic1_CHx_HG`, etc.

Then these columns are renamed into physical detector labels such as:
- `pst_...`
- `acs_...`
- `calog_...`

This makes the data easier to inspect and plot.

---

### 4. Data preview in GUI
After loading a CSV file:
- the processed table is displayed inside a `Treeview`
- up to the first 100 columns are shown
- horizontal and vertical scrollbars are enabled

This allows quick inspection of event values without writing additional scripts.

---

### 5. Histogram plotting
The application includes dedicated plotting functions for different detector subsystems.

#### Calo Graph
Plots histograms for calorimeter channels:
- channels containing `calo`
- separate windows are created automatically
- logarithmic Y scale is used

#### ACS Graph
Plots histograms for anti-coincidence channels:
- channels containing `acs`
- grouped in windows
- logarithmic Y scale is used

#### PST Graph
Plots histograms for PST channels:
- channels containing `pst`
- grouped logically by detector block
- overlay style is used for comparing related channels
- color coding depends on HG / LG mode

---

## Project Structure

```text
.
├── lg.py                # Main GUI application
├── decoder.py           # Data decoding / DataHandler logic
├── middle.csv           # Example CSV file for testing
└── README.md
