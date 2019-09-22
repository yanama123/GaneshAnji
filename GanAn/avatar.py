def get_secret(key, attribute):
    """
    sample yaml file
       rabbitmq:
          host: localhost
    :param key: yaml root key
    :param attribute: yaml nested key
    :return: value corresponding to the parameter
    """
    logger.info("Inside: get_secret")
    logger.debug("get_secret: parameters - {}, {}".format(key, attribute))
    try:
        encrypted_config_file = join(BASE_DIR, SECRETS_FILE_PATH)
        decrypt_file(BASE_DIR, encrypted_config_file, temp_file)
        doc = file_open(temp_file)
        param_value = doc[key][attribute]
        if os.path.exists(temp_file):
            remove(temp_file)
        logger.info("Exit: get_secret")
        return param_value
    except KeyError as e:
        e.message = "Missing key : {}".format(e)
        logger.exception(e)
        raise
    except FileNotFoundError as e:
        e.message = "{} : {}".format(e.strerror, e.filename)
        logger.exception(e)
        raise
