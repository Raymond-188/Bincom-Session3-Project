from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    # create parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    todo_list = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            todo_list[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    return todo_list


config()
