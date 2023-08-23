# Delayed Shutdown Script

The **Delayed Shutdown Script** is a Python script that enables you to set a delay time and subsequently perform an automated system shutdown once the designated delay has elapsed. This can prove valuable if you wish to schedule your computer for an automatic shutdown after a specific duration.

## How It Operates

The script initiates a user input prompt to acquire a delay time in the format `X.Yz`, where:
- `X` represents the integer portion of the time.
- `Y` represents the decimal portion of the time.
- `z` represents the time unit, which can take the form of seconds (`s`), minutes (`m`), hours (`h`), days (`d`), or weeks (`w`).

As an example, entering `30s` would yield a 30-second delay, while inputting `1.5h` would result in a delay of 1 hour and 30 minutes.

The script subsequently converts the input delay time into seconds and then employs the `sleep` function to halt execution for the specified duration. Once the delay concludes, it issues a system shutdown command using the `rundll32.exe` utility.

## Usage

1. Execute the script via the command `python delayed_shutdown.py`.
2. The script will prompt you to input a delay time. Provide the delay time in the aforementioned format.
3. Following the designated delay, the script will initiate a system shutdown.
