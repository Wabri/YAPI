# YAPI - Yet Another Package Installer

import cache_manager
import script_runner
import subprocess  # Run Bash Commands
import sys  # Make System Calls

# File Locations
where_is_scripts = "scripts/"
# Response and run Options
yes_answer = ("Y", "Yes", "y", "yes")
no_answer = ("N", "No", "n", "no")
right_answer = yes_answer + no_answer
options = {
    "install": ["<package_to_install>", "Install one of the packages"],
    "console": ["no", "Run Yapi with the terminal question installer"],
    "update": ["no", "Pull the newest YAPI version from github"],
    "cache": ["no", "Recreate the cache"]
}


def consoleInstall():
    """Console installer."""
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
            choose = input("What package do you want to install? ")
            try:
                choose = int(choose)
                if choose not in range(package_counter + 1):
                    print("The package number must be between " +
                          " 0 and {}".format(package_counter))
            except ValueError:
                if choose == "exit":
                    print("Ok, bye bye!")
                    exit()
                print("Please insert a number between 0 and {}".format(
                    package_counter))
                choose = -1
        package_to_install = choose
        while choose not in right_answer:
            choose = input(
                "Do you want to install {}? ".format(
                    packages[package_to_install][0]))
        if choose in yes_answer:
            print("Let's start the installation, these take a moment...")
            with open(packages[package_to_install][3], "r") as file_script:
                bashCommand = ""
                for line in file_script.readlines():
                    if line[0] != "#":
                        bashCommand += line
                bashCommand = bashCommand.replace("\n", " ; ")
                subprocess.call(
                    bashCommand, stderr=subprocess.STDOUT, shell=True)
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


def argumentError(arg):
    """Argument error."""
    print("The argument {} isn't allowed,".format(arg.upper()) +
          " you can choose from this arguments:")
    for option in options:
        if options[option][0] != "no":
            print("\t - {} \n\t\t python yapi.py {} {}".format(
                options[option][1], option, options[option][0]))
        else:
            print("\t - {} \n\t\t python yapi.py {}".format(
                options[option][1], option))


if len(sys.argv) == 1:
    try:
        import kivy  # GUI Library
        from kivy.app import App
        from kivy.uix.button import Button
        from kivy.uix.gridlayout import GridLayout
        from kivy.uix.label import Label
        from kivy.uix.textinput import TextInput
        kivy.require('1.10.1')
    except ImportError:
        pass

    class packageScreen(GridLayout):
        """GUI."""

        def __init__(self, **kwargs):
            """Constructor."""
            super(packageScreen, self).__init__(**kwargs)
            self.packages = cache_manager.get_packages(where_is_scripts)
            for package_counter in packages:
                self.packages += "{:>2}) {} - {}\n".format(
                    package_counter,
                    packages[package_counter][0].capitalize(),
                    packages[package_counter][1])

            self.cols = 2
            self.packageList = Label(text=self.packages)
            self.packageInput = TextInput(multiline=False)
            self.commandOutput = Label(text='')
            self.submit = Button(text='Submit')

            self.add_widget(self.packageList)
            self.add_widget(self.packageInput)
            self.add_widget(self.commandOutput)
            self.add_widget(self.submit)
            self.submit.bind(on_press=self.submitCallback)

        def submitCallback(instance, instance2):
            """Installer."""
            packageText = instance.packageInput.text
            try:
                file_script = where_is_scripts + packageText + ".sh"
                with open(file_script, "r") as file_script:
                    bashCommand = ""
                    for line in file_script.readlines():
                        if line[0] != "#":
                            bashCommand += line
                    bashCommand = bashCommand.replace("\n", " ; ")
                    output = str(subprocess.call(
                        bashCommand, stderr=subprocess.STDOUT, shell=True))
            except (OSError, IOError, KeyError):
                output = "Package not found. Try again."
            instance.commandOutput.text = output

    class YAPIApp(App):
        """YAPI GUI."""

        def build(self):
            """Yapi build."""
            return packageScreen()
    if __name__ == '__main__':
        try:
            YAPIApp().run()
        except Exception:
            print("Kivy not installed. Please install or use arguments")

elif len(sys.argv) == 2:
    if (sys.argv[1] == "console"):
        packages = cache_manager.get_packages(where_is_scripts)
        consoleInstall()
    elif (sys.argv[1] == "update"):
        script_runner.runScript(where_is_scripts + "yapi.sh")
    elif (sys.argv[1] == "cache"):
        try:
            import os
            cache_file = where_is_scripts.strip("/") + ".bin"
            os.remove(cache_file)
            cache_manager.make_bin_from_packages(packages, cache_file)
        except FileNotFoundError:
            print("No cache found")
    else:
        argumentError(sys.argv[1])

elif len(sys.argv) == 3:
    if sys.argv[1] == "install":
        script_runner.runScript(sys.argv[2])
