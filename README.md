# Advanced Keylogger

This is an advanced keylogger written in Python using the `pynput` library. It records keystrokes and stores them in both JSON and text file formats. It can optionally send the recorded data remotely to a specified server.

## Features

- Records keystrokes and captures key press events.
- Supports handling special keys such as Enter, Tab, Space, Backspace, Shift, Ctrl, and Esc.
- Stores the captured keystrokes in JSON and text file formats.
- Optionally sends the recorded data remotely to a server using HTTP POST requests.

## Dependencies

The following dependencies are required to run the keylogger:

- `pynput`: Used for monitoring and capturing keyboard events.
- `json`: Used for serializing/deserializing data to/from JSON format.
- `requests`: Used for sending HTTP POST requests (required only for remote data transmission).

## Usage

1. Install the required dependencies by running the following command:

   ```
   pip install pynput requests
   ```

2. Update the desired configuration parameters in the code:

   - Modify the `ip_address` and `port_number` variables if you want to send the recorded data remotely to a server.
   - Adjust the `time_interval` variable to specify the interval between each data transmission (in seconds).

3. Run the script using the following command:

   ```
   python keylogger.py
   ```

4. The keylogger will start capturing keystrokes. Press the Escape key (`Esc`) to stop the keylogger.

5. The captured keystrokes will be stored in the `adv_logs.json` file (in JSON format) and the `adv_log.txt` file (in plain text format).

6. If you have enabled remote data transmission, the keylogger will send the recorded data to the specified server at regular intervals.

## Important Note

**Please use this keylogger responsibly and in compliance with applicable laws and regulations. Ensure that you have proper authorization before using it on any device. Respect the privacy and legal rights of others.**

---

Feel free to customize the README file further based on your requirements and include any additional information or instructions that may be relevant.
