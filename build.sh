#!/usr/bin/env bash

echo "Build backend..."
sudo docker build -t registry.cn-hangzhou.aliyuncs.com/njupt-isl/tower:backend .
echo "Build nginx..."
sudo docker build -f ./nginx.dockerfile -t registry.cn-hangzhou.aliyuncs.com/njupt-isl/tower:nginx .

echo "Push Images..."
sudo docker push registry.cn-hangzhou.aliyuncs.com/njupt-isl/tower:backend
sudo docker push registry.cn-hangzhou.aliyuncs.com/njupt-isl/tower:nginx
sudo docker logout