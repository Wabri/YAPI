
def _remove_whitespaces(string):
    while ', ' in string:
        string = string.replace(', ', ',')
    return string

if __name__ == '__main__':

    from configparser import ConfigParser


    lang_path = 'languages/en'
    lang = ConfigParser()
    lang.read(lang_path)
    get_default_lang = lambda config, key: config['DEFAULT'][key]

    print('-'*50)
    print(get_default_lang(lang,'hello'))
    print('-'*50)

    while True:


        print(get_default_lang(lang,'post_config_question_0'))

        print(' - ' + get_default_lang(lang,'answer_question0_0'))
        install_update_request = _remove_whitespaces(get_default_lang(lang,'user_answers_answer0')).split(',')

        print(' - ' + get_default_lang(lang, 'answer_question0_1'))
        change_config_request = _remove_whitespaces(get_default_lang(lang, 'user_answers_answer1')).split(',')

        print(' - ' + get_default_lang(lang, 'answer_question0_2'))
        exit_request = _remove_whitespaces(get_default_lang(lang, 'user_answers_answer2')).split(',')

        choose = (str)(input('-----> ')).lower()

        if choose in exit_request:
            print(get_default_lang(lang, 'answer_user_question0_2'))
            exit()
        elif choose in install_update_request:
            print(get_default_lang(lang, 'answer_user_question0_0'))
        elif choose in change_config_request:
            print(get_default_lang(lang, 'answer_user_question0_1'))
        else:
            print(get_default_lang(lang, 'answer_user_understand'))

        print('-'*50)


