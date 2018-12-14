import cache_manager
import subprocess
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

where_is_scripts = "scripts/"


class packageScreen(GridLayout):
    """GUI."""

    def __init__(self, **kwargs):
        """Constructor."""
        super(packageScreen, self).__init__(**kwargs)
        self.packages = cache_manager.get_packages(
            where_is_scripts, "test.sh", "updateYapiScripts.sh")
        for package_counter in self.packages:
            self.packages += "{:>2}) {} - {}\n".format(
                package_counter,
                self.packages[package_counter][0].capitalize(),
                self.packages[package_counter][1])

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


def run():
    """Run GUI."""
    if __name__ == '__main__':
        try:
            YAPIApp().run()
        except Exception:
            print("Kivy not installed. Please install or use arguments")
