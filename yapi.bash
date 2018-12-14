#!/bin/bash
if [$1 == "install"]
then
  bash python3 yapi.py $1 $2
elif [$1 == "console"]
then
  bash python3 yapi.py $1
else
  bash python3 yapi.py
fi
