import configparser

transform_environments = {"prod", "qa", "perf"}
all_environments = {"prod", "qa", "test", "perf", "dev"}
required_sections_and_options = ['Environment', 'EncryptedKeys:Keys']
path = "./ConfigFiles/OriginalFile/testconfig.{env}.cfg"


def get_file_names():
    files = []
    for environment in all_environments:
        files.append(path.replace("{env}", environment))

    return files


def get_config_section_and_name(config_section):
    map = {}
    options = config.options(config_section)

    for option in options:
        map[option] = config.get(config_section, option)

    return map


def validate_config(env_section):
    env_name = config.get(env_section, "env")

    return env_name == "prod"

def decrypt_config_value(encrypted_config_value):
    # decrypt logic
    decrypted_value = encrypted_config_value

    return decrypted_value


def decrypt_config_section(config_map, encrypted_sections):
    decrypted_config_map = {}
    config_value = ''

    for config_map_section in config_map:
        if config_map_section in encrypted_sections:
            config_names = config.items(config_map_section)

            for config_name in config_names:
                config_value = configparser.get(config_map_section, config_name)
                decrypted_config_map[config_name] = decrypt_config_value(config_value)

    return decrypted_config_map


def validate_required_options():
    required_section = ''
    required_options_in_section = ''

    for option in required_sections_and_options:

        if ':' in option:
            section_details = option.split(":")
            required_section = section_details[0]
        else:
            required_section = option


        config.has_section()

# def decrypt_config_values(config_map, encrypted_names):
#     for config_map_section in config_map:
#         if config_map_section in encrypted_names:
#             configparser.get(config_map_section, )


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("./ConfigFiles/OriginalFile/testconfig.dev.cfg")

    if validate_required_options(config):

        envName = config.get("Environment", "env")
        encrypted_options = config.get("EncryptedKeys", "Keys")

        decrypted_config_map = {}

        for section in config.sections():
            config_map = (get_config_section_and_name(section))
            print(config_map)
            if envName in transform_environments:
                decrypted_config_map = decrypt_config_section(config_map, encrypted_options)

    print(decrypted_config_map)

    # if isTransformEnvironment:
    #     secureKeys = ["ACCOUNT", "Environment"]




# parser.set('ACCOUNT', "user", "xyztest1")
# with open(r"./ConfigFiles/testconfig.cfg", "wb") as configFile:
#     parser.write(configFile)