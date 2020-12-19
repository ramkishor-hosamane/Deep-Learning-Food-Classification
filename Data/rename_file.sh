
read -p "Enter offset :" i
read -p "Enter fruitname :" fruit


fruit=${fruit}_
echo $fruit
for x in *.jpg 
do
 mv $x $fruit$i.jpg
 i=$(expr $i + 1)
done
