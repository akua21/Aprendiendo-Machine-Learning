dir="102blur/jpg"

for f in $dir/*; do
  num=$(echo $f | cut -d / -f 3 | cut -d . -f 1 | cut -d _ -f 2)

  if [ $(($num)) -lt 10 ]
  then
    mv $f $dir/image_0000$num.jpg
  else
    if [ $(($num)) -lt 100 ]
    then
      mv $f $dir/image_000$num.jpg
    else
      if [ $(($num)) -lt 1000 ]
      then
        mv $f $dir/image_00$num.jpg
      else
        mv $f $dir/image_0$num.jpg
      fi
    fi
  fi
done
