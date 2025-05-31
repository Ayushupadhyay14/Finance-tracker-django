 echo "BUILD START"
 python3.13.3 -m pip install -r requirment.txt
 python3.13.3 manage.py collectstatic --noinput --clear
 echo "BUILD END"