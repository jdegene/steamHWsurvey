# -*- coding: utf-8 -*-
# Creates a readme file and stats/graphs from current files. Overwrites existing README.md

import os
import numpy as np
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
Graphs are auto-generated with every data update. See create_readme.py for details. 
This is raw data, expect some weirdness ;) \n
"""
)


# %% 3 - Add stats

# ---------------------------------------------------------------------------------------------
# %% 3.1 GPU stats
# ---------------------------------------------------------------------------------------------
readme_content = readme_content + "\n## GPUs \n"

# colors_list = ["#CB7876", "#62866C", "#32769B", "#64557B", "#F67B45"]
colors_list = ["#51a8a6", "#f9a900", "#f92800", "#d92080", "#8a52a6"]
gpu_config_str = f"""---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "{','.join(colors_list)}"

--- 
"""

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.0 Annual Stats - Get average market share per manufacturer and year
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

annual_gpu_df = df[df["category"] == "Video Card Description"].copy()
annual_gpu_df["type"] = "Other"
annual_gpu_df["type"] = np.where(
    annual_gpu_df["name"].str.lower().str.contains("nvidia"), "NVIDIA", annual_gpu_df["type"]
)
annual_gpu_df["type"] = np.where(
    annual_gpu_df["name"].str.lower().str.contains("amd |ati "), "AMD", annual_gpu_df["type"]
)
annual_gpu_df["type"] = np.where(
    annual_gpu_df["name"].str.lower().str.contains("intel "), "Intel", annual_gpu_df["type"]
)

# sum up percentages per day, then return average percentages per year
annual_gpu_grp_df = annual_gpu_df.groupby(["date", "type"])["percentage"].sum().reset_index()
annual_gpu_grp_df["year"] = annual_gpu_grp_df["date"].dt.year
annual_gpu_grp_df = (
    annual_gpu_grp_df.groupby(["year", "type"])["percentage"].mean().reset_index()
)

### add title and x-axis & y-axis info. Use official venfor colors
cur_stats_txt = (
    "```mermaid\n"
    + """---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#76b900,#ED1C24,#0071C5,#808080"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "Average annual marketshares by manufacturer and year"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([int(i) for i in annual_gpu_grp_df["year"].unique()])
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "Ø %" \n'

manuf_list = ["NVIDIA", "AMD", "Intel", "Other"]
for manu in manuf_list:
    manu_stats_df = annual_gpu_grp_df[annual_gpu_grp_df["type"] == manu].copy()

    manu_stats_df["percentage"] = manu_stats_df["percentage"] * 100
    manu_stats_list = (
        manu_stats_df["percentage"].to_list()
        if len(manu_stats_df["percentage"].to_list()) > 0
        else [0]
    )
    cur_stats_txt = cur_stats_txt + "    line " + str(manu_stats_list) + "\n"

legend_str = """$${\color{#76b900}NIVIDA\space\space\space
\color{#ED1C24}AMD\space\space\space
\color{#0071C5}Intel\space\space\space
\color{#808080}Other\space\space\space}$$"""

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.1 NVIDIA xx90s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

readme_content = (
    readme_content
    + """### NVIDIA Generation Comparison

Compare GPUs across Generations, first month a GPU appears in Steam Hardware Survey = month 0.
Combines all variants, eg. 4060, 4060 Laptop GPU, 4060 Ti are all grouped in 4060.\n
"""
)

num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx90 cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values and extract date when card was first seen
gpu_list = ["---", "---", "3090", "4090", "5090"]
first_seen_month_list = []
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
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("--")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.2 NVIDIA xx80s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx80 cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values and extract date when card was first seen
gpu_list = ["1080", "2080", "3080", "4080", "5080"]
first_seen_month_list = []
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
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("---")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.3 NVIDIA xx70s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### calculate actual line values and extract date when card was first seen
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx70 cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values
gpu_list = ["1070", "2070", "3070", "4070", "5070"]
first_seen_month_list = []
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
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("---")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.4 NVIDIA xx60s market penetration in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "NVIDIA xx60 cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values and extract date when card was first seen
gpu_list = ["1060", "2060", "3060", "4060", "5060"]
first_seen_month_list = []
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
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("---")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.5 AMD high-end cards in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

readme_content = (
    readme_content
    + """### AMD Generation Comparison

Compare GPUs across Generations, first month a GPU appears in Steam Hardware Survey = month 0.
Grouping is a bit less straight forward than with NVIDIA cards because of the naming shifts\n
"""
)

num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "AMD High-End cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values and extract date when card was first seen
gpu_list = ["---", "6800|6900|6950", "7900", "9090"]
first_seen_month_list = []
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("amd radeon rx"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("---")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.6 AMD upper-midrange cards in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "AMD Upper-Midrange cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values and extract date when card was first seen
gpu_list = ["5700", "6700|6750", "7800", "9080"]
first_seen_month_list = []
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("amd radeon rx"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("---")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.7 AMD midrange cards in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "AMD Midrange cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values and extract date when card was first seen
gpu_list = ["5600", "6600|6650", "7700", "9070"]
first_seen_month_list = []
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("amd radeon rx"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("---")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.1.8 AMD entry-level cards in months after "first seen month". Adds all variants together
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
num_months = 36

### add title and x-axis & y-axis info
cur_stats_txt = "```mermaid\n" + gpu_config_str + "\n"
cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "AMD Midrange cards in months after (first seen). All variants."
"""
)
cur_stats_txt = cur_stats_txt + "    x-axis" + str([i for i in range(num_months)]) + "\n"
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

### calculate actual line values and extract date when card was first seen
gpu_list = ["5500", "6400|6500", "7600|7650", "9060"]
first_seen_month_list = []
for gpu in gpu_list:
    gpu_stats_df = (
        df[
            (df["category"] == "Video Card Description")
            & (df["name"].str.contains(gpu))
            & (df["name"].str.lower().str.contains("amd radeon rx"))
        ]
        .groupby("date")["percentage"]
        .sum()
        .iloc[:num_months]
    )
    try:
        first_seen_month_list.append(gpu_stats_df.index[0].strftime("%b \space %Y"))
    except:
        first_seen_month_list.append("---")
    gpu_stats_df = gpu_stats_df * 100
    gpu_stats_list = gpu_stats_df.to_list() if len(gpu_stats_df.to_list()) > 0 else [0]
    cur_stats_txt = cur_stats_txt + "    line " + str(gpu_stats_list) + "\n"

# Format and add legend as LATEX code to allow for coloring
legend_str = "$${"
for i, gpu in enumerate(gpu_list):
    legend_str = (
        legend_str
        + "\color{"
        + colors_list[i]
        + "}"
        + gpu
        + f"\space({first_seen_month_list[i]})"
        + "\space\space\space"
    )
legend_str = legend_str + "}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


# ---------------------------------------------------------------------------------------------
# %% 3.2 OS stats
# ---------------------------------------------------------------------------------------------
readme_content = readme_content + "\n## OS \n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.2.1 Windows
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

readme_content = readme_content + """### Windows \n"""

pc_df = df_platform[
    (df_platform["platform"] == "pc") & (df_platform["category"] == "Windows Version")
].copy()
pc_df["Windows"] = "Other"

pc_df["Windows"] = np.where(
    pc_df["name"].str.lower().str.contains("windows 7"), "Win 7", pc_df["Windows"]
)
pc_df["Windows"] = np.where(
    pc_df["name"].str.lower().str.contains("windows 8"), "Win 8", pc_df["Windows"]
)
pc_df["Windows"] = np.where(
    pc_df["name"].str.lower().str.contains("windows 10"), "Win 10", pc_df["Windows"]
)
pc_df["Windows"] = np.where(
    pc_df["name"].str.lower().str.contains("windows 11"), "Win 11", pc_df["Windows"]
)


# get only last 9 years or x-axis will not fit all labels
pc_df = pc_df[pc_df["date"].dt.year >= (pc_df["date"].max().year - 9)]

pc_grp_df = pc_df.groupby(["date", "Windows"])["percentage"].sum().reset_index()

pc_grp_df["quarter"] = pc_grp_df["date"].dt.to_period("Q").astype(str).str.slice(2, 6)
pc_grp_quarter_df = (
    pc_grp_df.groupby(["quarter", "Windows"])["percentage"].mean().reset_index()
)

### add title and x-axis & y-axis info
cur_stats_txt = (
    "```mermaid\n"
    + """---
config:
    xyChart:
        width: 1400
        height: 700
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#808080"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "pc -- Windows Versions"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([i for i in pc_grp_quarter_df["quarter"].unique()]).replace("'", "")
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'


for ops in ["Win 7", "Win 8", "Win 10", "Win 11", "Other"]:
    os_stats_df = pc_grp_quarter_df[pc_grp_quarter_df["Windows"] == ops].copy()
    os_stats_df["percentage"] = os_stats_df["percentage"] * 100

    # ensure all years have values
    os_stats_list = []
    for q in pc_grp_quarter_df["quarter"].unique():
        os_q_df = os_stats_df[os_stats_df["quarter"] == q]
        if len(os_q_df) > 0:
            os_value = float(os_q_df["percentage"].values[0])
        else:
            os_value = 0
        os_stats_list.append(os_value)

    cur_stats_txt = cur_stats_txt + "    line " + str(os_stats_list) + "\n"

legend_str = """$${\color{#51a8a6}Win 7\space\space\space
\color{#f9a900}Win 8\space\space\space
\color{#f92800}Win 10\space\space\space
\color{#d92080}Win 11\space\space\space
\color{#808080}Other\space\space\space}$$"""

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.2.2 Linux
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

readme_content = readme_content + """### Linux \n"""

linux_df = df_platform[
    (df_platform["platform"] == "linux") & (df_platform["category"] == "Linux Version")
].copy()
linux_df["Linux"] = "Other"

linux_df["Linux"] = np.where(
    linux_df["name"].str.lower().str.contains("steamos"), "SteamOS", linux_df["Linux"]
)
linux_df["Linux"] = np.where(
    linux_df["name"].str.lower().str.contains("arch"), "Arch", linux_df["Linux"]
)
linux_df["Linux"] = np.where(
    linux_df["name"].str.lower().str.contains("mint"), "Mint", linux_df["Linux"]
)
linux_df["Linux"] = np.where(
    linux_df["name"].str.lower().str.contains("ubuntu"), "Ubuntu", linux_df["Linux"]
)
linux_df["Linux"] = np.where(
    linux_df["name"].str.lower().str.contains("manjaro"), "Manjaro", linux_df["Linux"]
)
linux_df["Linux"] = np.where(
    linux_df["name"].str.lower().str.contains("pop!"), "Pop!_OS", linux_df["Linux"]
)
linux_df["Linux"] = np.where(
    linux_df["name"].str.lower().str.contains("debian"), "Debian", linux_df["Linux"]
)


# get only last 9 years or x-axis will not fit all labels
linux_df = linux_df[linux_df["date"].dt.year >= (linux_df["date"].max().year - 9)]

linux_grp_df = linux_df.groupby(["date", "Linux"])["percentage"].sum().reset_index()

linux_grp_df["quarter"] = linux_grp_df["date"].dt.to_period("Q").astype(str).str.slice(2, 6)
linux_grp_quarter_df = (
    linux_grp_df.groupby(["quarter", "Linux"])["percentage"].mean().reset_index()
)

### add title and x-axis & y-axis info
cur_stats_txt = (
    "```mermaid\n"
    + """---
config:
    xyChart:
        width: 1400
        height: 700
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6,#46a2da,#32CD32,#808080"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "linux -- Linux Distros"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([i for i in linux_grp_quarter_df["quarter"].unique()]).replace("'", "")
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'


for ops in ["SteamOS", "Arch", "Mint", "Ubuntu", "Manjaro", "Pop!_OS", "Debian", "Other"]:
    os_stats_df = linux_grp_quarter_df[linux_grp_quarter_df["Linux"] == ops].copy()
    os_stats_df["percentage"] = os_stats_df["percentage"] * 100

    # ensure all years have values
    os_stats_list = []
    for q in linux_grp_quarter_df["quarter"].unique():
        os_q_df = os_stats_df[os_stats_df["quarter"] == q]
        if len(os_q_df) > 0:
            os_value = float(os_q_df["percentage"].values[0])
        else:
            os_value = 0
        os_stats_list.append(os_value)

    cur_stats_txt = cur_stats_txt + "    line " + str(os_stats_list) + "\n"

legend_str = """$${\color{#51a8a6}SteamOS\space\space\space
\color{#f9a900}Arch\space\space\space
\color{#f92800}Mint\space\space\space
\color{#d92080}Ubuntu\space\space\space
\color{#8a52a6}Manjaro\space\space\space
\color{#46a2da}Pop!_OS\space\space\space
\color{#32CD32}Debian\space\space\space
\color{#808080}Other\space\space\space}$$"""

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.2.3 Mac
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

readme_content = readme_content + """### Mac OSX \n"""

min_version = 10
max_version = 15

mac_df = df_platform[
    (df_platform["platform"] == "mac") & (df_platform["category"] == "OSX Version")
].copy()

mac_df["OSX"] = "Other"
for v in range(min_version, max_version + 1):
    mac_df["OSX"] = np.where(
        mac_df["name"].str.lower().str.startswith(f"macos {v}"), f"{v}", mac_df["OSX"]
    )

# get only last 9 years or x-axis will not fit all labels
mac_df = mac_df[mac_df["date"].dt.year >= (mac_df["date"].max().year - 9)]

mac_grp_df = mac_df.groupby(["date", "OSX"])["percentage"].sum().reset_index()

mac_grp_df["quarter"] = mac_grp_df["date"].dt.to_period("Q").astype(str).str.slice(2, 6)
mac_grp_quarter_df = mac_grp_df.groupby(["quarter", "OSX"])["percentage"].mean().reset_index()


### add title and x-axis & y-axis info
osx_color_palette = [
    "#51a8a6",
    "#f9a900",
    "#f92800",
    "#d92080",
    "#8a52a6",
    "#46a2da",
    "#808080",
]
cur_stats_txt = (
    "```mermaid\n"
    + f"""---
config:
    xyChart:
        width: 1400
        height: 700
        
    themeVariables:
        xyChart:
            plotColorPalette: "{','.join(osx_color_palette)}"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "OSX -- OSX Versions"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([i for i in mac_grp_quarter_df["quarter"].unique()]).replace("'", "")
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'


for ops in [str(i) for i in range(min_version, max_version + 1)] + ["Other"]:
    os_stats_df = mac_grp_quarter_df[mac_grp_quarter_df["OSX"] == ops].copy()
    os_stats_df["percentage"] = os_stats_df["percentage"] * 100

    # ensure all years have values
    os_stats_list = []
    for q in mac_grp_quarter_df["quarter"].unique():
        os_q_df = os_stats_df[os_stats_df["quarter"] == q]
        if len(os_q_df) > 0:
            os_value = float(os_q_df["percentage"].values[0])
        else:
            os_value = 0
        os_stats_list.append(os_value)

    cur_stats_txt = cur_stats_txt + "    line " + str(os_stats_list) + "\n"

legend_str = "$${"
for i, os_v in enumerate(range(min_version, max_version + 1)):
    legend_str = (
        legend_str + "\color{" + osx_color_palette[i] + "}" + str(os_v) + "\space\space\space"
    )
legend_str = legend_str + "\color{#808080}Other\space\space\space}$$"

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


# ---------------------------------------------------------------------------------------------
# %% 3.3 Resolution stats
# ---------------------------------------------------------------------------------------------
readme_content = readme_content + "\n## Display Resolution \n"
readme_content = (
    readme_content
    + """\n 
Aspect ratio classes are roughly mapped according to [wikipedia](https://en.wikipedia.org/wiki/Display_resolution_standards) 
with:

* 1.24 < **4:3** < 1.4  
* 1.49 < **3:2** < 1.51  
* 1.59 < **16:10** < 1.7
* 1.75 < **16:9** < 1.85  
* 1.98 < **18:9** < 2.27  
* 2.3 < **21:9** < 2.5
"""
)

# get pixels on screen
resolution_df = df[df["category"].str.contains("Resolution")].copy()
resolution_df[["w", "h"]] = resolution_df["name"].str.split(" x ", expand=True)
resolution_df["w"] = pd.to_numeric(resolution_df["w"], errors="coerce")
resolution_df["h"] = pd.to_numeric(resolution_df["h"], errors="coerce")
resolution_df.dropna(subset=["w", "h"], how="any", inplace=True)

resolution_df["ratio"] = resolution_df["w"] / resolution_df["h"]
resolution_df["pixels"] = resolution_df["w"] * resolution_df["h"]
resolution_df["pixels_weighted"] = resolution_df["pixels"] * resolution_df["percentage"]
resolution_df["w_weighted"] = resolution_df["w"] * resolution_df["percentage"]
resolution_df["h_weighted"] = resolution_df["h"] * resolution_df["percentage"]


# get weighted pixel sums per month
resolution_grp_df = (
    resolution_df.groupby(["date", "category"])[
        ["pixels_weighted", "w_weighted", "h_weighted"]
    ]
    .sum()
    .reset_index()
)
resolution_grp_df["ratio_weighted"] = (
    resolution_grp_df["w_weighted"] / resolution_grp_df["h_weighted"]
)

resolution_grp_year_df = (
    resolution_grp_df.groupby([resolution_grp_df["date"].dt.year, "category"])[
        ["pixels_weighted", "ratio_weighted"]
    ]
    .mean()
    .reset_index()
)

# create separate df for mapping ratios to predefined ranges
ratio_df = resolution_df.copy()
ratio_df["ratio_name"] = "Other"
ratio_df["ratio_name"] = np.where(
    (ratio_df["ratio"] > 1.24) & (ratio_df["ratio"] < 1.4), "4:3", ratio_df["ratio_name"]
)
ratio_df["ratio_name"] = np.where(
    (ratio_df["ratio"] > 1.49) & (ratio_df["ratio"] < 1.51), "3:2", ratio_df["ratio_name"]
)
ratio_df["ratio_name"] = np.where(
    (ratio_df["ratio"] > 1.59) & (ratio_df["ratio"] < 1.7), "16:10", ratio_df["ratio_name"]
)
ratio_df["ratio_name"] = np.where(
    (ratio_df["ratio"] > 1.75) & (ratio_df["ratio"] < 1.85), "16:9", ratio_df["ratio_name"]
)
ratio_df["ratio_name"] = np.where(
    (ratio_df["ratio"] > 1.98) & (ratio_df["ratio"] < 2.27), "18:9", ratio_df["ratio_name"]
)
ratio_df["ratio_name"] = np.where(
    (ratio_df["ratio"] > 2.3) & (ratio_df["ratio"] < 2.5), "21:9", ratio_df["ratio_name"]
)

ratio_grp_df = (
    ratio_df[ratio_df["category"].str.contains("Primary")]
    .groupby(["date", "ratio_name"])["percentage"]
    .sum()
    .reset_index()
)
ratio_grp_year_df = (
    ratio_grp_df.groupby([ratio_grp_df["date"].dt.year, "ratio_name"])["percentage"]
    .mean()
    .reset_index()
)


# create same ratio analyises per platform
ratio_p_df = df_platform[df_platform["category"].str.contains("Resolution")].copy()
ratio_p_df[["w", "h"]] = ratio_p_df["name"].str.split(" x ", expand=True)
ratio_p_df["w"] = pd.to_numeric(ratio_p_df["w"], errors="coerce")
ratio_p_df["h"] = pd.to_numeric(ratio_p_df["h"], errors="coerce")
ratio_p_df.dropna(subset=["w", "h"], how="any", inplace=True)
ratio_p_df["ratio"] = ratio_p_df["w"] / ratio_p_df["h"]

ratio_p_df["ratio_name"] = "Other"
ratio_p_df["ratio_name"] = np.where(
    (ratio_p_df["ratio"] > 1.24) & (ratio_p_df["ratio"] < 1.4), "4:3", ratio_p_df["ratio_name"]
)
ratio_p_df["ratio_name"] = np.where(
    (ratio_p_df["ratio"] > 1.49) & (ratio_p_df["ratio"] < 1.51),
    "3:2",
    ratio_p_df["ratio_name"],
)
ratio_p_df["ratio_name"] = np.where(
    (ratio_p_df["ratio"] > 1.59) & (ratio_p_df["ratio"] < 1.7),
    "16:10",
    ratio_p_df["ratio_name"],
)
ratio_p_df["ratio_name"] = np.where(
    (ratio_p_df["ratio"] > 1.75) & (ratio_p_df["ratio"] < 1.85),
    "16:9",
    ratio_p_df["ratio_name"],
)
ratio_p_df["ratio_name"] = np.where(
    (ratio_p_df["ratio"] > 1.98) & (ratio_p_df["ratio"] < 2.27),
    "18:9",
    ratio_p_df["ratio_name"],
)
ratio_p_df["ratio_name"] = np.where(
    (ratio_p_df["ratio"] > 2.3) & (ratio_p_df["ratio"] < 2.5), "21:9", ratio_p_df["ratio_name"]
)


ratio_p_grp_df = (
    ratio_p_df[ratio_p_df["category"].str.contains("Primary")]
    .groupby(["date", "ratio_name", "platform"])["percentage"]
    .sum()
    .reset_index()
)
ratio_p_grp_year_df = (
    ratio_p_grp_df.groupby([ratio_p_grp_df["date"].dt.year, "ratio_name", "platform"])[
        "percentage"
    ]
    .mean()
    .reset_index()
)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.3.1 Primary Display: Preset Aspect Ratios
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

readme_content = readme_content + """### All platforms\n"""

### add title and x-axis & y-axis info
cur_stats_txt = (
    "```mermaid\n"
    + """---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6,#46a2da,#808080"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "Primary Display: Aspect Ratio classes"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([int(i) for i in ratio_grp_year_df["date"].unique()])
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

min_year = ratio_grp_year_df["date"].min()
max_year = ratio_grp_year_df["date"].max()
ratio_classes_list = ["4:3", "3:2", "16:10", "16:9", "18:9", "21:9", "Other"]
for rc in ratio_classes_list:
    rc_stats_df = ratio_grp_year_df[ratio_grp_year_df["ratio_name"] == rc].copy()
    rc_stats_df["percentage"] = rc_stats_df["percentage"] * 100

    # ensure all years have values
    rc_stats_list = []
    for year in range(min_year, max_year + 1):
        rc_year_df = rc_stats_df[rc_stats_df["date"] == year]
        if len(rc_year_df) > 0:
            rc_value = float(rc_year_df["percentage"].values[0])
        else:
            rc_value = 0
        rc_stats_list.append(rc_value)

    cur_stats_txt = cur_stats_txt + "    line " + str(rc_stats_list) + "\n"

legend_str = """$${\color{#51a8a6}4:3\space\space\space
\color{#f9a900}3:2\space\space\space
\color{#f92800}16:10\space\space\space
\color{#d92080}16:9\space\space\space
\color{#8a52a6}18:9\space\space\space     
\color{#46a2da}21:9\space\space\space
\color{#808080}Other\space\space\space}$$"""

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.3.2 Primary Display: Aspect Ratio over time
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

primary_display_df = resolution_grp_year_df[
    resolution_grp_year_df["category"].str.contains("Primary")
].copy()

### add title and x-axis & y-axis info
cur_stats_txt = (
    "```mermaid\n"
    + """---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#DB4105"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "Primary Display: average aspect ratio (weighted by percentage)"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([int(i) for i in primary_display_df["date"].unique()])
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "ratio" \n'
cur_stats_txt = (
    cur_stats_txt + "    line " + str(primary_display_df["ratio_weighted"].to_list()) + "\n"
)

legend_str = """$${\color{#DB4105} For \space reference \space 1920*1080 \space ratio \space = \space 16:9 \space = \space 1.77 \space}$$"""

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.3.3 Primary Display: Pixels Shown
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

primary_display_df = resolution_grp_year_df[
    resolution_grp_year_df["category"].str.contains("Primary")
].copy()

### add title and x-axis & y-axis info
cur_stats_txt = (
    "```mermaid\n"
    + """---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#DB4105"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "Primary Display: number of pixels on screen (weighted by percentage)"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([int(i) for i in primary_display_df["date"].unique()])
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "pixels" \n'
cur_stats_txt = (
    cur_stats_txt + "    line " + str(primary_display_df["pixels_weighted"].to_list()) + "\n"
)

legend_str = """$${\color{#DB4105} For \space reference \space 1920*1080 \space = \space 2.073.600 \space pixels \space}$$"""

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.3.4 Multi Display Setup: Pixels Shown
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
##51a8a6,#f9a900,#f92800,#d92080,#8a52a6"

mm_display_df = resolution_grp_year_df[
    resolution_grp_year_df["category"].str.contains("Multi-Monitor")
].copy()

### add title and x-axis & y-axis info
cur_stats_txt = (
    "```mermaid\n"
    + """---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#DB4105"

--- 
"""
)

cur_stats_txt = (
    cur_stats_txt
    + """
xychart-beta
    title "Multi-Monitor: number of pixels on screens (weighted by percentage)"
"""
)
cur_stats_txt = (
    cur_stats_txt
    + "    x-axis "
    + str([int(i) for i in mm_display_df["date"].unique()])
    + "\n"
)
cur_stats_txt = cur_stats_txt + '    y-axis "pixels" \n'
cur_stats_txt = (
    cur_stats_txt + "    line " + str(mm_display_df["pixels_weighted"].to_list()) + "\n"
)

legend_str = """$${\color{#DB4105} For \space reference \space 2x \space 1920*1080 \space = \space 4.147.200 \space pixels \space}$$"""

readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## 3.3.5 Per Platform: Primary Display: Preset Aspect Ratios
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

readme_content = readme_content + """### Single platforms\n"""

for platform in ["pc", "mac", "linux"]:

    platform_ratio_p_grp_year_df = ratio_p_grp_year_df[
        ratio_p_grp_year_df["platform"] == platform
    ]

    ### add title and x-axis & y-axis info
    cur_stats_txt = (
        "```mermaid\n"
        + """---
config:
    xyChart:
        width: 700
        height: 400
        
    themeVariables:
        xyChart:
            plotColorPalette: "#51a8a6,#f9a900,#f92800,#d92080,#8a52a6,#46a2da,#808080"

--- 
"""
    )

    cur_stats_txt = (
        cur_stats_txt
        + f"""
    xychart-beta
        title "{platform} -- Primary Display: Aspect Ratio classes"
    """
    )
    cur_stats_txt = (
        cur_stats_txt
        + "    x-axis "
        + str([int(i) for i in platform_ratio_p_grp_year_df["date"].unique()])
        + "\n"
    )
    cur_stats_txt = cur_stats_txt + '    y-axis "%" \n'

    min_year = platform_ratio_p_grp_year_df["date"].min()
    max_year = platform_ratio_p_grp_year_df["date"].max()
    ratio_classes_list = ["4:3", "3:2", "16:10", "16:9", "18:9", "21:9", "Other"]
    for rc in ratio_classes_list:
        rc_stats_df = platform_ratio_p_grp_year_df[
            platform_ratio_p_grp_year_df["ratio_name"] == rc
        ].copy()
        rc_stats_df["percentage"] = rc_stats_df["percentage"] * 100

        # ensure all years have values
        rc_stats_list = []
        for year in range(min_year, max_year + 1):
            rc_year_df = rc_stats_df[rc_stats_df["date"] == year]
            if len(rc_year_df) > 0:
                rc_value = float(rc_year_df["percentage"].values[0])
            else:
                rc_value = 0
            rc_stats_list.append(rc_value)

        cur_stats_txt = cur_stats_txt + "    line " + str(rc_stats_list) + "\n"

    legend_str = """$${\color{#51a8a6}4:3\space\space\space
    \color{#f9a900}3:2\space\space\space
    \color{#f92800}16:10\space\space\space
    \color{#d92080}16:9\space\space\space
    \color{#8a52a6}18:9\space\space\space     
    \color{#46a2da}21:9\space\space\space
    \color{#808080}Other\space\space\space}$$"""

    readme_content = readme_content + cur_stats_txt + "``` \n" + legend_str + "\n\n<br/>\n\n"


# %% 4 - Save to File
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
