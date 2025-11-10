# Falling Sand Simulation
Falling sand simulation made with python using pygame
![Project Demo](https://raw.githubusercontent.com/yashwanth2706/fallingsand-simulation/main/demo/FallingSandSimulationDemo.gif)
## Requirements & Setup

### Prerequisites
- Python 3.8+ installed (use python or python3 depending on your system).
- Git (optional) and a terminal/PowerShell.

Project dependencies are listed in requirements.txt
Use a virtual environment to avoid conflicts

### Create a virtual environment

Unix / macOS
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows (PowerShell)
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows (Command Prompt)
```
python -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

To deactivate the virtual environment:
```
deactivate
```

### Run the game
From the repository root (with the venv activated), run the main entry script. Replace `main.py` with the actual launcher file if different:
```
python main.py
```
On macOS/Linux, if your system uses `python3`, you can run:
```
python3 main.py
```

### Without a virtual environment
You can also install dependencies system-wide (not recommended):
```
pip install -r requirements.txt
python main.py
```

### Create or update requirements.txt
After installing or updating packages in your virtual environment:
```
pip freeze > requirements.txt
```

### Notes & Troubleshooting
- Ensure you run commands from the project root where requirements.txt and the main script live.
- If pygame installation fails on macOS, ensure you have relevant SDL libraries (install via Homebrew) or consult pygame installation docs.
- If `python` points to Python 2 on your system, use `python3` instead.
