import json
import boto3

from aws_config import AwsConfig

# CONSTANTS
SECRET_NAME = 'RDSSecret3683CA93-0pVOwSQetUgt'

class Config:
    def __init__(self):
        """
        Constructor
        """

    def __get_secrets_mgr(self):
        """
        Get AWS secrets manager.
        """
        aws_config = AwsConfig().read()
        session    = boto3.session.Session(
            aws_access_key_id=aws_config['access_key_id'],
            aws_secret_access_key=aws_config['secret_access_key'],
            region_name=aws_config['region']
        )
        return session.client(
            service_name='secretsmanager',
            region_name=aws_config['region']
        )

    @property
    def db_connection_string(self):
        """
        Get Database connection string.
        """
        secret_mgr = self.__get_secrets_mgr()
        response = secret_mgr.get_secret_value(SecretId=SECRET_NAME)
        if 'SecretString' in response:
            secret = json.loads(response['SecretString'])
            return 'mysql://{master_user}:{pwd}@{endpoint}/{db_name}'.format(
                master_user=secret['username'],
                pwd=secret['password'],
                endpoint=secret['host'],
                db_name='kojinten'
            )
        else:
            return ''
