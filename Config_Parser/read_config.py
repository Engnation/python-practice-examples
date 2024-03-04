from configparser import ConfigParser

config = ConfigParser()
config.read("my_test_config.ini")

config_sections = config.sections()

print(config_sections)

for section in config_sections:
    print(f"{section} {config.items(section)}")
    