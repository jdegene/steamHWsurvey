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
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#76b900,#ED1C24,#0071C5,#808080"

--- 

xychart-beta
    title "Average annual marketshares by manufacturer and year"
    x-axis [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    y-axis "Ø %" 
    line [56.48, 56.763333333333335, 50.07625, 47.84571428571429, 37.81375, 35.39000000000001, 39.059, 45.67400000000001, 50.03636363636363, 62.983999999999995, 70.6925, 68.25333333333333, 68.15416666666665, 69.88333333333333, 71.41666666666667, 71.76, 74.17666666666666, 71.792]
    line [19.93, 20.3875, 23.07, 25.19, 21.881249999999998, 16.706666666666667, 16.323999999999998, 21.631999999999998, 18.71, 6.939999999999999, 8.461666666666668, 9.675833333333333, 11.463333333333333, 11.3575, 10.354999999999999, 10.59, 12.410833333333333, 12.65]
    line [3.2, 2.75, 3.09625, 2.145714285714286, 9.1675, 12.888333333333332, 17.224999999999998, 13.13, 17.69909090909091, 7.8375, 9.230833333333333, 10.240833333333333, 9.756666666666668, 6.418333333333333, 4.340833333333333, 3.480833333333334, 4.300000000000001, 3.3940000000000006]
    line [20.39, 20.301666666666666, 23.971249999999998, 24.98, 39.86875, 53.145714285714284, 41.85272727272727, 49.48444444444444, 13.566363636363635, 25.19, 11.603333333333333, 11.834999999999999, 10.618333333333334, 12.334166666666667, 13.880833333333333, 14.175833333333335, 12.324166666666665, 12.148]
``` 
$${\color{#76b900}NIVIDA\space\space\space
\color{#ED1C24}AMD\space\space\space
\color{#0071C5}Intel\space\space\space
\color{#808080}Other\space\space\space}$$

<br/>

### NVIDIA Generation Comparison

Compare GPUs across Generations, first month a GPU appears in Steam Hardware Survey = month 0.
Combines all variants, eg. 4060, 4060 Laptop GPU, 4060 Ti are all grouped in 4060.

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "NVIDIA xx90 cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0]
    line [0]
    line [0.22, 0.29, 0.32, 0.36, 0.36, 0.33999999999999997, 0.37, 0.36, 0.41000000000000003, 0.43, 0.44, 0.42, 0.42, 0.41000000000000003, 0.44, 0.44999999999999996, 0.51, 0.44999999999999996, 0.52, 0.48, 0.47000000000000003, 0.47000000000000003, 0.51, 0.49, 0.53, 0.5, 0.43, 0.49, 0.48, 0.51, 0.58, 0.59, 0.53, 0.48, 0.58, 0.58]
    line [0.22999999999999998, 0.3, 0.25, 0.42, 0.43, 0.54, 0.64, 0.76, 0.7100000000000001, 0.61, 0.88, 0.8699999999999999, 0.91, 0.88, 0.8500000000000001, 0.96, 0.9900000000000001, 0.9199999999999999, 0.8999999999999999, 0.96, 0.91, 1.17, 1.01, 0.96, 0.96, 0.7100000000000001, 0.91, 0.9400000000000001, 0.8999999999999999]
    line [0]
``` 
$${\color{#51a8a6}---\space(--)\space\space\space\color{#f9a900}---\space(--)\space\space\space\color{#f92800}3090\space(Jan \space 2021)\space\space\space\color{#d92080}4090\space(Jan \space 2023)\space\space\space\color{#8a52a6}5090\space(--)\space\space\space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "NVIDIA xx80 cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.27999999999999997, 0.47000000000000003, 0.72, 0.83, 0.95, 2.17, 1.32, 1.1400000000000001, 1.2799999999999998, 1.26, 1.5099999999999998, 2.23, 3.29, 3.46, 3.5900000000000003, 3.42, 4.17, 4.180000000000001, 4.14, 4.5, 4.37, 4.33, 4.31, 4.45, 4.42, 4.470000000000001, 4.58, 4.130000000000001, 4.45, 4.36, 4.14, 4.24, 4.21, 4.38, 3.95, 4.01]
    line [0.21, 0.3, 0.59, 0.7299999999999999, 0.8699999999999999, 0.9400000000000001, 1.1400000000000001, 1.1099999999999999, 1.31, 1.41, 1.4200000000000002, 1.71, 1.83, 2.04, 1.97, 2.25, 2.1999999999999997, 2.29, 2.4, 2.52, 2.64, 2.73, 2.6100000000000003, 2.5500000000000003, 3.19, 2.3800000000000003, 2.43, 2.4699999999999998, 2.4699999999999998, 2.45, 2.3899999999999997, 2.19, 2.23, 2.11, 2.06, 2.07]
    line [0.22, 0.44999999999999996, 0.63, 0.74, 0.8099999999999999, 0.8200000000000001, 0.86, 0.8099999999999999, 0.8500000000000001, 0.96, 1.21, 1.3, 1.4500000000000002, 1.45, 1.48, 1.55, 1.87, 1.94, 2.3, 2.18, 2.5700000000000003, 2.54, 2.54, 2.62, 2.74, 2.78, 2.78, 2.86, 3.18, 2.79, 2.78, 2.88, 3.16, 3.2199999999999998, 3.06, 3.25]
    line [0.19, 0.19, 0.27999999999999997, 0.32, 0.38999999999999996, 0.44999999999999996, 0.52, 0.51, 0.62, 0.67, 0.7100000000000001, 0.88, 0.75, 0.75, 1.16, 1.3, 1.27, 1.3, 1.4000000000000001, 1.44, 1.9299999999999997, 1.69, 1.7399999999999998, 1.7399999999999998, 1.8599999999999999, 1.67, 1.7599999999999998, 1.73]
    line [0.19, 0.37, 0.44999999999999996]
``` 
$${\color{#51a8a6}1080\space(Jul \space 2016)\space\space\space\color{#f9a900}2080\space(Dec \space 2018)\space\space\space\color{#f92800}3080\space(Nov \space 2020)\space\space\space\color{#d92080}4080\space(Feb \space 2023)\space\space\space\color{#8a52a6}5080\space(Mar \space 2025)\space\space\space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "NVIDIA xx70 cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.32, 0.6799999999999999, 1.25, 1.53, 1.82, 3.18, 1.78, 1.55, 1.69, 1.82, 2.04, 2.84, 3.95, 4.17, 4.2299999999999995, 4.16, 4.77, 4.88, 4.67, 5.26, 5.119999999999999, 5.36, 5.489999999999999, 5.74, 5.66, 5.7700000000000005, 5.74, 5.51, 5.79, 5.6899999999999995, 5.56, 5.53, 5.4399999999999995, 5.6000000000000005, 5.140000000000001, 5.26]
    line [0.16, 0.32, 0.48, 0.63, 0.8099999999999999, 0.91, 1.06, 1.16, 1.34, 1.6199999999999999, 1.66, 2.02, 2.31, 2.45, 2.5, 3.0799999999999996, 2.9000000000000004, 3.06, 3.3100000000000005, 3.5900000000000003, 3.8599999999999994, 4.04, 3.8900000000000006, 4.21, 5.930000000000001, 4.180000000000001, 4.26, 4.38, 4.38, 4.35, 4.45, 4.07, 4.43, 3.91, 3.7900000000000005, 3.82]
    line [1.24, 1.3299999999999998, 1.4200000000000002, 1.67, 1.7599999999999998, 2.06, 2.2600000000000002, 2.3200000000000003, 2.55, 2.75, 2.7, 2.9099999999999997, 3.27, 3.29, 3.64, 3.5700000000000003, 4.1000000000000005, 4.24, 4.3999999999999995, 4.8500000000000005, 4.68, 4.930000000000001, 5.01, 5.41, 8.14, 5.42, 5.56, 5.5, 5.7700000000000005, 5.86, 6.18, 7.8, 5.83, 5.83, 5.7, 6.370000000000001]
    line [0.16999999999999998, 0.22999999999999998, 0.4, 0.65, 0.95, 1.1900000000000002, 1.68, 1.96, 3.1399999999999997, 2.53, 2.94, 3.06, 3.83, 4.199999999999999, 4.46, 4.97, 5.140000000000001, 5.65, 5.96, 6.67, 8.52, 6.93, 7.720000000000001, 7.720000000000001, 11.41, 7.199999999999999, 7.470000000000001, 7.16]
    line [0.63, 1.0499999999999998]
``` 
$${\color{#51a8a6}1070\space(Jul \space 2016)\space\space\space\color{#f9a900}2070\space(Dec \space 2018)\space\space\space\color{#f92800}3070\space(Mar \space 2021)\space\space\space\color{#d92080}4070\space(Feb \space 2023)\space\space\space\color{#8a52a6}5070\space(Apr \space 2025)\space\space\space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "NVIDIA xx60 cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.24, 0.9900000000000001, 1.47, 2.01, 6.3, 7.470000000000001, 11.29, 13.200000000000001, 14.610000000000001, 15.409999999999998, 14.05, 13.62, 11.88, 11.89, 12.33, 12.5, 13.309999999999999, 13.81, 14.299999999999999, 14.06, 14.799999999999999, 14.31, 15.310000000000002, 14.99, 15.690000000000001, 15.690000000000001, 15.5, 14.829999999999998, 14.42, 14.01, 14.44, 14.64, 15.790000000000001, 13.03, 12.23, 12.13]
    line [0.26, 0.51, 0.65, 0.8200000000000001, 0.9900000000000001, 1.23, 1.48, 1.6900000000000002, 2.1999999999999997, 2.63, 2.6, 2.66, 3.3099999999999996, 2.9200000000000004, 3.0400000000000005, 3.36, 3.52, 3.9699999999999998, 4.19, 4.34, 4.77, 6.9, 5.01, 5.24, 6.29, 6.35, 6.220000000000001, 7.199999999999999, 6.67, 8.020000000000001, 6.69, 6.24, 6.43, 6.659999999999999, 6.140000000000001, 6.35]
    line [0.25, 0.33, 0.36, 0.54, 0.8500000000000001, 1.38, 1.7000000000000002, 2.53, 2.9899999999999998, 3.2399999999999998, 3.9600000000000004, 4.7299999999999995, 4.760000000000001, 5.38, 6.039999999999999, 6.18, 6.529999999999999, 7.089999999999999, 7.62, 8.32, 9.3, 11.01, 9.94, 10.11, 10.43, 11.64, 18.42, 11.89, 12.33, 12.06, 11.649999999999999, 12.32, 13.750000000000002, 17.19, 12.129999999999999, 11.899999999999999]
    line [0.22999999999999998, 0.3, 0.79, 1.1199999999999999, 2.16, 2.87, 4.5200000000000005, 3.9900000000000007, 4.06, 4.87, 6.16, 6.800000000000001, 7.090000000000001, 7.71, 8.76, 9.22, 10.530000000000001, 12.229999999999999, 14.629999999999999, 11.530000000000001, 12.2, 12.25, 18.39, 11.959999999999999, 12.28, 11.690000000000001]
    line [0.2]
``` 
$${\color{#51a8a6}1060\space(Aug \space 2016)\space\space\space\color{#f9a900}2060\space(Mar \space 2019)\space\space\space\color{#f92800}3060\space(Jan \space 2021)\space\space\space\color{#d92080}4060\space(Apr \space 2023)\space\space\space\color{#8a52a6}5060\space(May \space 2025)\space\space\space}$$

<br/>

### AMD Generation Comparison

Compare GPUs across Generations, first month a GPU appears in Steam Hardware Survey = month 0.
Grouping is a bit less straight forward than with NVIDIA cards because of the naming shifts

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "AMD High-End cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0]
    line [0.15, 0.18, 0.16, 0.38, 0.33, 0.34, 0.33, 0.38999999999999996, 0.4, 0.42000000000000004, 0.43, 0.43, 0.43, 0.4699999999999999, 0.54, 0.5599999999999999, 0.53, 0.4099999999999999, 0.74, 0.72, 0.74, 0.68, 0.64, 0.73, 0.77, 0.71, 0.68, 0.69, 0.67, 1.03, 0.73, 0.8699999999999999, 0.7100000000000001, 0.37, 0.7299999999999999, 0.7100000000000001]
    line [0.16999999999999998, 0.22, 0.22, 0.19, 0.31, 0.32, 0.33999999999999997, 0.33999999999999997, 0.35000000000000003, 0.38999999999999996, 0.41000000000000003, 0.38, 0.37, 0.4, 0.37, 0.5, 0.44, 0.44, 0.44, 0.35000000000000003, 0.51, 0.53, 0.52]
    line [0]
``` 
$${\color{#51a8a6}---\space(---)\space\space\space\color{#f9a900}6800|6900|6950\space(Apr \space 2022)\space\space\space\color{#f92800}7900\space(Jul \space 2023)\space\space\space\color{#d92080}9090\space(---)\space\space\space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "AMD Upper-Midrange cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.15, 0.22, 0.26, 0.5900000000000001, 0.63, 0.7000000000000001, 0.8, 0.8699999999999999, 0.97, 1.04, 1.1199999999999999, 1.21, 1.17, 1.18, 1.06, 1.27, 1.25, 1.23, 1.1900000000000002, 1.17, 0.98, 0.98, 0.8500000000000001, 0.95, 0.9600000000000001, 0.93, 0.88, 0.88, 0.7000000000000001, 0.7100000000000001, 0.72, 0.9400000000000001, 0.6799999999999999, 0.9500000000000002, 0.67, 0.63]
    line [0.16, 0.16999999999999998, 0.19, 0.19, 0.2, 0.21, 0.22, 0.24, 0.27, 0.26, 0.32, 0.3, 0.31, 0.31, 0.37, 0.4, 0.44999999999999996, 0.45999999999999996, 0.35000000000000003, 0.51, 0.51, 0.74, 0.8099999999999999, 0.8999999999999999, 0.8500000000000001, 0.7299999999999999, 1.03, 1.05, 1.06, 0.97, 0.95, 1.05, 1.09, 1.17, 1.1300000000000001, 1.22]
    line [0.27, 0.35000000000000003]
    line [0]
``` 
$${\color{#51a8a6}5700\space(Oct \space 2019)\space\space\space\color{#f9a900}6700|6750\space(Sep \space 2021)\space\space\space\color{#f92800}7800\space(Apr \space 2025)\space\space\space\color{#d92080}9080\space(---)\space\space\space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "AMD Midrange cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.18, 0.19, 0.22, 0.22, 0.32, 0.32, 0.33999999999999997, 0.33, 0.33999999999999997, 0.29, 0.29, 0.25, 0.27, 0.27999999999999997, 0.27, 0.25, 0.24, 0.24, 0.24, 0.22999999999999998, 0.25, 0.22999999999999998, 0.26, 0.21, 0.2, 0.19, 0.22, 0.21, 0.21, 0.22, 0.16, 0.22999999999999998, 0.22999999999999998, 0.22999999999999998, 0.24, 0.24]
    line [0.3, 0.5, 0.53, 0.62, 0.62, 0.66, 0.61, 0.73, 0.75, 0.79, 0.8099999999999999, 0.66, 1.03, 1.04, 1.09, 1.15, 1.22, 1.1900000000000002, 0.95, 1.34, 1.3299999999999998, 1.39, 1.31, 1.29, 1.44, 1.52, 1.4200000000000002, 1.38, 1.4200000000000002, 1.37, 1.82, 1.51, 1.5, 1.5, 1.16, 1.5599999999999998]
    line [0.16, 0.16, 0.19, 0.19, 0.16, 0.21, 0.25, 0.24]
    line [0]
``` 
$${\color{#51a8a6}5600\space(Sep \space 2020)\space\space\space\color{#f9a900}6600|6650\space(Apr \space 2022)\space\space\space\color{#f92800}7700\space(Oct \space 2024)\space\space\space\color{#d92080}9070\space(---)\space\space\space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

--- 


xychart-beta
    title "AMD Midrange cards in months after (first seen). All variants."
    x-axis[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    y-axis "%" 
    line [0.16, 0.19, 0.2, 0.29, 0.32, 0.33999999999999997, 0.33999999999999997, 0.36, 0.31, 0.3, 0.27, 0.29, 0.3, 0.29, 0.44, 0.45000000000000007, 0.45000000000000007, 0.42, 0.43999999999999995, 0.44, 0.42, 0.29, 0.4, 0.37, 0.2, 0.22, 0.22, 0.38000000000000006, 0.22, 0.16, 0.22, 0.22, 0.21, 0.22, 0.21, 0.19]
    line [0.16999999999999998, 0.16999999999999998, 0.18, 0.19, 0.2, 0.21, 0.21, 0.22, 0.2, 0.2, 0.19, 0.19, 0.19, 0.19, 0.18, 0.16999999999999998, 0.2, 0.19, 0.19, 0.18, 0.19, 0.18, 0.22, 0.19, 0.19, 0.19, 0.19, 0.2, 0.19]
    line [0]
    line [0]
``` 
$${\color{#51a8a6}5500\space(Oct \space 2020)\space\space\space\color{#f9a900}6400|6500\space(Sep \space 2022)\space\space\space\color{#f92800}7600|7650\space(---)\space\space\space\color{#d92080}9060\space(---)\space\space\space}$$

<br/>


## Resolution 
```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6"

--- 

xychart-beta
    title "Primary Display: aspect ratio changes (weighted by percentage)"
    x-axis [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    y-axis "Ø %" 
    line [1.417941306228879, 1.4611567835141763, 1.533974920001756, 1.5813610553330728, 1.6441197983994256, 1.6789673069298932, 1.6979525680775114, 1.7118873828122096, 1.7229454013771042, 1.7476951638068883, 1.7618596685661352, 1.765595772113996, 1.7737831941811184, 1.7794489740395185, 1.7798889098601134, 1.7814503174534728, 1.784019854809584, 1.7849837780465507]
``` 
$${\color{#51a8a6} For \space reference \space 1920*1080 \space ratio \space = \space 1.77 \space pixels \space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6"

--- 

xychart-beta
    title "Primary Display: number of pixels on screen (weighted by percentage)"
    x-axis [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    y-axis "Ø %" 
    line [1188430.8928, 1288926.3533333333, 1387816.4456, 1487587.5584, 1541658.4541874998, 1555539.6754714285, 1549496.4588272728, 1559351.2310333333, 1557359.9222666668, 1788536.702933333, 1951604.4634666666, 2014008.6962666668, 2119798.684, 2216151.314933333, 2307369.4647999997, 2473576.992, 2673738.5261333333, 2760045.62816]
``` 
$${\color{#51a8a6} For \space reference \space 1920*1080 \space = \space 2.073.600 \space pixels \space}$$

<br/>

```mermaid
---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#f9a900"

--- 

xychart-beta
    title "Multi-Monitor: number of pixels on screens (weighted by percentage)"
    x-axis [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    y-axis "Ø %" 
    line [2319909.5456, 2509416.3005333333, 2798777.9104, 2867947.6621714286, 3563643.0461, 3616471.1752, 3474378.030618182, 3537545.9458333333, 3281757.5182666667, 3441108.7957666665, 5179962.898033333, 7688149.9864, 7739759.53, 7992133.524266667, 8231354.020799999, 8598812.918666666, 9028144.557333333, 9222842.2144]
``` 
$${\color{#f9a900} For \space reference \space 2x \space 1920*1080 \space = \space 4.147.200 \space pixels \space}$$

<br/>

