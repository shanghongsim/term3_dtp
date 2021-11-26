Instuctions to run on Vocareum:

1) change directory to "Web App" folder:
cd "Web App"

2) Create Virtual Env
python -m venv virtenv

3) Activate virtual Env
source virtenv/bin/activate

4) Install Python Packages
python -m pip install -U --force-reinstall -r requirements.txt

5) make linux/vocareum allow you to run flask
chmod a+x ./runflaskvoc.sh

6) Run flask web app
./runflaskvoc.sh

7) usage:
Insert corresponding data values from cowid data set (csv) 
https://github.com/owid/covid-19-data/blob/master/public/data/README.md
or insert your own values on to the web fields
