import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_test",
    version="0.0.1",
    
    description="A sample CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk_test"},
    packages=setuptools.find_packages(where="cdk_test"),

    install_requires=[
        "aws-cdk.core==1.28.0",
        "aws-cdk.aws_iam==1.28.0",
        "aws-cdk.aws-lambda==1.28.0",
        "aws-cdk.aws_sns==1.28.0",
        "aws-cdk.aws_sns_subscriptions==1.28.0",
        "aws-cdk.aws_s3==1.28.0",
    ],

    python_requires=">=3.8",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
