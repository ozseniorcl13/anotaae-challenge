import os

ssm_keys = {"sqs_catalog": f"anotae-catalog-sqs-url-{os.environ.get('ENV')}"}
