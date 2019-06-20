
if __name__ == '__main__':

    print('-'*50)
    print('Hello this is YAPI new version')
    print('-'*50)

    while True:
        print('What do you want to do?')

        print(' - Install/update packages')
        install_update_request = ['install', 'update', 'install packages', 'update packages']

        print(' - Change configuration')
        change_config_request = ('configuration', 'config', 'change', 'change config', 'change configuration')

        print(' - Exit')
        exit_request = ('exit', 'quit')

        choose = (str)(input('-----> ')).lower()

        if choose in exit_request:
            print('Bye')
            exit()
        elif choose in install_update_request:
            print('Install update packages')
        elif choose in change_config_request:
            print('Change config')
        else:
            print("Sorry I don't understand")

        print('-'*50)


