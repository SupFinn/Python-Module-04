#!/usr/bin/python3

if __name__ == "__main__":

    """
    This program reads a storage file and displays its contents.
    It handles missing files safely and ensures the file is properly closed
    after use.
    """

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:

        file = open("ancient_fragment.txt", 'r')
        print(f"Accessing Storage Vault: {file.name}")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        print(file.read())

        file.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
