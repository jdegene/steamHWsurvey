# Files Description
## shs.csv
* Regularly updated [Steam Hardware Survey Data](https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam)

* Data from 2008-11-01 - now (data before ca. 2020 was collected through web.archive)

* The Python script includes functions to collect the current months steam hardware survey data or past data from web.archive.org

## shs_platform.csv

* Regularly updated platform dependent [data](https://store.steampowered.com/hwsurvey?platform=pc). Fetches Linux, Mac & PC.

* Data from ca. 2010-06-01 - now (data before 2023-11 was collected through web.archive with some months/platform combinations missing. No Linux data exists before 2014 in the archive.)

* The Python script includes functions to collect the current months steam hardware survey data or past data from web.archive.org

# Infos

## Watchouts & Known Discrepancies

* As mentioned by [luxzg](https://github.com/jdegene/steamHWsurvey/issues/1): some video card names have stuff like "(R)" or "Series" added to the names, and thus could introduce duplicates to the data

* After an initial release of December 2022 hardware data that showed [some odd discrepancies](https://archive.is/XyyNP), Steam reuploaded a revised dataset. The current shs.csv uses the revised data (original data can be found in first commit for December 2022 data)

* Data from March 2023 (= posted in April 2023 on the steam website) saw unusual spikes in several areas (like growth in "Language: Simplified Chinese" or "Intel CPU" share amongst others). The reason was never officially addressed (but may be due to similar reasons as pointed in official statements by steam below) nor was the data updated during the span April on the website. With the April data update in May, these outliers have seemed to be mitigated and numbers are closer to prior months.

* As mentioned by [likudo](https://github.com/jdegene/steamHWsurvey/issues/4) the raw data omits the category "others". Creating a category sum can as such create misleading results. Refer to the platform specific data instead.

* As mentioned by [mrxz](https://github.com/jdegene/steamHWsurvey/issues/5) the data did not include "total rows", as in "Steam users with VR Headsets" which represent the normal stat across all users while the actual stats per VR Headset are relative to this totals number. As of September 2024 the total rows are included in the data (currently only relevant for VR Headsets), be careful when calculating sums across entire categories as the result might be misleading.

* Data from December 2024 (uploaded January 2025) did show larger inconsistencies as mentioned by [Devaniti](https://github.com/jdegene/steamHWsurvey/issues/6), where sums can add up to mathmatically incorrect >100%. The data remained as is throughout January (i.e. was not revised by Steam). The following February upload (of January 2025 data) seems to be correct again, and was changed around February 19th 2025 by Steam to account for correct changes in relation to December (e.g. the first entry for Windows 11 from beginning of February changed from  "-0.0150,0.5346" to "0.0034,0.5346" at that date). The current dataset contains the revised data from February 19th 2025 AND the recalculated values for December 2024 using the revised changes. For a pre-calculated version of December 2024 data see commit #7017769


## Official Information posted on the Steam Hardware Survey Site

STEAM HARDWARE SURVEY FIX – 5/2/2018

The latest Steam Hardware Survey incorporates a number of fixes that address over counting of cybercafé customers that occurred during the prior seven months.

Historically, the survey used a client-side method to ensure that systems were counted only once per year, in order to provide an accurate picture of the entire Steam user population. It turns out, however, that many cybercafés manage their hardware in a way that was causing their customers to be over counted.

Around August 2017, we started seeing larger-than-usual movement in certain stats, notably an increase in Windows 7 usage, an increase in quad-core CPU usage, as well as changes in CPU and GPU market share. This period also saw a large increase in the use of Simplified Chinese. All of these coincided with an increase in Steam usage in cybercafés in Asia, whose customers were being over counted in the survey.

It took us some time to root-cause the problem and deploy a fix, but we are confident that, as of April 2018, the Steam Hardware Survey is no longer over counting users. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
(2012-06)

Why do many of the Steam Hardware Survey numbers seem to undergo a significant change in April 2012?

There was a bug introduced into Steam's survey code several months ago that caused a bias toward older systems. Specifically, only systems that had run the survey prior to the introduction of the bug would be asked to run the survey again. This caused brand-new systems to never run the survey. In March 2012, we caught the bug, causing the survey to be run on a large number of new computers, thus giving us a more accurate survey and causing some of the numbers to vary more than they normally would month-to-month. Some of the most interesting changes revealed by this correction were the increased OS share of Windows 7 (as Vista fell below XP), the rise of Intel as a graphics provider and the overall diversification of Steam worldwide (as seen in the increase of non-English language usage, particularly Russian). 


# Graphs 

Graphs are auto-generated with every data update 


## GPUs 
```mermaid
---
config:
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"
--- 


xychart-beta
    title "NVIDIA xx90 cards in months after 'first seen'. All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0]
    line [0.22, 0.29, 0.32, 0.36, 0.36, 0.33999999999999997, 0.37, 0.36, 0.41000000000000003, 0.43, 0.44, 0.42, 0.42, 0.41000000000000003, 0.44, 0.44999999999999996, 0.51, 0.44999999999999996, 0.52, 0.48, 0.47000000000000003, 0.47000000000000003, 0.51, 0.49, 0.53, 0.5, 0.43, 0.49, 0.48, 0.51, 0.58, 0.59, 0.53, 0.48, 0.58, 0.58]
    line [0.22999999999999998, 0.3, 0.25, 0.42, 0.43, 0.54, 0.64, 0.76, 0.7100000000000001, 0.61, 0.88, 0.8699999999999999, 0.91, 0.88, 0.8500000000000001, 0.96, 0.9900000000000001, 0.9199999999999999, 0.8999999999999999, 0.96, 0.91, 1.17, 1.01, 0.96, 0.96, 0.7100000000000001, 0.91, 0.9400000000000001, 0.8999999999999999]
    line [0]
``` 
$${\color{#51a8a6}2090 \space\color{#f9a900}3090 \space\color{#f92800}4090 \space\color{#d92080}5090 \space}$$

```mermaid
---
config:
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"
--- 


xychart-beta
    title "NVIDIA xx80 cards in months after 'first seen'. All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.21, 0.3, 0.59, 0.7299999999999999, 0.8699999999999999, 0.9400000000000001, 1.1400000000000001, 1.1099999999999999, 1.31, 1.41, 1.4200000000000002, 1.71, 1.83, 2.04, 1.97, 2.25, 2.1999999999999997, 2.29, 2.4, 2.52, 2.64, 2.73, 2.6100000000000003, 2.5500000000000003, 3.19, 2.3800000000000003, 2.43, 2.4699999999999998, 2.4699999999999998, 2.45, 2.3899999999999997, 2.19, 2.23, 2.11, 2.06, 2.07]
    line [0.22, 0.44999999999999996, 0.63, 0.74, 0.8099999999999999, 0.8200000000000001, 0.86, 0.8099999999999999, 0.8500000000000001, 0.96, 1.21, 1.3, 1.4500000000000002, 1.45, 1.48, 1.55, 1.87, 1.94, 2.3, 2.18, 2.5700000000000003, 2.54, 2.54, 2.62, 2.74, 2.78, 2.78, 2.86, 3.18, 2.79, 2.78, 2.88, 3.16, 3.2199999999999998, 3.06, 3.25]
    line [0.19, 0.19, 0.27999999999999997, 0.32, 0.38999999999999996, 0.44999999999999996, 0.52, 0.51, 0.62, 0.67, 0.7100000000000001, 0.88, 0.75, 0.75, 1.16, 1.3, 1.27, 1.3, 1.4000000000000001, 1.44, 1.9299999999999997, 1.69, 1.7399999999999998, 1.7399999999999998, 1.8599999999999999, 1.67, 1.7599999999999998, 1.73]
    line [0.19, 0.37, 0.44999999999999996]
``` 
$${\color{#51a8a6}2080 \space\color{#f9a900}3080 \space\color{#f92800}4080 \space\color{#d92080}5080 \space}$$

```mermaid
---
config:
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"
--- 


xychart-beta
    title "NVIDIA xx70 cards in months after 'first seen'. All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.16, 0.32, 0.48, 0.63, 0.8099999999999999, 0.91, 1.06, 1.16, 1.34, 1.6199999999999999, 1.66, 2.02, 2.31, 2.45, 2.5, 3.0799999999999996, 2.9000000000000004, 3.06, 3.3100000000000005, 3.5900000000000003, 3.8599999999999994, 4.04, 3.8900000000000006, 4.21, 5.930000000000001, 4.180000000000001, 4.26, 4.38, 4.38, 4.35, 4.45, 4.07, 4.43, 3.91, 3.7900000000000005, 3.82]
    line [1.24, 1.3299999999999998, 1.4200000000000002, 1.67, 1.7599999999999998, 2.06, 2.2600000000000002, 2.3200000000000003, 2.55, 2.75, 2.7, 2.9099999999999997, 3.27, 3.29, 3.64, 3.5700000000000003, 4.1000000000000005, 4.24, 4.3999999999999995, 4.8500000000000005, 4.68, 4.930000000000001, 5.01, 5.41, 8.14, 5.42, 5.56, 5.5, 5.7700000000000005, 5.86, 6.18, 7.8, 5.83, 5.83, 5.7, 6.370000000000001]
    line [0.16999999999999998, 0.22999999999999998, 0.4, 0.65, 0.95, 1.1900000000000002, 1.68, 1.96, 3.1399999999999997, 2.53, 2.94, 3.06, 3.83, 4.199999999999999, 4.46, 4.97, 5.140000000000001, 5.65, 5.96, 6.67, 8.52, 6.93, 7.720000000000001, 7.720000000000001, 11.41, 7.199999999999999, 7.470000000000001, 7.16]
    line [0.63, 1.0499999999999998]
``` 
$${\color{#51a8a6}2070 \space\color{#f9a900}3070 \space\color{#f92800}4070 \space\color{#d92080}5070 \space}$$

```mermaid
---
config:
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"
--- 


xychart-beta
    title "NVIDIA xx60 cards in months after 'first seen'. All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.26, 0.51, 0.65, 0.8200000000000001, 0.9900000000000001, 1.23, 1.48, 1.6900000000000002, 2.1999999999999997, 2.63, 2.6, 2.66, 3.3099999999999996, 2.9200000000000004, 3.0400000000000005, 3.36, 3.52, 3.9699999999999998, 4.19, 4.34, 4.77, 6.9, 5.01, 5.24, 6.29, 6.35, 6.220000000000001, 7.199999999999999, 6.67, 8.020000000000001, 6.69, 6.24, 6.43, 6.659999999999999, 6.140000000000001, 6.35]
    line [0.25, 0.33, 0.36, 0.54, 0.8500000000000001, 1.38, 1.7000000000000002, 2.53, 2.9899999999999998, 3.2399999999999998, 3.9600000000000004, 4.7299999999999995, 4.760000000000001, 5.38, 6.039999999999999, 6.18, 6.529999999999999, 7.089999999999999, 7.62, 8.32, 9.3, 11.01, 9.94, 10.11, 10.43, 11.64, 18.42, 11.89, 12.33, 12.06, 11.649999999999999, 12.32, 13.750000000000002, 17.19, 12.129999999999999, 11.899999999999999]
    line [0.22999999999999998, 0.3, 0.79, 1.1199999999999999, 2.16, 2.87, 4.5200000000000005, 3.9900000000000007, 4.06, 4.87, 6.16, 6.800000000000001, 7.090000000000001, 7.71, 8.76, 9.22, 10.530000000000001, 12.229999999999999, 14.629999999999999, 11.530000000000001, 12.2, 12.25, 18.39, 11.959999999999999, 12.28, 11.690000000000001]
    line [0.2]
``` 
$${\color{#51a8a6}2060 \space\color{#f9a900}3060 \space\color{#f92800}4060 \space\color{#d92080}5060 \space}$$

