import os

os.environ['GCLOUD_PROJECT'] = os.environ.get('GCLOUD_PROJECT', "firecloud-cgl")
os.environ['WORKSPACE_NAME'] = os.environ.get('WORKSPACE_NAME', "terra-notebook-utils-tests")
os.environ['WORKSPACE_BUCKET'] = os.environ.get('WORKSPACE_BUCKET', "gs://fc-9169fcd1-92ce-4d60-9d2d-d19fd326ff10")
