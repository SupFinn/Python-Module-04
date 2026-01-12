#!/usr/bin/python3

def archive_creation():

    """
    This program creates a new archival storage file and inscribes
    critical preservation entries. It ensures data is written
    correctly and displays the stored information.
    """

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
 
    try:
        file = open("new_discovery.txt", "w")
        print(f"Initializing new storage unit: {file.name}")
        print("Storage unit created successfully...\n")

        file.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
        file.write("{[}ENTRY 002{]} Efficiency increased by 347%\n")
        file.write("{[}ENTRY 003{]} Archived by Data Archivist trainee\n")
        file.close()
    except PermissionError:
        print("ERROR: You do not have the permissions to write in this file.")

    try:
        print("Inscribing preservation data...")
        file = open("new_discovery.txt", "r")
        print(file.read())

        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file.name}' ready for long-term preservation.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    archive_creation()