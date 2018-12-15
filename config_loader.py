
def load_config_from_file(config_input, binary_output="config.bin"):
    """Reload configuration from file."""
    configuration = dict()
    with open(config_input, "r") as config:
        config_element = ""
        for line in config:
            if config_element:
                if line == "\n":
                    config_element = ""
                else:
                    try:
                        configuration[config_element].append(line.strip("\n"))
                    except Exception:
                        configuration[config_element] = list()
                        configuration[config_element].append(line.strip("\n"))
            if line[0] == "#":
                config_element = line.strip("# ").strip("\n")
        for conf in configuration:
            print(configuration[conf])


load_config_from_file("yapi.config")
