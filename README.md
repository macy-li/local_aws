# local_aws
Contains sample code to develop and test AWS applications locally.


    .
    ├── localstack              # examples with localstack
    │   ├── lambda_localstack   # use CLI to deploy and invoke lambda function (run this first to create resources )
    │   ├── sam_localstack      # use SAM to deploy lambda function ( no trigger event configured )
    │   └── sam_localstack_1    # use SAM to deploy lambda function ( with trigger , SQS as event source )
    ├── moto                    # example test cases with moto
    └── Readme.md

## localstack
localstack is a cloud service emulator that runs in a single container on your laptop or in your CI environment.

### Requirements

* `python` (Python 3.6 up to 3.9 supported)
* `pip` (Python package manager)
* `Docker`

### Install

The easiest way to install LocalStack is via `pip`:
```
pip install localstack
```

#### Localstack AWS CLI (optional)
Localstack provides the `awslocal` command line, a simple wrapper around the `aws` command line interface for use with LocalStack.
```
pip install awscli-local
```

#### Localstack AWS SAM CLI
Localstack provides the `samlocal` command line, a simple wrapper around the AWS `sam` CLI for use with LocalStack.
To deploy SAM in localstack, you will need to install this library.
```
pip install aws-sam-cli-local
```
### Running

By default, LocalStack is started inside a Docker container by running:
```
localstack start
```

For more information please refer to [localstack github repo](https://github.com/localstack/localstack)

#### Port forwardinn if running Docker with Docker-machine on Virtualbox 
Forword port 4566 on docker-machine to localhost port 4566 under Settings -> Network -> Advanced -> Port Forward.

## Moto
Moto is a library that allows your tests to easily mock out AWS services.

## Install

To install moto for a specific service:
```console
$ pip install moto[ec2,s3]
```
This will install Moto, and the dependencies required for that specific service.
If you don't care about the number of dependencies, or if you want to mock many AWS services:
```console
$ pip install moto[all]
```

For more information please refer to [moto github repo](https://github.com/spulec/moto)







