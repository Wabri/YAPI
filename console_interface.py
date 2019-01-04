

def run(packages):
    """Run the console installer.

    Arguments:
    packages -- list of packages to print
    """
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    from os import getlogin
    import script_runner

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read("config.ini")
    language_config_file = str(config["COMMON"]["language_dir"]).replace(
        "~", "/home/" + getlogin()) + "/" + config["COMMON"]["language"] \
        + ".ini"
    del config
    language_config = ConfigParser()
    language_config.read(language_config_file)
    yes_answer = str(language_config["ANSWER"]["yes_answer"]).split(sep=", ")
    no_answer = str(language_config["ANSWER"]["no_answer"]).split(sep=", ")
    right_answer = yes_answer + no_answer
    continue_to_ask = True
    while continue_to_ask:
        print("-" * 79)
        print(language_config["CONSOLE"]["0_choose_package"])
        for package_counter in packages:
            print("{:>2}) {} - {}".format(
                package_counter,
                packages[package_counter][0].capitalize(),
                packages[package_counter][1]))
        choose = -1
        while choose not in range(package_counter + 1):
            choose = input(language_config["CONSOLE"]
                           ["1_install_question"] + " ")
            try:
                choose = int(choose)
                if choose not in range(package_counter + 1):
                    print(str(language_config["CONSOLE"]["2_end_numers"])
                          .format(package_counter))
            except ValueError:
                if choose == "exit":
                    print("Ok, bye bye!")
                    exit()
                print(str(language_config["CONSOLE"]["3_input_format_error"])
                      .format(package_counter))
                choose = -1
        package_to_install = choose
        while choose not in right_answer:
            choose = input(str(language_config["CONSOLE"]
                               ["4_confirmation_question"] + " ")
                           .format(packages[package_to_install][0]))
        if choose in yes_answer:
            print(language_config["CONSOLE"]["5_installation_start"])
            script_runner.runScript(packages[package_to_install][3])
        else:
            print(language_config["CONSOLE"]["6_reject_installation"])
        choose = ""
        while choose not in right_answer:
            choose = input(language_config["CONSOLE"]
                           ["7_restart_installation"] + " ")
        if choose in yes_answer:
            continue
        else:
            print(language_config["CONSOLE"]["8_end_installation"])
            exit()
    print("-" * 79)
