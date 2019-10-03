# Natural Language Sentiment Analysis 
>using Google Cloud Natural Language API Client Libraries

## A python script that does a sentiment analysis of an excel or text file. 

- For **excel**, it analyzes the sentiment for each cell separately and stores the results next to it and saves it to the file "s_[original file name]".
- For **text** file, it analyzes the sentiment of the whole file and shows you the results.

I used Google's Cloud Natural Language API and it's new (beta) Natural Language API Client Libraries that are pre-trained and highly accurate. The API can analyze the following languages (which are detected automatically): 
- Chinese (Simplified & Traditional), English, French, German, Italian, Japanese, Korean, Portuguese (Brazilian & Continental), Spanish

Results have following parameters:
- **Score** of the sentiment ranges between -10 (negative) and 10 (positive) and corresponds to the overall emotional leaning of the text.
- **Magnitude** indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and infinity.
---
## If you want to test my scrip for yourself, please, follow these instructions.
>I've tested it on Mac OS, so, normally, it should work on Linux too, but I'm not sure about Windows. 

To get it setup and running, please, do the following:
1. download or upgrade your python to version 3 or higher (it won't work on python 2).
2. download the script
3. from terminal go to it's folder, then do:  
    `pip3 install -r requirements.txt`
    >- it will install all the necessary modules for the script to work
    >- if you don't have pip you can install it from [here](https://pip.pypa.io/en/stable/installing/), thought, normally, it comes preinstalled when you download python3.
4. Configure Google Cloud Console and download your key.
    - Register at https://cloud.google.com/
    - In the GCP Console, go to the [Create service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.77969431.-249870926.1567691041) page.
    - From the **Service account** list, select **New service account**.
    - In the **Service account name** field, enter a name.
    - From the **Role** list, select **Project > Owner**.
    - Click **Create**. A JSON file that contains your key downloads to your computer.
    - Then from terminal export your Google key:  
        `export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"`  
        For example:  
        `export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/fortify.json"`
        >for Google NL API to work you’d have to do the last step (export your key) every time you open a terminal, because when you exit, it gets removed.

5. That's it ! Now you can use the script from terminal as follows:  
    `python3 analyze.py [file]`  
    For example:  
    `python3 analyze.py test.xls`

    >- accepted file extensions are .xls/.xlsx for excel and .txt for text
    >- please note that excel files should be without headers, just with text in cells

And for the Google Cloud NL API using the script you can do up to 5000 analyses per month for free. You can check the number of requests you've made during the month here: https://console.cloud.google.com/apis/dashboard