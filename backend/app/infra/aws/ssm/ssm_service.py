import os

import boto3

from .ssm_keys import ssm_keys


class SSMService:
    def __init__(self):
        self.ssm = boto3.client("ssm", region_name=os.environ.get("AWS_REGION"))
        self.ssm_parameters_cache = {}
        self.load_parameters(list(ssm_keys.values()))

    def load_parameters(self, keys):
        if not keys:
            return
        response = self.ssm.get_parameters(Names=keys, WithDecryption=True)
        for param in response.get("Parameters", []):
            self.ssm_parameters_cache[param["Name"]] = param["Value"]

    def get(self, key):
        if key not in self.ssm_parameters_cache:
            self.load_parameters([key])
        return self.ssm_parameters_cache.get(key)


ssm_service = SSMService()
