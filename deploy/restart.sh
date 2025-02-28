#!/bin/bash

checkNetNum () {
  netWorkNum=`docker network ls | grep prometheus_default |wc -l`
  return $netWorkNum
}

checkServerIsStop () {
  netNum=1
  # 检查网络是否关闭
  while [ $netNum -eq 1 ]
  do
    sleep 1
    checkNetNum
    netNum=$?
  done
}

sh deploy/stop.sh
checkServerIsStop
sh deploy/start.sh
