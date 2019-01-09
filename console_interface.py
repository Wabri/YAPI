

def run(packages):
    """Run the console installer.

    Arguments:
    packages -- list of packages to print
    """
    from language_pack_manager import get_language_pack
    import script_runner
    language_pack = get_language_pack()
    yes_answer = language_pack["ANSWER"]["yes_answer"]
    no_answer = language_pack["ANSWER"]["yes_answer"]
    right_answer = yes_answer + no_answer
    continue_to_ask = True
    while continue_to_ask:
        print("-" * 79)
        print(language_pack["CONSOLE"]["0_choose_package"])
        for package_counter in packages:
            print("{:>2}) {} - {}".format(
                package_counter,
                packages[package_counter][0].capitalize(),
                packages[package_counter][1]))
        choose = -1
        while choose not in range(package_counter + 1):
            choose = input(language_pack["CONSOLE"]
                           ["1_install_question"] + " ")
            try:
                choose = int(choose)
                if choose not in range(package_counter + 1):
                    print(str(language_pack["CONSOLE"]["2_end_numers"])
                          .format(package_counter))
            except ValueError:
                if choose == "exit":
                    print(language_pack["CONSOLE"]["8_end_installation"])
                    exit()
                print(str(language_pack["CONSOLE"]["3_input_format_error"])
                      .format(package_counter))
                choose = -1
        package_to_install = choose
        while str(choose) not in right_answer:
            choose = input(str(language_pack["CONSOLE"]
                               ["4_confirmation_question"] + " ")
                           .format(packages[package_to_install][0]))
        if choose in yes_answer:
            print(language_pack["CONSOLE"]["5_installation_start"])
            print(script_runner.runScript(packages[package_to_install][3]))
        else:
            print(language_pack["CONSOLE"]["6_reject_installation"])
        choose = ""
        while choose not in right_answer:
            choose = input(language_pack["CONSOLE"]
                           ["7_restart_installation"] + " ")
        if choose in yes_answer:
            continue
        else:
            print(language_pack["CONSOLE"]["8_end_installation"])
            exit()
    print("-" * 79)
