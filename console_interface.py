

def run(packages):
    """Run the console installer ."""
    import script_runner

    yes_answer = ("Y", "Yes", "y", "yes")
    no_answer = ("N", "No", "n", "no")
    right_answer = yes_answer + no_answer
    continue_to_ask = True
    while continue_to_ask:
        print("-" * 79)
        print("You can choose to install this packages:")
        for package_counter in packages:
            print("{:>2}) {} - {}".format(
                package_counter,
                packages[package_counter][0].capitalize(),
                packages[package_counter][1]))
        choose = -1
        while choose not in range(package_counter + 1):
            choose = input(
                "What package do you want to install? (type exit to exit) > ")
            try:
                choose = int(choose)
                if choose not in range(package_counter + 1):
                    print("The package number must be between " +
                          " 0 and {}".format(package_counter))
            except ValueError:
                if choose == "exit":
                    print("Ok, bye bye!")
                    exit()
                print("Please insert a number between 0 and {} > ".format(
                    package_counter))
                choose = -1
        package_to_install = choose
        while choose not in right_answer:
            choose = input("Do you want to install {}? > ".format(
                packages[package_to_install][0]))
        if choose in yes_answer:
            print("Let's start the installation, these take a moment...")
            script_runner.runScript(packages[package_to_install][3])
        else:
            print("Ok, no problem...")
        choose = ""
        while choose not in right_answer:
            choose = input("Do you want to install something else? ")
        if choose in yes_answer:
            continue
        else:
            print("Ok, bye bye!")
            exit()
    print("-" * 79)
