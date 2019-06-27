from configparser import ConfigParser
import glob

def _remove_whitespaces(string):
    while ', ' in string:
        string = string.replace(', ', ',')
    return string

if __name__ == '__main__':

    get_default = lambda config, key: config['DEFAULT'][key]
    lang_path = 'languages/'
    lang = ConfigParser()
    lang.read(lang_path+'en')

    config_path = 'config'
    config = ConfigParser()
    config.read(config_path)

    if get_default(config,'language_use') is '':
        lang_list = []
        print('-'*50)
        print(get_default(lang,'lang_missing'))
        print('-'*50)
        for file in glob.glob(lang_path +'*'):
            lang_file = (str)(file)
            lang_temp = ConfigParser()
            lang_temp.read(lang_file)
            lang_name = get_default(lang_temp,'name')
            lang_list.append([lang_file.replace(lang_path,'').lower(),lang_name])
            del lang_temp, lang_file, lang_name
        not_choose = True
        while not_choose:
            print('Select language')
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
                    print('You choose {} language'.format(choose))
                    lang.read(lang_path + language[0])
    else:
        lang.read(lang_path+get_default(config, 'language_use'))

    print('-'*50)
    print(get_default(lang,'hello'))
    print('-'*50)

    while True:

        print(get_default(lang,'post_config_question_0'))

        print(' - ' + get_default(lang,'answer_question0_0'))
        install_update_request = _remove_whitespaces(get_default(lang,'user_answers_answer0')).split(',')

        print(' - ' + get_default(lang, 'answer_question0_1'))
        change_config_request = _remove_whitespaces(get_default(lang, 'user_answers_answer1')).split(',')

        print(' - ' + get_default(lang, 'answer_question0_2'))
        exit_request = _remove_whitespaces(get_default(lang, 'user_answers_answer2')).split(',')

        choose = (str)(input('-----> ')).lower()

        if choose in exit_request:
            print(get_default(lang, 'answer_user_question0_2'))
            exit()
        elif choose in install_update_request:
            print(get_default(lang, 'answer_user_question0_0'))
        elif choose in change_config_request:
            print(get_default(lang, 'answer_user_question0_1'))
        else:
            print(get_default(lang, 'answer_user_understand'))

        print('-'*50)


