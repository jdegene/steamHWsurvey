# shs.csv
* Regularly updated [Steam Hardware Survey Data](https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam)

* Data from 2008-11-01 - now (data before ca. 2020 was collected through web.archive)

* The Python script includes functions to collect the current months steam hardware survey data or past data from web.archive.org

# shs_platform.csv

* Regularly updated platform dependent [data](https://store.steampowered.com/hwsurvey?platform=pc). Fetches Linux, Mac & PC.

* Data from 2023-11-01 - now (data before 2023-11 was collected through web.archive with some months/platform combinations missing)

* The Python script includes functions to collect the current months steam hardware survey data or past data from web.archive.org

# General Information

* As mentioned by [luxzg](https://github.com/jdegene/steamHWsurvey/issues/1): some video card names have stuff like "(R)" or "Series" added to the names, and thus could introduce duplicates to the data

* After an initial release of December 2022 hardware data that showed [some odd discrepancies](https://archive.is/XyyNP), Steam reuploaded a revised dataset. The current shs.csv uses the revised data (original data can be found in first commit for December 2022 data)

* Data from March 2023 (= posted in April 2023 on the steam website) saw unusual spikes in several areas (like growth in "Language: Simplified Chinese" or "Intel CPU" share amongst others). The reason was never officially addressed (but may be due to similar reasons as pointed in official statements by steam below) nor was the data updated during the span April on the website. With the April data update in May, these outliers have seemed to be mitigated and numbers are closer to prior months.

* As mentioned by [likudo](https://github.com/jdegene/steamHWsurvey/issues/4) the raw data omits the category "others". Creating a category sum can as such create misleading results. Refer to the platform specific data instead.

# Official Information posted on the Steam Hardware Survey Site

STEAM HARDWARE SURVEY FIX – 5/2/2018

The latest Steam Hardware Survey incorporates a number of fixes that address over counting of cybercafé customers that occurred during the prior seven months.

Historically, the survey used a client-side method to ensure that systems were counted only once per year, in order to provide an accurate picture of the entire Steam user population. It turns out, however, that many cybercafés manage their hardware in a way that was causing their customers to be over counted.

Around August 2017, we started seeing larger-than-usual movement in certain stats, notably an increase in Windows 7 usage, an increase in quad-core CPU usage, as well as changes in CPU and GPU market share. This period also saw a large increase in the use of Simplified Chinese. All of these coincided with an increase in Steam usage in cybercafés in Asia, whose customers were being over counted in the survey.

It took us some time to root-cause the problem and deploy a fix, but we are confident that, as of April 2018, the Steam Hardware Survey is no longer over counting users. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
(2012-06)

Why do many of the Steam Hardware Survey numbers seem to undergo a significant change in April 2012?

There was a bug introduced into Steam's survey code several months ago that caused a bias toward older systems. Specifically, only systems that had run the survey prior to the introduction of the bug would be asked to run the survey again. This caused brand-new systems to never run the survey. In March 2012, we caught the bug, causing the survey to be run on a large number of new computers, thus giving us a more accurate survey and causing some of the numbers to vary more than they normally would month-to-month. Some of the most interesting changes revealed by this correction were the increased OS share of Windows 7 (as Vista fell below XP), the rise of Intel as a graphics provider and the overall diversification of Steam worldwide (as seen in the increase of non-English language usage, particularly Russian). 
