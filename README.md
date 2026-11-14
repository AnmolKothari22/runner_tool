# **A CPP tool to run , test and debug competative coding problems**
    this utility tool is used to run codeforces style problems .
    please take care about the blank line rules in subsequent text

## Requirements

    1: Linux/WSL
    2: python


## Installation steps

#### 1. Clone the repo
    git clone https://github.com/AnmolKothari22/runner_tool && cd runner_tool

#### 2. Copy runner to binaries
    sudo cp runner /usr/local/bin/

#### 3. Copy runner_tool to binaries
    sudo cp runner_tool /usr/local/bin/

#### 4. Make runner executable
    sudo chmod +x /usr/local/bin/runner

#### 5. Verify installation
    ls -l /usr/local/bin/runner
    ls -ld /usr/local/bin/runner_tool

    
## Running process
    1: open /usr/local/bin/runner_tool/input.txt for inputting test cases
    2: open /usr/local/bin/runner_tool/expected_output.txt for expected outputs
    3: keep only **ONE** line empty in between testcases and expected output both 
    3: command to run :
```bash
    runner {PATH of cpp file}
```


