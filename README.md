# Simple Linux Terminal AI Wrapper

The goal of this project is to integrate a simple AI wrapper to help the user better understand the outputs it receive from the terminal invoked by the user. The output and input in the terminal is logged automatically after running `./shell_logging.sh` and is saved in a personal `log` directory inside the host (`/home/{hostname}`directory. 

To run the AI (DeepSeek version 3.2) and ask question(s) pertain to the log content, it uses a custom shell command. In my case, it's `AIag`. For more details about arguments, please go to ....   The command calls the `AIag.sh` script. Within the script, it than calls the python script which will call the AI model using a API key and than reading the log content and return it's content upon successful exacution. 

<hr>

## Setup Instruction:

### 1. Clone Repository

- ```bash
  git clone https://github.com/ProximaSF/Simple-Linux-Shell-AI-Wrapper
  ```

- Create .env file inside the cloned repository and add these variable

  ```sh
  AWS_BEARER_TOKEN_BEDROCK = ...
  LOG_FILE = ...
  ```

  - **AWS_BEARER_TOKEN_BEDROCK**: AWS Bedrock API key

  - **LOG_FILE**: File path to `logging.log` for AI to read

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

### 3. Install Dependencies

- Using the active .venv working directory to install required packages:

  ```bash
  pip install -r requirements.txt
  ```

### 4. Create logs and bin folder

- In host directory (`/home/{hostname}`) create two folders:

  ```bash 
  mkdir logs
  mkdir bin
  ```

### 5. Create `logging.sh` and `AIag` inside bin

- In `/home/{hostname}/bin` directory:

  ```bash
  nano logging.sh
  ```

- Copy script in clone repository (`"bash scripts/logging.sh"`) and past it to the editor. Save (ctrl+o) and exit to create the file (ctrl+x)

- Allow the new script to run in terminal:

  ```bash
  chmod +x logging.sh 
  ```
  
- <u>Repeat the same process for `AIag`</u>
  - Make sure the two file paths at the bottom of the script points to the right direction. 
    - The first path points to the `.venv` python interpreter
    - Second path point to the python script (should be in the same working directory of the clone repository)

### 6. Add scripts to SYSTEM PATH

- Inside of `nano ~./bashrc` add these two lines at the very bottom:

  ```sh
  export PATH="$PATH:/home/{hostname}/bin/logging.sh"
  export PATH="$PATH:/home/{hostname}/bin/AIag"
  ```

### 7. Finally Reset system (Might be Optional)

<hr>

## How to Use:

1. Start logging.sh script by `logging.sh` in terminal

2. Enter commands

   - All input and output will be recorded in `/logs/recorded_session.log`
   - The content will be the exact clone of the input, thus there will be bash ANSI escape sequences and terminal control characters.
   - Use `cat` command to read content in proper format

3. Type `exit` to stop script (optional)

4. Ask AI what are in the context

   ```bash
   AIag "What is this file?"
   ```

### Bash Script Arguments:

- Prompt: a *required* argument to ask AI a question based on the context it can see
- Token: *optional* argument to determine how many token will be used for the output. 
- Verbose: *optional* argument to echo other argument inputs

## Side Notes:

- While logging.sh is running, running commands like `clear` should not reset/clear the `recorded_session.log` 
- The python script is configured for DeepSeek v3.2.
  - Make sure the model variable is set for DeepSeek v3.2

<hr>

## Possible Future Improvement

- Allow different models
- Provide additional file
- Default chat mode (without using file)