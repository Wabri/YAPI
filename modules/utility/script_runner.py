
def runScript(path_to_file):
    """Run the script give in argument.

    Arguments:
    path_to_file -- the path to the script to run
    """
    from modules.languages.language_pack_manager import get_language_pack
    import subprocess
    language_pack = get_language_pack()
    try:
        with open(path_to_file, "r") as file_script:
            bashCommand = ""
            for line in file_script.readlines():
                if line[0] != "#":
                    bashCommand += line
            bashCommand = bashCommand.replace("\n", " ; ")
            output = subprocess.call(
                bashCommand, stderr=subprocess.STDOUT, shell=True)
            if output == 0:
                return language_pack["SCRIPT-RUNNER"]["1_package_intalled"]
            else:
                return language_pack["SCRIPT-RUNNER"]["2_package_error"]
    except (OSError, IOError, KeyError):
        return language_pack["SCRIPT-RUNNER"]["0_package_not_found_error"]
