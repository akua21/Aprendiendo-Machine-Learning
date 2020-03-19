# !/ bin / bash

#Comprueba que solo haya 1 argumento
if [ $# -ne 2 ]
then
  echo "-ERROR- : Too many/not enough arguments were given, required 2 FILE: origin, dest"
  exit 0
fi

directory=$1
#Comprueba que sea un directorio

#Si no es un directorio
if ! [[ -d $directory ]]
then
  echo "$directory is not a directory"
  exit 0
fi

src=$2

#Si no es un directorio
if ! [[ -d $src ]]
then
  echo "$src is not a directory"
  exit 0
fi


i=0

name="flower_"
count=1
termination=".jpg"

#Recorrer todos los archivos del directorio pasado por parametro
for file in "$directory"/*
do

  fullname="${src}/${name}${count}${termination}"

  #convert  $file  -channel G -level 25%,100%,.6 $fullname
  convert $file +dither -colors 32 $fullname
  convert $fullname +dither -posterize 3 $fullname
  convert $fullname -dither None -colors 64 $fullname
  convert $file +dither -colors 32 $fullname
  convert $fullname -separate -threshold 70% -combine $fullname
  convert $fullname -blur 0x3 -paint 10 $fullname
  convert $fullname -filter Gaussian -blur 0x8 $fullname
  convert $fullname -filter Gaussian -blur 0x8 $fullname
  convert $fullname -filter Gaussian -resize 10% -define filter:sigma=2.5 -resize 1000%  $fullname


  echo $fullname

  ((count++))


done
