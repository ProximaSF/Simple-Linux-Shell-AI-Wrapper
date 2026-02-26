# Simple Linux Terminal AI Wrapper

The goal of this project is to integrate a simple AI wrapper to help the user better understand the outputs it receive fro the terminal invoked by the user. The output and input in the terminal is logged automatically after running `./shell_logging.sh` and is saved in a personal `log` directory inside the host (`/home/{hostname}`directory. 

To run the AI (DeepSeek version 3.2) and ask question(s) pertain to the log content, it uses a custom shell command. In my case, it's `AIag`. For more details about arguments, please go to ....   The command calls the `AIag.sh` script. Within the script, it than calls the python script which will call the AI model using a API key and than reading the log content and return it's content upon successful exacution. 

## Setup Instruction:

## 1. Clone Repository

- ```bash
  git clone https://github.com/ProximaSF/Simple-Linux-Shell-AI-Wrapper
  ```

### 2. Setup virtual environment (.venv)

- In a empty directory terminal, past:

  ```bash
  python -m venv .venv
  ```

- Activate .venv

  ```bash
  source ".venv/bin/activate"
  ```

  - To deactivate, simply type `deactivate`

## 3. Install Dependencies

- Using the active venv working directory install required pip packages:

  ```bash
  pip install -r requirements.txt
  ```

## 4. Create logs and bin folder

- In host directory (`/home/{hostname}`) create two folders:

  ```bash 
  mkdir logs
  mkdir bin
  ```

## 5. Create `shell_logging.sh`

- In `/home/{hostname}` directory:

  ```bash
  nano shell_logging.sh
  ```

- Copy script in clone repository (`"bash scripts/shell_logging.sh"`) and past it to the editor. Save (ctrl+o) and exit to create the file (ctrl+x)

- Allow the new script to run in terminal:

  ```bash
  ```

  