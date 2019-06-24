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
        lang_dict = []
        print(get_default(lang,'lang_missing'))
        for file in glob.glob(lang_path+'*'):
            lang_file = (str)(file)
            print(lang_file)
            lang.read(lang_path + lang_file)
            lang_name = get_default(lang,'name')
            print(lang_name)
            lang_dict.append([lang_file.replace(lang_path,''),lang_name])
            lang.clear()

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


