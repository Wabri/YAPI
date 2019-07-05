from configparser import ConfigParser
import glob

_packages_path = 'packages/'
_lang_path = 'languages/'

_lenght_separator = 50
_separator = '-'

_get_default = lambda config, key: config['DEFAULT'][key]
_print_separator = lambda separetor=_separator, lenght=_lenght_separator: print(separetor * lenght)

def _remove_whitespaces(string):
    while ', ' in string:
        string = string.replace(', ', ',')
    return string

def _category_chosing(lang, packages_path=_packages_path):
    title_category = _get_default(lang, 'main2_title_category')
    _print_separator(lenght=len(title_category))
    print(title_category)
    _print_separator(lenght=len(title_category))
    del title_category

    info_packages = {}

    for file in glob.glob(packages_path + '*'):
        packages_temp = ConfigParser()
        packages_temp.read(file)
        for category in _remove_whitespaces(_get_default(packages_temp, 'class')).split(','):
            if category not in info_packages.keys():
                info_packages[category] = []
            info_packages[category].append(_get_default(packages_temp, 'name'))
        del packages_temp

    print('Choose one of this category')

    for classes in info_packages:
        print(' - {} ({}) '.format(classes, len(info_packages[classes])))
    print(' - ' + _get_default(lang, 'title_back'))
    back_request = _remove_whitespaces(_get_default(lang, 'title_back_answers')).split(',')
    print(' - ' + _get_default(lang, 'title_exit'))
    exit_request = _remove_whitespaces(_get_default(lang, 'title_exit_answers')).split(',')

    choose = (str)(input('-----> ')).lower()
    if choose in back_request:
        return 1
    if choose in exit_request:
        return 2
    elif choose in info_packages:
        print('You choose the category {}'.format(choose))
    else:
        print(_get_default(lang, 'main1_title_undestand'))

def _install_procedure(lang, packages_path=_packages_path):
    while True:

        title_install = _get_default(lang,'main2_title_install')
        _print_separator(lenght=len(title_install))
        print(title_install)
        _print_separator(lenght=len(title_install))
        del title_install

        exit_request = _remove_whitespaces(_get_default(lang, 'title_exit_answers')).split(',')
        back_request = _remove_whitespaces(_get_default(lang, 'title_back_answers')).split(',')

        files_list = []
        for file in glob.glob(packages_path + '*'):
            packages_temp = ConfigParser()
            packages_temp.read(file)
            file_name = _get_default(packages_temp, 'name')
            print(' - ' + file_name)
            files_list.append(file_name)
            del packages_temp
        print(' - ' + _get_default(lang, 'title_back'))
        print(' - ' + _get_default(lang, 'title_exit'))

        choose = (str)(input('-----> ')).lower()

        if choose in files_list:
            start_install =_get_default(lang,'main3_start_install').format(choose.capitalize())
            end_install = _get_default(lang,'main3_end_install').format(choose.capitalize())
            max_string = max(len(start_install),len(end_install))
            _print_separator(lenght=max_string)
            print(start_install)
            print(end_install)
            _print_separator(lenght=max_string)
            del start_install, end_install, max_string
        elif choose in back_request:
            break
        elif choose in exit_request:
            print(_get_default(lang, 'bye'))
            exit()
        else:
            title_undestand = _get_default(lang, 'main1_title_undestand')
            _print_separator(lenght=len(title_undestand))
            print(title_undestand)
            _print_separator(lenght=len(title_undestand))
            del title_undestand

def _config_language(lang, lang_path):
    lang_list = []

    for file in glob.glob(lang_path +'*'):
        lang_file = (str)(file)
        lang_temp = ConfigParser()
        lang_temp.read(lang_file)
        lang_name = _get_default(lang_temp,'name')
        lang_list.append([lang_file.replace(lang_path,'').lower(),lang_name])
        del lang_temp, lang_file, lang_name

    not_choose = True
    while not_choose:
        print(_get_default(lang,'conf1_title_language'))

        for language in lang_list:
            print(' - {} ({})'.format(language[1].capitalize(), language[0]))

        choose = (str)(input('-----> ')).lower()

        for language in lang_list:
            if choose in language[0].lower() or choose in language[1].lower():
                lang_temp = ConfigParser()
                config.set('DEFAULT', 'language_use', language[0])
                with open(config_path, 'w') as configfile:
                    config.write(configfile)
                not_choose = False
                print(_get_default(lang,'conf2_title_language').format(language[1].capitalize()))
                lang.read(lang_path + language[0])

if __name__ == '__main__':

    lang = ConfigParser()
    lang.read(_lang_path + 'en')

    config_path = 'config'
    config = ConfigParser()
    config.read(config_path)

    if _get_default(config,'language_use') is '':
        title_conf_language = _get_default(lang,'conf0_title_language')
        _print_separator(lenght=len(title_conf_language))
        print(title_conf_language)
        _print_separator(lenght=len(title_conf_language))
        del title_conf_language
        _config_language(lang,_lang_path)
    else:
        lang.read(_lang_path+_get_default(config, 'language_use'))

    hello = _get_default(lang,'hello')
    _print_separator(lenght=len(hello))
    print(hello)
    _print_separator(lenght=len(hello))
    del hello

    while True:

        print(_get_default(lang,'main0_main'))

        print(' - ' + _get_default(lang,'main0_title_install'))
        install_update_request = _remove_whitespaces(_get_default(lang,'main0_answers_install')).split(',')

        print(' - ' + _get_default(lang, 'main0_title_configuration'))
        change_config_request = _remove_whitespaces(_get_default(lang, 'main0_answers_configuration')).split(',')

        print(' - ' + _get_default(lang, 'title_exit'))
        exit_request = _remove_whitespaces(_get_default(lang, 'title_exit_answers')).split(',')

        choose = (str)(input('-----> ')).lower()

        if choose in exit_request:
            print(_get_default(lang, 'bye'))
            exit()
        elif choose in install_update_request:
            while True:
                title_install = _get_default(lang, 'main1_title_install')

                _print_separator(lenght=len(title_install))
                print(title_install)
                _print_separator(lenght=len(title_install))
                del title_install

                print(' - ' + _get_default(lang,'main1_list_install'))
                list_install = _remove_whitespaces(_get_default(lang,'main1_list_answers_install')).split(',')

                print(' - ' + _get_default(lang,'main1_categorize_install'))
                category_install = _remove_whitespaces(_get_default(lang,'main1_categorize_answers_install')).split(',')

                print(' - ' + _get_default(lang, 'title_back'))
                back_request = _remove_whitespaces(_get_default(lang, 'title_back_answers')).split(',')

                print(' - ' + _get_default(lang, 'title_exit'))
                exit_request = _remove_whitespaces(_get_default(lang, 'title_exit_answers')).split(',')

                choose = (str)(input('-----> ')).lower()

                if choose in exit_request:
                    print(_get_default(lang, 'bye'))
                    exit()
                if choose in back_request:
                    break
                elif choose in list_install:
                    _install_procedure(lang)
                elif choose in category_install:
                    category_result = _category_chosing(lang, _packages_path)
                    if  category_result == 1:
                        break
                    elif category_result == 2:
                        print(_get_default(lang, 'bye'))
                        exit()
                    del category_result
                else:
                    print(_get_default(lang, 'main1_title_undestand'))

        elif choose in change_config_request:
            title_configuration = _get_default(lang, 'main1_title_configuration')
            _print_separator(lenght=len(title_configuration))
            print(title_configuration)
            _print_separator(lenght=len(title_configuration))
            del title_configuration

            while True:
                for items in config.items():
                    for item in items[1]:
                        print(' - ' + item)
                    print(' - ' + _get_default(lang, 'title_exit'))
                    print(' - ' + _get_default(lang, 'title_back'))
                exit_request = _remove_whitespaces(_get_default(lang, 'title_exit_answers')).split(',')
                back_request = _remove_whitespaces(_get_default(lang, 'title_back_answers')).split(',')

                choose = (str)(input('-----> ')).lower()

                if choose == 'language_use':
                    _config_language(lang,_lang_path)
                    break
                elif choose in back_request:
                    break
                elif choose in exit_request:
                    print(_get_default(lang, 'bye'))
                    exit()
                else:
                    title_understand = _get_default(lang, 'main1_title_undestand')
                    _print_separator(lenght=len(title_understand))
                    print(title_understand)
                    _print_separator(lenght=len(title_understand))
                    del title_understand
        else:
            print(_get_default(lang, 'main1_title_undestand'))

        _print_separator()


