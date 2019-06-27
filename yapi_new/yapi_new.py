from configparser import ConfigParser
import glob

_lenght_separator = 50
_separator = '-'

_get_default = lambda config, key: config['DEFAULT'][key]
_print_separator = lambda : print(_separator * _lenght_separator)

def _remove_whitespaces(string):
    while ', ' in string:
        string = string.replace(', ', ',')
    return string

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

    packages_path = 'packages/'
    lang_path = 'languages/'
    lang = ConfigParser()
    lang.read(lang_path+'en')

    config_path = 'config'
    config = ConfigParser()
    config.read(config_path)

    if _get_default(config,'language_use') is '':
        _print_separator()
        print(_get_default(lang,'conf0_title_language'))
        _print_separator()
        _config_language(lang,lang_path)
    else:
        lang.read(lang_path+_get_default(config, 'language_use'))

    _print_separator()
    print(_get_default(lang,'hello'))
    _print_separator()

    while True:

        print(_get_default(lang,'main0_main'))

        print(' - ' + _get_default(lang,'main0_title_install'))
        install_update_request = _remove_whitespaces(_get_default(lang,'main0_answers_install')).split(',')

        print(' - ' + _get_default(lang, 'main0_title_configuration'))
        change_config_request = _remove_whitespaces(_get_default(lang, 'main0_answers_configuration')).split(',')

        print(' - ' + _get_default(lang, 'main0_title_exit'))
        exit_request = _remove_whitespaces(_get_default(lang, 'main0_answers_exit')).split(',')

        choose = (str)(input('-----> ')).lower()

        if choose in exit_request:
            print(_get_default(lang, 'main1_title_exit'))
            exit()
        elif choose in install_update_request:
            _print_separator()
            print(_get_default(lang, 'main1_title_install'))
            _print_separator()
            while True:
                files_list = []
                for file in glob.glob(packages_path + '*'):
                    file_name = file.strip(packages_path).strip('.yp').strip('.sh')
                    print(' - ' + file_name)
                    files_list.append(file_name)
                print(' - ' + _get_default(lang, 'main0_title_exit'))
                choose = (str)(input('-----> ')).lower()
                print(_get_default(lang,'main2_title_install'))
                if choose in files_list:
                    _print_separator()
                    print(_get_default(lang,'main2_start_install').format(choose.capitalize()))
                    print(_get_default(lang,'main2_end_install').format(choose.capitalize()))
                    _print_separator()
                elif choose in exit_request:
                    break
                else:
                    _print_separator()
                    print(_get_default(lang, 'main1_title_undestand'))
                    _print_separator()
        elif choose in change_config_request:
            _print_separator()
            print(_get_default(lang, 'main1_title_configuration'))
            _print_separator()
            while True:
                for items in config.items():
                    for item in items[1]:
                        print(' - ' + item)
                    print(' - ' + _get_default(lang, 'main0_title_exit'))
                choose = (str)(input('-----> ')).lower()
                if choose == 'language_use':
                    _config_language(lang,lang_path)
                    break
                elif choose in exit_request:
                    break
                else:
                    _print_separator()
                    print(_get_default(lang, 'main1_title_undestand'))
                    _print_separator()
        else:
            print(_get_default(lang, 'main1_title_undestand'))

        _print_separator()


