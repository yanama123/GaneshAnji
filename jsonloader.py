
#
# def dict_to_yaml(data_dict, yaml_file_name):
#     """Convert the Dictionary to Yaml file
#     :param yaml_file_name: File name to save the yaml data
#     :param data: Dictionary variable which contains key, value pairs
#     :return: Boolean True or False
#     """
#     logging.info('Parsing Config Files')
#     try:
#         with open(yaml_file_name, 'w') as outfile:
#             logging.debug('Opening {}'.format(yaml_file_name))
#             # Dumping the data to yaml file
#
#             #yaml.dump(data_dict, outfile, default_flow_style=False)
#             logging.debug('Successfully converted the Dictionary to Yaml file')
#             result_flag = True
#     except FileNotFoundError:
#         message = 'FileNotFoundError: No such file or directory: {}'.format(yaml_file_name)
#         logging.fatal(message)
#         raise Exception(message)
#     except yaml.YAMLError as exc:
#         message = "Exception: An exception occured: {}".format(exc)
#         logging.fatal(message)
#         raise Exception(message)
#     except IOError as io_error:
#         message = "Exception: An exception occured: {}".format(io_error)
#         raise Exception(message)
#     except Exception as ex:
#         message = "Exception: An exception occured: {}".format(ex)
#         raise Exception(message)
#     return result_flag
import json
from pprint import pprint

with open('list1.json',encoding="utf8") as f:
    data = json.load(f)

pprint(data)
#print(data["maps"][0]["id"])