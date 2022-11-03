# db_scrape_automation

<h2>Setup:</h2>
git clone repo<br>
create virutalenv<br>
pip install -r requirements.txt<br>

<h2>Instructions:</h2>
open main.py<br>
set desired number of quarterly periods to download parameter and save<br>
run main.py

<h2>Output:</h2>
running main.py will create a directory 'data'<br>
data will contain a directory for each quarterly period<br>
each period directory is named by date and contains .txt files<br>

<h2>Potential Issues:</h2>
If the chromedriver closes before all .zip files are downloaded from the ffiec page, it won't work.<br>
There is a built in time.sleep(10) in scrape.py to help prevent this.<br>
If you have a slower internet connection, increase the time.sleep parameter to allow the driver more time to download .zip files.
