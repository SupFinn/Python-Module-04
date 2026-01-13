#!/usr/bin/python3

def secure_vault():

    """
    Simulates secure vault operations in the Cyber Archives.

    Extracts classified data and archives new security protocols,
    ensuring automatic vault sealing using the with statement.
    """

    print(" === CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        print("Initiating secure vault access...")

        with open("classified_data.txt", "r") as file1:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file1.read())
    except FileNotFoundError:
        print(
            "ERROR: classified_data.txt not found. Run data generator first."
            )

    try:
        with open("security_protocols.txt", "r") as file2:
            print("\nSECURE PRESERVATION:")
            print(file2.read())
            print("Vault automatically sealed upon completion\n")

        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print(
            "ERROR: security_protocols.txt not "
            "found. Run data generator first."
            )


if __name__ == "__main__":
    secure_vault()
