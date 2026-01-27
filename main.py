import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import malware
import detector
import hasher

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGINAL_FILE = os.path.join(BASE_DIR, "labs", "original", "important.txt")
INFECTED_FILE = os.path.join(BASE_DIR, "labs", "infected", "important.txt")

class IntegrityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyFIM: Malware Simulation & Detection")
        self.root.geometry("600x500")

        # Title Label
        tk.Label(root, text="File Integrity Monitor Lab", font=("Arial", 16, "bold")).pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="1. Setup Lab Environment", command=self.setup, width=25, bg="#e1e1e1").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="2. Run Malware Attack", command=self.run_attack, width=25, bg="#ffcccb").grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="3. Verify Integrity", command=self.run_detection, width=52, bg="#ccffcc").grid(row=1, column=0, columnspan=2, pady=5)

        # Output Log (This replaces the terminal)
        tk.Label(root, text="Activity Log:").pack(anchor="w", padx=20)
        self.log_area = scrolledtext.ScrolledText(root, width=70, height=15)
        self.log_area.pack(padx=20, pady=5)

    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def setup(self):
        os.makedirs(os.path.dirname(ORIGINAL_FILE), exist_ok=True)
        with open(ORIGINAL_FILE, "w") as f:
            f.write("I'm a cybersecurity expert")
        self.log(f"[+] Setup: Created clean file at {ORIGINAL_FILE}")
        messagebox.showinfo("Success", "Lab Environment Ready!")

    def run_attack(self):
        if not os.path.exists(ORIGINAL_FILE):
            messagebox.showerror("Error", "Please run Setup first!")
            return
        malware.simulate_malware_attack(ORIGINAL_FILE, INFECTED_FILE)
        self.log("[!] Attack: Malware has modified the file.")
        messagebox.showwarning("Alert", "Malware Attack Simulated!")

    def run_detection(self):
        if not os.path.exists(INFECTED_FILE):
            messagebox.showerror("Error", "No infected file found to scan!")
            return
        
        # Get hashes
        orig_hash = hasher.generate_file_hash(ORIGINAL_FILE)
        inf_hash = hasher.generate_file_hash(INFECTED_FILE)
        
        self.log(f"\n--- Integrity Scan ---")
        self.log(f"Baseline: {orig_hash}")
        self.log(f"Current:  {inf_hash}")

        if orig_hash == inf_hash:
            self.log("[OK] No tampering detected.")
            messagebox.showinfo("Result", "Integrity Verified: Safe")
        else:
            self.log("[!!!] ALERT: HASH MISMATCH DETECTED!")
            messagebox.showerror("Security Alert", "INTEGRITY COMPROMISED!")

if __name__ == "__main__":
    root = tk.Tk()
    app = IntegrityApp(root)
    root.mainloop()
