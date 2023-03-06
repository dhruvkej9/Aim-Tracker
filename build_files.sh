echo " BUILD START"
python -m pip install --ignore-installed pip==21.2.4 --disable-pip-version-check --no-warn-script-location
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo " BUILD END" 
