if [$1 == "install"]
then
  python3 yapi.py $1 $2
elif [$1 == "console"]
then
  python3 yapi.py $1
else
  python3 yapi.py
fi
