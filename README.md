# Cognifyz Technologies — Data Analysis Internship

This project contains Python analysis tasks for **Level 1** and **Level 2** of the Cognifyz Technologies Data Analysis internship.

## Project contents

Place these files in the same project folder:

```text
Cognifyz-Data-Analysis/
├── Dataset .csv
├── Cognifyz_Level_1.ipynb
├── Cognifyz_Level_2.ipynb
├── README.md
└── requirements.txt
```

Your notebook filenames may be different; open the notebook files you saved.

## Requirements

- Python 3.9 or newer
- Jupyter Notebook
- The dataset CSV file supplied for the internship

The Python libraries required by the notebooks are listed in `requirements.txt`.

## How to run this project on your computer

### 1. Install Python

Install Python 3.9 or newer from https://www.python.org/downloads/.

On Windows, select **Add Python to PATH** during installation if that option appears.

### 2. Put the files in one folder

Create a folder named `Cognifyz-Data-Analysis` and place the dataset, both notebooks, `README.md`, and `requirements.txt` inside it.

The setup code uses:

```python
df = pd.read_csv("Dataset .csv")
```

The CSV must therefore be named exactly `Dataset .csv` and be in the same folder as the notebook. If your dataset has another filename, update the path in that line.

### 3. Open a terminal in the project folder

**Windows:** Open the folder in File Explorer, click the address bar, type `cmd`, and press Enter.

**macOS/Linux:** Open Terminal and use `cd` to move into the project folder.

### 4. Create and activate a virtual environment (recommended)

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

If `python` is not recognized, try `py` instead.

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install the required libraries

Run this command from the project folder:

```bash
python -m pip install -r requirements.txt
```

On macOS/Linux, use `python3 -m pip install -r requirements.txt` if needed.

### 6. Start Jupyter Notebook

```bash
python -m notebook
```

A browser tab should open. If it does not, copy the local URL shown in the terminal into your browser.

### 7. Run the notebooks

1. Open `Cognifyz_Level_1.ipynb`.
2. Run the setup cell first.
3. Run each task cell from top to bottom using **Run** or **Shift + Enter**.
4. Check that the printed results and charts appear.
5. Repeat for `Cognifyz_Level_2.ipynb`.

Each notebook must run its setup cell so that `df` is loaded before the task code is executed.

## Tasks covered

### Level 1
1. Top Cuisines
2. City Analysis
3. Price Range Distribution
4. Online Delivery

### Level 2
1. Restaurant Ratings
2. Cuisine Combination
3. Geographic Analysis
4. Restaurant Chains

## Troubleshooting

- **FileNotFoundError:** Check that `Dataset .csv` is in the same folder as the notebook and the filename matches exactly.
- **ModuleNotFoundError:** Activate the virtual environment and run `python -m pip install -r requirements.txt`.
- **Charts do not appear:** Run notebook cells in order and confirm the setup cell completed successfully.
- **`df` is not defined:** Run the setup cell before the task cell.
- **Notebook command issue:** Run `python -m notebook` after installing the requirements.

