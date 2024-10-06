import os

ssm_keys: dict = {
    "sqs_catalog": f"anotae-catalog-sqs-url-{os.environ.get('ENV')}",
    "s3_catalog": f"anotae-catalog-s3-bucket-{os.environ.get('ENV')}",
}
