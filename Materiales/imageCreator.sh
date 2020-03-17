# !/ bin / bash

#Comprueba que solo haya 1 argumento
if [ $# -ne 1 ]
then
  echo "-ERROR- : Too many/not enough arguments were given, required 1 FILE"
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
