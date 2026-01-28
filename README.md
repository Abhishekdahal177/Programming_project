# Programming_project
# PyFIM: Python-Based Malware Simulation and File Integrity Detection
**PyFIM** is a cybersecurity tool designed to demonstrate the importance of **Data Integrity** within the CIA Triad. This project simulates a malware attack (Trojan behavior) on a target file and detects unauthorized modifications using **File Integrity Monitoring (FIM)** techniques.

The system utilizes the **SHA-256** cryptographic hash algorithm to generate digital fingerprints of files. By leveraging the **Avalanche Effect**, even the slightest modification by the simulated malware results in a completely different hash, triggering a security alert.

##Features

* **GUI Interface:** A user-friendly Graphical User Interface built with `tkinter` for easy interaction.
* **SHA-256 Hashing:** Implements secure hashing to create unique digital signatures for files.
* **Malware Simulation:** Simulates a file-infecting Trojan that injects a malicious payload into a target file.
* **Integrity Verification:** Compares baseline hashes against current hashes to detect tampering.
* **Real-time Logging:** Displays system activities, hash values, and alerts in a scrollable log window.

##Tech Stack

* **Language:** Python 3.14.2
* **GUI Framework:** Tkinter (Standard Python Library)
* **Hashing Algorithm:** SHA-256 (hashlib)
* **OS Compatibility:** Cross-platform (Developed on Fedora Linux, compatible with Windows/macOS)
