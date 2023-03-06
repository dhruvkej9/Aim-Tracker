echo " BUILD START"
sudo pip install virtualenv
virtualenv newenv
source newenv/bin/activate
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo " BUILD END" 
