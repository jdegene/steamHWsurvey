# -*- coding: utf-8 -*-
# Creates a readme file and stats/graphs from current files. Overwrites existing README.md

import os
import pandas as pd

# %% 0 - Define manual first part of the readme

readme_content = """# Files Description
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

"""

# %% 1 - Load Data & Prep
df = pd.read_csv("shs.csv", encoding="utf8")
df_platform = pd.read_csv("shs_platform.csv", encoding="utf8")

df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
df_platform["date"] = pd.to_datetime(df_platform["date"], format="%Y-%m-%d")

df["name"] = df["name"].fillna("")
df_platform["name"] = df_platform["name"].fillna("")
df["category"] = df["category"].fillna("")
df_platform["category"] = df_platform["category"].fillna("")

df = df.sort_values("date")
df_platform = df_platform.sort_values("date")


# %% 2 - Prepare recurring string parts
readme_content = (
    readme_content
    + """\n# Graphs \n
Graphs are auto-generated with every data update \n
"""
)

# colors_list = ["#CB7876", "#62866C", "#32769B", "#64557B", "#F67B45"]
colors_list = ["#51a8a6", "#f9a900", "#f92800", "#d92080", "#8a52a6"]
config_str = f"""---
config:
    themeVariables:
        xyChart:
            plotColorPalette: "{','.join(colors_list)}"
--- 
"""

# %% 3 - Add stats

# ---------------------------------------------------------------------------------------------
# 3.1 GPU stats
# ---------------------------------------------------------------------------------------------
readme_content = readme_content + "\n## GPUs \n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.1 NVIDIA xx90s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx90 cards in months after 'first seen'. All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values
gpu_list = ["2090", "3090", "4090", "5090"]
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("nvidia"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = legend_str + "\color{" + colors_list[i] + "}" + gpu + " \space"
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n - - - \n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.2 NVIDIA xx80s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx80 cards in months after 'first seen'. All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values
gpu_list = ["2080", "3080", "4080", "5080"]
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("nvidia"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = legend_str + "\color{" + colors_list[i] + "}" + gpu + " \space"
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n - - - \n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.3 NVIDIA xx70s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx70 cards in months after 'first seen'. All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values
gpu_list = ["2070", "3070", "4070", "5070"]
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("nvidia"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = legend_str + "\color{" + colors_list[i] + "}" + gpu + " \space"
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n - - - \n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.4 NVIDIA xx60s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx60 cards in months after 'first seen'. All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values
gpu_list = ["2060", "3060", "4060", "5060"]
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("nvidia"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = legend_str + "\color{" + colors_list[i] + "}" + gpu + " \space"
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n - - - \n"


# %% 4 - Save to File
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
