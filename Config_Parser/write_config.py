from configparser import ConfigParser

config = ConfigParser()

#add configurations to config parser
config["case_1"] = {
    "neighbourhood_px_dist": 10,
    "show_output": False
}

config["case_2"] = {
    "neighbourhood_px_dist": 5,
    "show_output": True
}

config["case_3"] = {
    "neighbourhood_px_dist": 10,
    "show_output": True,
    "extra_debug_parameter":True
}

#save configurations
with open("my_test_config.ini", "w") as f:
    config.write(f)

