#!/bin/bash

sudo apt-get install curl

build_python_lib() {
 python setup.py sdist bdist_wheel
}

upload_to_s3() {
  curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
  unzip AWSCLIV2.zip
  sudo ./aws/install
 # Values coming from git secret manager
  export AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID"
 # Values coming from git secret manager
  export AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY"
  aws s3 cp dist/*.whl s3://tww-metabase-bucket
  aws s3 cp delhivery-courier-tracker.py s3://tww-metabase-bucket/main.py
}

deploy() {
  build_python_lib
  upload_to_s3
}

case $1 in
all)
  deploy
  ;;
libgen)
  build_python_lib
  ;;
s3deploy)
  upload_to_s3
  ;;
*)
  echo "Please enter a valid input"
esac