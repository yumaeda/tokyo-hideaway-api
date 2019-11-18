import json
import os

class AwsConfig:
    def __init__(self):
        """
        Initialize.
        """

    def read(self, filename='.aws_config.json'):
        """
        Read AWS config file.

        :param filename: Config filename, defaults to '.aws_config.json'
        :param filename: str, optional
        :return: Dictionary of AWS config.
        :rtype: Dict[str, str]
        """
        try:
            with open(filename) as json_data:
                config = json.load(json_data)

            for key in ('access_key_id', 'secret_access_key', 'region'):
                if key not in config.keys():
                    msg = '"{}" cannot be found in {}'.format(key, filename)
                    raise KeyError(msg)
                                    
        except FileNotFoundError:
            try:
                config = {
                    'access_key_id': os.environ['AWS_ACCESS_KEY_ID'],
                    'secret_access_key': os.environ['AWS_SECRET_ACCESS_KEY'],
                    'region': os.environ['AWS_REGION']
                }
            except KeyError:
                msg = 'No AWS config found in file or environment variables.'
                raise RuntimeError(msg)

        return config
