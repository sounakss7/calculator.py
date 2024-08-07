# Desktop Calculator

![Calculator Screenshot](https://raw.githubusercontent.com/xanmoy/calculator-desktop/main/media/Screenshot%20from%202024-08-07%2003-33-56.png)


A simple desktop calculator application built using Python and Tkinter. This application performs basic arithmetic operations and can be compiled into a standalone executable using PyInstaller.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Simple and user-friendly graphical interface.

## Prerequisites

- Python 3.x
- Tkinter (comes bundled with Python)
- PyInstaller (for creating standalone executables)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/xanmoy/calculator-desktop.git
cd calculator-desktop
```

### 2. Set Up a Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

### 3. Install Dependencies
Make sure you have pyinstaller installed:

```bash
pip install pyinstaller
```
## Usage
Running the Application
To run the calculator application directly from source:

```bash
python main.py
```

## Creating a Standalone Executable
To create a standalone executable using PyInstaller:

```bash
pyinstaller --onefile --windowed main.py
```

The executable will be created in the dist directory. You can then run the executable from the command line or double-click it to start the application.

Directory Structure
```graphql
calculator-desktop/
├── build/                  # Intermediate build files (generated by PyInstaller)
├── dist/                   # Generated executable and related files
├── main.py                 # Main Python script
├── main.spec               # PyInstaller spec file (optional)
├── .gitignore              # Git ignore file
├── README.md               # This README file
└── requirements.txt        # Python dependencies (if any)
```
## Contributing
Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## License
This project is licensed under the [MIT License](https://github.com/xanmoy/calculator-desktop/blob/main/LICENCE) - see the LICENSE file for details.

## Acknowledgements
Tkinter: Python's standard GUI library used for building the graphical interface.
PyInstaller: Tool used for packaging Python applications into standalone executables.


### Explanation of Sections

1. **Project Title and Description**: Clearly state the purpose of the project.
2. **Features**: Highlight what the application does.
3. **Prerequisites**: List software and tools required to run and build the project.
4. **Installation**: Instructions for setting up the project environment and installing dependencies.
5. **Usage**: How to run the application and create an executable.
6. **Directory Structure**: Explain the directory layout.
7. **Contributing**: Guidelines for contributing to the project.
8. **License**: Licensing information.
9. **Acknowledgements**: Credit any libraries or tools used in the project.
