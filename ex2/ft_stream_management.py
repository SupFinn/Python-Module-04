#!/usr/bin/python3

import sys

if __name__ == "__main__":

    """
    Simulates the Cyber Archives communication system.

    Collects archivist ID and status, then sends standard messages
    to stdout and alerts to stderr, demonstrating proper stream usage.
    """

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    sys.stdout.write(
        "\n{[}STANDARD{]} Archive status from "
        f"{archivist_id}: {status_report}\n"
        )
    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: Communication "
        "channels verified\n"
        )
    sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")
    print("\nThree-channel communication test successful.")
