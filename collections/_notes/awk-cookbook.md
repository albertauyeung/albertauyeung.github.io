---
layout: article
title:  "AWK Cookbook"
tags: [awk, data processing]
---

## Options

- `-F`: To specify a file separator.
- `-f`: To specify a file that contains awk script.
- `-v`: To declare a variable.

## Positional Variables

- `$0`: refers to the current line
- `$1`: refers to the value in the first column
- `$6`: refers to the value in the sixth column

Example: print the second column of each row:

```awk
$ echo "1,2,3\n4,5,6" | awk -F, '{ print $2 }'
2
5
```

Example: print the first and third columns of each row:

```awk
$ echo "1,2,3\n4,5,6" | awk -F, '{ print $1","$3 }'
1,3
4,6
```

## Built-in Variables

- `FS`: input field separator, tells Awk how to split a record into different fields
- `OFS`: output field separator, tells Awk how to print out a record
- `NF`: number of fields in a record
    - Note: `$NF` refers to the last field;
    - Note: In Awk, there is a limit of 99 fields in a single line
- `NR`: number of records
- `RS`: record separator (by default it is the line break `\n` character)
- `ORS`: output record separator (by default it is also the new line `\n` character)
- `FILENAME`: the current file name

## Built-in Functions

- `length`: Return the lenght of a string, e.g `if length($0) > 1 { ... }`
- `index`: Return the position of a substring in a given string, e.g. `index("apple", "l")` returns `4`
- `substr`: Return a substring of the given string, e.g. `substr("apple", 1, 3)` returns `app`
- `split`: Split a string into an array, return the number of components, usage: `split(string, array, separator)`, where separator should be a single character
- `tolower`, `toupper`: convert strings to lowercases or uppercases

## Summary of Data

Summing up the values in the second column:

```awk
$ echo "1,2,3\n4,5,6" | awk -F, '{ sum += $2 } END { print sum }'
7
```

Summing up the values in the second column if the first column is larger than 10:

```awk
$ echo "11,2\n4,1\n15,3\n8,2" | awk -F, '$1 > 10 { sum += $2 } END { print sum }'
5
```

## Text Search

Regular expressions are put between slashes. For example, `/apple/` will match any string containing the `apple`.

```awk
$ echo "I have an apple\nI have an orange" | awk '/apple/' { print $0 }'
I have an apple
```



