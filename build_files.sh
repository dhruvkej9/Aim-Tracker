echo " BUILD START"
sudo apt install python-pip
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo " BUILD END" 
