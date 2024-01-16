# Tripwire
creating a tripwire script that can be executed on various directories. By comparing the directory content against a static/pre-existing record, the tripwire script will determine whether files have been added, removed or altered.



## How to run
To run the provided Python script, follow these steps:

1. **Save the Script:**
   Copy the script into a file named `tripwire.py` and save it.

2. **Prepare the Test Directory:**
   In Linux, create a test directory and add at least two different text files with your first and last name inside the content of each file.

3. **Run the Script to Create a Tripwire Record:**
   Open a terminal and navigate to the directory where you saved the `tripwire.py` script and execute the following command:

   ```bash
   python tripwire.py /path/to/your/test_directory tripwireRecord.txt c
   ```

   Replace `/path/to/your/test_directory` with the actual path to your test directory.

   This command will create a tripwire record file (`tripwireRecord.txt`) containing the static information.

4. **Modify, Add, or Remove Files in the Test Directory:**
   Make changes in your test directory such as modifying existing files, adding new files, or removing existing files.

5. **Run the Script to Compare with Tripwire Record:**
   Run the script again to compare the current state of the directory with the tripwire record:

   ```bash
   python tripwire.py /path/to/your/test_directory tripwireRecord.txt
   ```

   This command will print a report to the console specifying the file names that have been modified, missing, or added, following the format you specified earlier.

Make sure to replace `/path/to/your/test_directory` with the actual path to your test directory. Adjustments may be needed based on your system configuration and Python version.
