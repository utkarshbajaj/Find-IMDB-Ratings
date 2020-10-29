# Find IMDB Ratings 
<!--Remove the below lines and add yours -->
This script is used to fetch the Ratings and Genre of the films in your films folder that match with ones on IMDb, the data is scraped from IMDB's official website and store in a csv file. The csv file can be used for analysis then, sorting acc to rating etc. 

Input: -> Path of the directory which contains the films. 

Output: -> A new csv file is made - 'film_ratings.csv' which contains the ratings for the films in your directory. 

__P.S. - Please ask for assign before making a PR.__<br>Creation of new issues is encouraged. 

Do a git pull from the master repo before making a new Pull Request using<br>
`git remote add upstream https://github.com/utkarshbajaj/Find-IMDB-Ratings` <br>
`git fetch upstream`<br>
`git pull upstream master` 

### Prerequisites
<!--Remove the below lines and add yours -->
This program uses and external dependency of 'BeautifulSoup' (for web scraping), 'requests' (for fetching content of the webpage), 'pandas' (to make the csv file), 'os' (to get data from directory). <br>
These libraries can be installed easily by using the following command: `pip install -r requirements.txt`

### How to run the script
<!--Remove the below lines and add yours -->
1. Install the requirements using the `pip install -r requirements.txt` command. <br>
2. Type the following command: `python GUI.py` <br>
3. Browse to the path where Films are located inside the folder  <br>
4. A csv file with rating will be created in the same directory as the python file. <br>

### Sample use of the script
<!--Remove the below lines and add yours -->
Script :

![new](https://user-images.githubusercontent.com/44445191/94925225-7fe59280-04dc-11eb-843e-df5dd3ea07f8.gif)

Folder :

![Screenshot 2020-10-02 at 6 15 22 PM](https://user-images.githubusercontent.com/44445191/94925320-a4da0580-04dc-11eb-85e8-b27962d51d97.png)

Result: (Also stored in a csv file)

![Screenshot 2020-10-02 at 6 23 29 PM](https://user-images.githubusercontent.com/44445191/94925387-c2a76a80-04dc-11eb-9ee6-893880c53362.png)


## Author
[Utkarsh Bajaj](https://github.com/utkarshbajaj)

## Contributors 
* [Avarindha](https://github.com/Aravindha1234u)
* [Vipul Bajaj](https://github.com/Vipul-Bajaj)
