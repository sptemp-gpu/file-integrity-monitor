import os
import json
from utils.hashing import calculate_file_hash
from utils.logger import log_change

BASELINE_PATH = "db/baseline_hashes.json"

def load_paths():
    paths = []
    with open("config/paths_to_monitor.txt", "r") as f:
        for line in f:
            path = line.strip()
            if os.path.exists(path):
                if os.path.isfile(path):
                    paths.append(path)
                elif os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            full_path = os.path.join(root, file)
                            paths.append(full_path)
    return paths
def create_baseline(paths):
    baseline = {}
    for file_path in paths:
        file_hash = calculate_file_hash(file_path)
        if file_hash:
            baseline[file_path] = file_hash
    with open(BASELINE_PATH, "w") as f:
        json.dump(baseline, f, indent=4)
    print("[+] Baseline created.")

def check_for_changes(paths):
    try:
        with open(BASELINE_PATH, "r") as f:
            content = f.read().strip()
            if not content:  # If the file is empty
                print("[!] Baseline file is empty. Please create a baseline first.")
                return
            baseline = json.loads(content)
    except FileNotFoundError:
        print("[!] Baseline not found. Run baseline creation first.")
        return
    except json.JSONDecodeError:
        print("[!] Error in reading baseline. Check file for corrupt or invalid JSON.")
        return

    current_state = {}
    for file_path in paths:
        file_hash = calculate_file_hash(file_path)
        if file_hash:
            current_state[file_path] = file_hash

    # Test logging by manually logging a message
    log_change("Test Log", "test_file.txt")

    # Detect Modified & Deleted files
    for file_path, old_hash in baseline.items():
        if file_path not in current_state:
            log_change("File Deleted", file_path)
        elif current_state[file_path] != old_hash:
            log_change("File Modified", file_path)

    # Detect New files
    for file_path in current_state:
        if file_path not in baseline:
            log_change("New File Detected", file_path)

    print("[+] Change scan complete. Check logs/changes.log for details.")




if __name__ == "__main__":
    paths = load_paths()
    
    # Uncomment this once to create baseline
    create_baseline(paths)
    
    # Check for file changes
    check_for_changes(paths)

