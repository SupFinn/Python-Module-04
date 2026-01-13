#!/usr/bin/python3

def crisis_response():

    """
    Handles archive access crises and prints status updates for each
    scenario using structured exception handling.
    """

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        with open("lost_archive.txt", "r") as file:
            pass
    except FileNotFoundError:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    try:
        with open("classified_vault.txt", "r") as file:
            file.read()
    except PermissionError:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("CRISIS ALERT: Attempting access to 'standard_archive.txt'...")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
