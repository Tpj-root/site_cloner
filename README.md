Disclaimer:

This project is intended solely for educational purposes. The materials, code, and information provided within this project are designed to help individuals learn and understand various technical concepts and should not be used in a production environment without further modification and testing.


--------------------

Site: https://www.tamil2lyrics.com

This Git repository downloads all Tamil film lyrics. 
The lyrics are downloaded into folders named after each movie, and the song lyrics are saved in HTML format.

--------------------




--------------------
How to Use This Code
--------------------
Step 1: Set Up a Python Virtual Environment
Before running the code, it's a good practice to create a virtual environment. This isolates your project and ensures that dependencies do not conflict with other projects.

```
python3 -m venv mysite
source mysite/bin/activate
```

Step 2: Clone My GitHub Repository
Clone the repository to your local machine using the following command:

```
git clone "https://github.com/Tpj-root/site_cloner.git"
```

Step 3: Install the Required Dependencies
Navigate to the project directory and install the required dependencies:

```
pip install -r requirements.txt
```

Step 4: Run the Code
Finally, run the code with the following command:
```
python3 main_2.py
```

-------------------------

note:
main_1.py — This code is used to generate and collect all the film URLs.


-------------------------

Time Required for Runtime

For python3 main_1.py:

    The code processes 270 pages per URL request, and each request takes 10 seconds. 
    Therefore, the total runtime required is approximately 45 minutes. 
    The code has already been run to collect all the film URLs in movie_urls.txt.
    

For python3 main_2.py:

    The command cat movie_urls.txt | wc -l shows that there are approximately 4048 films.
    The total runtime required to download all the movie lyrics is approximately 11+ hours.
    (4048 * 10 ) / (60 * 60) = 11.24 hr


-------------------------






