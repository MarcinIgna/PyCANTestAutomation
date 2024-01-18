# PyCANalyze

PyCANalyze is a Python-based project for CAN testing and automation, designed for analyzing and simulating Controller Area Network (CAN) messages in automotive systems.

## Installation

1. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Setting up Virtual CAN (vcan)

Run the `setup_vcan.sh` script to create a virtual CAN interface (`vcan0`):
   ```bash
   ./setup_vcan.sh
   ```

## Running the Project

### Sending CAN Messages (Optional)

Execute the main script (`main.py`) to send CAN messages:
   ```bash
   python3 main.py
   ```

### Simulating Automotive Scenarios

Run the automotive simulation script (`automotive_simulation.py`) to generate CAN messages:
   ```bash
   python3 automotive_simulation.py
   ```

### Verifying Message Reception

Run the test automation script (`test_automation.py`) to verify message reception:
   ```bash
   python3 test_automation.py
   ```

Adjust configurations in the scripts as needed for your testing scenarios.

Feel free to explore and contribute to the project!
