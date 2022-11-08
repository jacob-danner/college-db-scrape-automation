# db_scrape_automation

<h2>Setup:</h2>
git clone repo<br>
create virutalenv<br>
pip install -r requirements.txt<br>

<h2>Instructions:</h2>
navigate to the directory where repo was cloned. <br>
this script has a comman line interface <br>
specify the number of quarterly periods you want to download in the parameters <br>
<br>
Example Use: <br>
say I want to download the most recent quarter from the ffiec page; num_quarterly_downloads would be one <br>
from the comman line run: <code>python glue.py 1</code> <br>
<br>
Output: <br>
Running this script will output a directory, named tables <br>
tables contains a folder for each csv file <br>
within each csv_folder, there are the sql ready tables 
