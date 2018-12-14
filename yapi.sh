if [$1 == "install"]
then
  python yapi.py $1 $2
elif [$1 == "console"]
then
  python yapi.py $1
else
  python yapi.py
fi
