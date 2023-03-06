echo " BUILD START"
python -m ensurepip --upgrade
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo " BUILD END" 
