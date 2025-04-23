# File Integrity Monitoring System

A Python-based file integrity monitoring system that checks for changes, deletions, and new files in specified directories, comparing the current state with a baseline hash. It supports logging and easy baseline creation.

## Features

- **Baseline Creation**: Generate and store hash values of all files in monitored directories.
- **Change Detection**: Detect modifications, deletions, and new files based on file hash comparisons.
- **Logging**: All changes are logged in logs/changes.log and backed up with timestamps.
- **Backup Logs**: Automatically back up old logs before new scans.
- **File Hashing**: Uses SHA-256 for file integrity checking.

## Installation

### 1. Clone the repository:

- git clone https://github.com/sptemp-gpu/file-integrity-monitor.git


### 2. Install dependencies:

Make sure you have Python 3.x installed. You can install the required libraries using pip:

- pip install -r requirements.txt


### 3. Configure paths to monitor:

- Add paths to the config/paths_to_monitor.txt file (one path per line).

### 4. Run the system:

#### First, create a baseline:

- python main.py


#### To scan for file changes:

- python main.py


## Files

- main.py: Main script for creating baselines and checking for file changes.
- config/paths_to_monitor.txt: List of directories/files to monitor.
- logs/changes.log: Log file for file changes.
- db/baseline_hashes.json: Stored baseline hashes for comparison.

## Contributing

- Fork the repository.
- Create a new branch (git checkout -b feature-name).
- Commit your changes (git commit -am 'Add feature').
- Push to the branch (git push origin feature-name).
- Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Uses SHA-256 for file hashing (via hashlib).
- Inspired by various file integrity monitoring systems in cybersecurity.
  
