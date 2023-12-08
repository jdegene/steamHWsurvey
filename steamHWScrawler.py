# -*- coding: utf-8 -*-

import os
import time

import pendulum
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Dates in output file are dates of measurements (Steam shows November values in December)
# Dates in queries and functions (eq current month december to fetch november dates)


def get_soup(url):
    r = requests.get(url)
    soup_all = BeautifulSoup(r.text, "html5lib")

    return soup_all


def get_2008(soup_all):
    page_df = pd.DataFrame(columns=["date", "category", "name", "change", "percentage"])

    date_header = soup_all.find("div", {"id": "main_stats_header"})
    date_text_raw = date_header.h1.text
    date_text_clean = date_text_raw[: date_text_raw.find("(")].strip()
    date_formatted = pendulum.from_format(date_text_clean, "MMMM YYYY").to_date_string()

    soup_main_stats = soup_all.find("div", {"id": "main_stats"})
    soup_main_stats_category = soup_main_stats.find_all("div", {"class": "stats_row"})
    soup_main_stats_right_cols = soup_main_stats.find_all("div", {"class": "stats_row_details"})

    for entry_num in range(len(soup_main_stats_category)):
        entry_main_category = soup_main_stats_category[entry_num]
        main_category_name = entry_main_category.find(
            "div", {"class": "stats_col_left"}
        ).text.strip()

        entry_main_stats = soup_main_stats_right_cols[entry_num]
        entry_main_stats_entries = entry_main_stats.find_all(
            "div", {"class": "stats_col_mid_details"}
        )

        for single_line in entry_main_stats_entries:
            line_name = single_line.text.strip()

            stats_line = single_line.find_next("div", {"class": "stats_col_right row_details"})
            stats_line_raw = stats_line.text.strip()

            change_text = stats_line_raw[stats_line_raw.find("(") + 1 : stats_line_raw.find(")")]
            change_float = float(change_text.strip("%")) / 100

            abs_text = stats_line_raw[stats_line_raw.rfind(" ") + 1 :]
            abs_float = float(abs_text.strip("%")) / 100

            page_df = pd.concat(
                [
                    page_df,
                    pd.DataFrame(
                        {
                            "date": [date_formatted],
                            "category": [main_category_name],
                            "name": [line_name],
                            "change": [change_float],
                            "percentage": [abs_float],
                        }
                    ),
                ],
                ignore_index=True,
            )

    return page_df


def get_2010(soup_all):
    page_df = pd.DataFrame(columns=["date", "category", "name", "change", "percentage"])

    date_header = soup_all.find("div", {"id": "main_stats_header"})
    date_text_raw = date_header.text
    date_text_clean = date_text_raw[: date_text_raw.find("(")].strip()
    date_formatted = pendulum.from_format(date_text_clean, "MMMM YYYY").to_date_string()

    soup_main_stats = soup_all.find("div", {"id": "main_stats"})
    soup_main_stats_category = soup_main_stats.find_all("div", {"class": "stats_row"})
    soup_main_stats_right_cols = soup_main_stats.find_all("div", {"class": "stats_row_details"})

    for entry_num in range(len(soup_main_stats_category)):
        entry_main_category = soup_main_stats_category[entry_num]
        main_category_name = entry_main_category.find(
            "div", {"class": "stats_col_left"}
        ).text.strip()

        entry_main_stats = soup_main_stats_right_cols[entry_num]
        entry_main_stats_entries = entry_main_stats.find_all(
            "div", {"class": "stats_col_mid data_row"}
        )

        for single_line in entry_main_stats_entries:
            line_name = single_line.text.strip()

            stats_line_abs = single_line.find_next("div", {"class": "stats_col_right data_row"})
            stats_line_abs_raw = stats_line_abs.text.strip()
            abs_float = float(stats_line_abs_raw.strip("%")) / 100

            stats_line_change = single_line.find_next(
                "div", {"class": "stats_col_right2 data_row"}
            )
            change_text = stats_line_change.text
            change_float = float(change_text.strip("%")) / 100

            page_df = pd.concat(
                [
                    page_df,
                    pd.DataFrame(
                        {
                            "date": [date_formatted],
                            "category": [main_category_name],
                            "name": [line_name],
                            "change": [change_float],
                            "percentage": [abs_float],
                        }
                    ),
                ],
                ignore_index=True,
            )

    return page_df


def get_2014(soup_all):
    page_df = pd.DataFrame(columns=["date", "category", "name", "change", "percentage"])

    date_header = soup_all.find("div", {"id": "main_stats_header"})
    date_text_raw = date_header.text
    date_text_clean = date_text_raw[: date_text_raw.find("(")].strip()
    date_formatted = pendulum.from_format(date_text_clean, "MMMM YYYY").to_date_string()

    soup_main_stats = soup_all.find("div", {"id": "main_stats"})
    soup_main_stats_category = soup_main_stats.find_all(
        "div", {"class": "stats_row", "onclick": True}
    )
    soup_main_stats_right_cols = soup_main_stats.find_all("div", {"class": "stats_row_details"})

    for entry_num in range(len(soup_main_stats_category)):
        entry_main_category = soup_main_stats_category[entry_num]
        main_category_name = entry_main_category.find(
            "div", {"class": "stats_col_left"}
        ).text.strip()

        entry_main_stats = soup_main_stats_right_cols[entry_num]
        entry_main_stats_entries = entry_main_stats.find_all(
            "div", {"class": "stats_col_mid data_row"}
        )

        for single_line in entry_main_stats_entries:
            line_name = single_line.text.strip()

            stats_line_abs = single_line.find_next("div", {"class": "stats_col_right data_row"})
            stats_line_abs_raw = stats_line_abs.text.strip()
            abs_float = float(stats_line_abs_raw.strip("%")) / 100

            stats_line_change = single_line.find_next(
                "div", {"class": "stats_col_right2 data_row"}
            )
            change_text = stats_line_change.text
            change_float = float(change_text.strip("%")) / 100

            page_df = pd.concat(
                [
                    page_df,
                    pd.DataFrame(
                        {
                            "date": [date_formatted],
                            "category": [main_category_name],
                            "name": [line_name],
                            "change": [change_float],
                            "percentage": [abs_float],
                        }
                    ),
                ],
                ignore_index=True,
            )

    return page_df


def get_archive_soup_year_month(month=1, year=2020, day=15):
    str_month = str(month).rjust(2, "0")
    str_day = str(day).rjust(2, "0")
    url = f"http://web.archive.org/web/{year}{str_month}{str_day}/http://store.steampowered.com/hwsurvey"

    try:
        soup = get_soup(url)
    except (Exception,):
        time.sleep(30)
        try:
            soup = get_soup(url)
        except (Exception,):
            print(f"{month} and {year} site loading failed")
            return None

    month_df = None
    for fetch_func in [get_2008, get_2010, get_2014]:
        try:
            month_df = fetch_func(soup)
            if (month_df is None) or len(month_df) < 1:
                raise ValueError("Cannot be empty")
            break
        except (Exception,):
            pass

    if month_df is not None:
        return month_df
    else:
        print(f"{month} and {year} returned nothing")
        return None


def build_from_scratch(out_csv_path="shs.csv"):
    """Builds a csv file from scratch"""

    try:
        out_df = pd.read_csv(out_csv_path, encoding="utf8")
        start_year = pd.to_datetime(out_df["date"], errors="coerce").max().year
    except (Exception,):
        start_year = 2008

    for year in range(start_year, pendulum.now().year + 1):
        for month in range(1, 13):
            if (year == 2008) and (month != 12):
                continue

            month_df = get_archive_soup_year_month(month=month, year=year)

            if os.path.isfile(out_csv_path):
                out_df = pd.read_csv(out_csv_path, encoding="utf8")
                out_df = pd.concat([out_df, month_df])
            else:
                out_df = month_df.copy()

            out_df = out_df.drop_duplicates(subset=["date", "category", "name"])
            out_df.to_csv(out_csv_path, encoding="utf8", index=False, float_format="%.4f")

            print(f"{year} {month} done")


def update_month_from_archive(month=1, year=2020, day=15, out_csv_path="shs.csv"):
    """Loads a specific month and adds to out_csv_path file"""

    month_df = get_archive_soup_year_month(month=month, year=year, day=day)
    print(month_df)

    if os.path.isfile(out_csv_path):
        out_df = pd.read_csv(out_csv_path, encoding="utf8")
        out_df = pd.concat([out_df, month_df])
    else:
        out_df = month_df.copy()

    out_df = out_df.drop_duplicates(subset=["date", "category", "name"])
    out_df.to_csv(out_csv_path, encoding="utf8", index=False, float_format="%.4f")


def update_month_current_steam(out_csv_path="shs.csv"):
    """Reads current Steam HW site"""

    soup = get_soup("https://store.steampowered.com/hwsurvey")
    month_df = get_2014(soup)

    if os.path.isfile(out_csv_path):
        out_df = pd.read_csv(out_csv_path, encoding="utf8")
        out_df = pd.concat([out_df, month_df])
    else:
        out_df = month_df.copy()

    out_df = out_df.drop_duplicates(subset=["date", "category", "name"])
    out_df.sort_values(["date", "category", "name"], inplace=True)
    out_df.to_csv(out_csv_path, encoding="utf8", index=False, float_format="%.4f")


def update_month_current_platform_steam(out_csv_path="shs_platform.csv"):
    """Reads current Steam HW site by platform"""

    for platform in ["pc", "mac", "linux"]:
        soup = get_soup(f"https://store.steampowered.com/hwsurvey?platform={platform}")
        month_df = get_2014(soup)
        month_df.insert(1, "platform", platform)

        if os.path.isfile(out_csv_path):
            out_df = pd.read_csv(out_csv_path, encoding="utf8")
            out_df = pd.concat([out_df, month_df])
        else:
            out_df = month_df.copy()

        out_df = out_df.drop_duplicates(subset=["date", "category", "name"])
        out_df.sort_values(["date", "platform", "category", "name"], inplace=True)
        out_df.to_csv(out_csv_path, encoding="utf8", index=False, float_format="%.4f")


if __name__ == "__main__":
    update_month_current_steam(out_csv_path="shs.csv")
    update_month_current_platform_steam(out_csv_path="shs_platform.csv")
