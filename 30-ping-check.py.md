# Server Availability Checker

A simple Python network-monitoring script that checks multiple IP addresses and hostnames and reports whether they are **UP** or **DOWN**.

## Features

* Checks multiple servers automatically
* Supports IP addresses and hostnames
* Sends 2 ping requests to each server
* Uses Python's `subprocess` module
* Displays clear server availability status

## Requirements

* Python 3
* Linux system with the `ping` command

Check Python:

```bash
python3 --version
```

## Code

```python
import subprocess

servers = [
    "192.168.1.18",
    "192.16.1.98",
    "google.com",
    "yahoo.com",
    "192.168.1.10"
]
print("Starting the script to check all servers")

for server in servers:
    result = subprocess.run(
        ["ping", "-c", "2", server],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{server} is UP!")
    else:
        print(f"{server} is DOWN!!!")
```

## Run

```bash
python3 30-ping-check.py
```

## Example Output

```text
Starting the script to check all servers

192.168.1.1 is UP!
192.168.1.13 is DOWN!!!
google.com is UP!
yahoo.com is UP!
192.168.1.201 is DOWN!!!
10.0.0.1 is DOWN!!!
```

## Screenshots

### 1. Code

**Add a screenshot of the Python code here.**

```markdown

```

### 2. Execution

**Add a screenshot of the script running in the terminal here.**

```markdown
![Execution](screenshots/execution.png)
```

### 3. Results

**Add a screenshot showing the UP/DOWN server results here.**

```markdown
![Results](screenshots/results.png)
```

## Project Structure

```text
Python_basics/
├── 30-ping-check.py
├── README.md
└── screenshots/
    ├── code.png
    ├── execution.png
    └── results.png
```

## Note

**UP** means the host responded successfully to the ping request.
**DOWN** means the ping request failed. A host may still be running while blocking ICMP/ping traffic.

## Author

**Sumaid**
