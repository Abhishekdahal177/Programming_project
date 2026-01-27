# detector.py
from hasher import generate_file_hash

def detect_tampering(original_file, infected_file):
    """
    Compares the hashes of two files to detect modification.
    """
    print("\n--- Initiating Integrity Scan ---")
    
    # 1. Get baseline hash (The "Known Good" state)
    original_hash = generate_file_hash(original_file)
    if not original_hash:
        print(f"[X] Error: Original file not found at {original_file}")
        return
        
    # 2. Get current hash (The "Suspicious" state)
    infected_hash = generate_file_hash(infected_file)
    if not infected_hash:
        print(f"[X] Error: Infected file not found at {infected_file}")
        return

    print(f"Baseline Hash: {original_hash}")
    print(f"Current Hash:  {infected_hash}")

    # 3. Compare
    if original_hash == infected_hash:
        print("[OK] Integrity Verified: No changes detected.")
    else:
        print("[!!!] ALERT: INTEGRITY COMPROMISED [!!!]")
        print("The file hash does not match the baseline. Unauthorized modification detected.")
