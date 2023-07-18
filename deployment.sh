#!/bin/bash

sudo apt-get install curl

build_python_lib() {
 python setup.py sdist bdist_wheel
}

create_zip() {
  cd returns_prime_etl || exit
  zip -r ../returns_prime_etl.zip .
  cd ..
  zip returns_prime_etl_lambda_function.zip returns_prime_etl.zip connection.py main.py
}

upload_to_s3() {
  curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
  sudo installer -pkg ./AWSCLIV2.pkg -target /
 # Values coming from git secret manager
  export AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID"
 # Values coming from git secret manager
  export AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY"
  aws s3 cp returns_prime_etl_lambda_function.zip s3://tww-metabase-bucket
  #aws s3 cp main.py s3://tww-metabase-bucket/main.py
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