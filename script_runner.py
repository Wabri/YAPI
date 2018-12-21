
def runScript(path_to_file):
    """Run the script give in argument."""
    import subprocess
    try:
        with open(path_to_file, "r") as file_script:
            bashCommand = ""
            for line in file_script.readlines():
                if line[0] != "#":
                    bashCommand += line
            bashCommand = bashCommand.replace("\n", " ; ")
            output = subprocess.call(
                bashCommand, stderr=subprocess.STDOUT, shell=True)
            return output
    except (OSError, IOError, KeyError):
        return "Package not found. Try again."
