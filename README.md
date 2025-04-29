# ConsoleUtilityApp

A Python console application offering user management, system tools, port scanning, NFC data interaction, and fun commands. It supports admin mode for creating/deleting users and viewing the user list.

## Features

- **User Management**: 
  - Create and delete users (admin only)
  - View user list (admin only)
  
- **System Utilities**:
  - `ping`: Ping a host or IP address.
  - `sysinfo`: Retrieve detailed system information.
  - `time`: Display the current system time.
  - `clear`: Clear the console screen.
  
- **Network Tools**:
  - `portscan`: Scan open ports on a specified host.
  
- **NFC Interaction**:
  - `nfc`: Read and write NFC data.
  - `clear_nfc`: Clear NFC data.

- **Fun Commands**:
  - `bomb`: Trigger a fun 'bomb' action.
  - `echo`: Output a message to the console.
  - `spam`: Spam the terminal with repetitive messages.
  - `timer`: Start a timer countdown.

- **Developer Tools**:
  - `devlog`: Display developer logs.
  - `link`: Open a specified URL.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Vrexizzek/ConsoleUtilityApp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ConsoleUtilityApp
   ```

3. Install the required Python libraries (if necessary):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. You will be prompted for a login. Use the login credentials you have created.

3. After logging in, use the available commands:
   - Type `help` for a list of available commands.
   - Type `exit` to close the program.

### Commands

- **Admin Only**:
  - `create-user`: Create a new user account.
  - `delete-user`: Delete an existing user account.
  - `users`: Display a list of all users.

- **General Commands**:
  - `clear` or `cls`: Clear the console screen.
  - `ping`: Ping a host/IP.
  - `portscan`: Perform a port scan on a specified host.
  - `sysinfo`: Display system information.
  - `nfc`: Read and write NFC data.
  - `timer`: Start a timer.
  - `bomb`, `echo`, `spam`: Fun commands.

## Requirements

- Python 3.x
- `getpass` (for secure password input)
- `socket` (for network utilities)
- `datetime` (for time and date functionality)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
