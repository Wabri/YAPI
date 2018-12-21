try:
    import cache_manager          #Cache Manager
    import script_runner          #Script Runner
    import toga                   #GUI Library
    from toga.style.pack import * #GUI Components
except ImportError:
    pass

where_is_scripts = "scripts/"

def build(app):
    def installHandle(widget):
        import script_runner
        packageToInstall = packageInput.value
        resultInput.value = script_runner.runScript(where_is_scripts + packageToInstall + ".sh")

    packages = cache_manager.get_packages(
        where_is_scripts, "test.sh", "updateYapiScripts.sh")
    box = toga.Box()
    listBox = toga.Box()
    listLabel = toga.Label('Packages Available: ')
    packageBox = toga.Box()
    packageLabel = toga.Label('Package To Install:')
    packageInput = toga.TextInput()
    submitBox = toga.Box()
    install = toga.Button('Install Package', on_press=installHandle)
    resultBox = toga.Box()
    resultInput = toga.TextInput(readonly = True)

    listBox.add(listLabel)
    packageBox.add(packageLabel)
    packageBox.add(packageInput)
    submitBox.add(install)
    resultBox.add(resultInput)
    box.add(listBox)
    box.add(packageBox)
    box.add(submitBox)
    box.add(resultBox)

    box.style.update(direction=COLUMN, padding_top=10)
    listBox.style.update(direction=ROW, padding=5)
    packageBox.style.update(direction=ROW, padding=5)
    submitBox.style.update(direction=ROW, padding=5)
    return box

def start():
    return toga.App('Yet Another Package Manager', 'org.YAPI.yapi', startup=build).main_loop()

def main():
    start().main_loop()
