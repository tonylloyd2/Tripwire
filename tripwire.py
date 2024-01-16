import os
import sys
import hashlib

def calculate_hash(file_path):
    """Calculate the hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def create_tripwire_record(directory, record_file):
    """Create a tripwire record for the specified directory."""
    with open(record_file, "w") as record:
        record.write(directory + "\n")
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_hash = calculate_hash(file_path)
                record.write(f"\t{filename} {file_hash}\n")

def compare_tripwire_record(directory, record_file):
    """Compare the current state of the directory with the tripwire record."""
    modified = []
    added = []
    removed = []

    with open(record_file, "r") as record:
        record_directory = record.readline().strip()
        if record_directory != directory:
            print("Error: Directory mismatch in the record file.")
            return

        record_entries = {line.split()[0]: line.split()[1] for line in record.readlines()}

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_hash = calculate_hash(file_path)
            if filename in record_entries:
                if file_hash != record_entries[filename]:
                    modified.append(filename)
            else:
                added.append(filename)

    removed = [filename for filename in record_entries if filename not in os.listdir(directory)]

    print(f"\nDirectory: {directory}")
    print("Modified:", "|".join(modified))
    print("Removed:", "|".join(removed))
    print("Added:", "|".join(added))

if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[3] == "c":
        create_tripwire_record(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 3:
        compare_tripwire_record(sys.argv[1], sys.argv[2])
    else:
        print("Usage:")
        print("For creating tripwire record: python tripwire.py tripwireDir tripwireRecord c")
        print("For comparing with tripwire record: python tripwire.py tripwireDir tripwireRecord")
