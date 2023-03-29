
# ArabicLT

ArabicLT is a repository containing a SQLite database and a CSV file with a comprehensive collection of Arabic synonyms, antonyms, qawafi (rhymes), and plurals. This toolkit also includes a simple Python script to extract the data from the SQLite database and the CSV files.

## Table of Contents

-   [Features](https://github.com/mdanok/arabicLT#features)
-   [Installation](https://github.com/mdanok/arabicLT#installation)
-   [Usage](https://github.com/mdanok/arabicLT#usage)
-   [Source](https://github.com/mdanok/arabicLT#source)
-   [Contributing](https://github.com/mdanok/arabicLT#contributing)
-   [License](https://github.com/mdanok/arabicLT#license)

## Features

-   Comprehensive collection of Arabic language resources, including:
    -   Synonyms
    -   Antonyms
    -   Qawafi (rhymes)
    -   Plurals
-   SQLite database for efficient storage and retrieval
-   CSV files for easy data manipulation
-   Simple Python script to extract data

## Installation

1.  Clone the repository:
`git clone https://github.com/mdanok/arabicLT.git` 

2.  Change the working directory:
`cd arabicLT`

## Usage

The `arabiclt.py` script can be used to extract and manipulate data from the SQLite database. The script provides various functions to work with the data, such as searching for synonyms, antonyms, qawafi, and plurals.

Example usage:

    import arabiclt

### Get synonyms for a word
    synonyms = arabiclt.get_synonyms('كبير')
    print(synonyms)

### Get antonyms for a word
    antonyms = arabiclt.get_antonyms('صغير')
    print(antonyms)

### Get qawafi (rhymes) for a word
    qawafi = arabiclt.get_qawafi('بيت')
    print(qawafi)

### Get plurals for a word
    plurals = arabiclt.get_plurals('كتاب')
    print(plurals) 

## Source
This data has been taken from [Radif App](https://play.google.com/store/apps/details?id=com.tahadz.radif_dictionary), decompile using [apktool](https://github.com/iBotPeaches/Apktool).
You can download the SQL database from `db` folder, and you can download the csv version in `csv` folder.

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these steps:

1.  Fork the repository
2.  Create a new branch (`git checkout -b feature-branch`)
3.  Commit your changes (`git commit -m 'Add new feature'`)
4.  Push to the branch (`git push origin feature-branch`)
5.  Create a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/mdanok/arabicLT/blob/master/LICENSE.md) file for more information.
