# Telegram Account Age

Find the approximate creation date of a Telegram account using User ID interpolation based on known ID-timestamp mappings.

## Overview

This project estimates when a Telegram account was created by comparing a given User ID against a dataset of known Telegram User ID and timestamp pairs, then using interpolation to calculate an approximate creation date.

This tool is useful for getting a close estimate of account age, but it does **not** provide the exact Telegram account creation date.

## Features

- Estimate Telegram account creation date from User ID

## Important Notice

This project provides **approximate results only**.

The estimated creation date is **not exact** and may be inaccurate in some cases, especially for:

- newly created Telegram accounts
- accounts with User IDs outside or near the edge of the known mapping range
- cases where Telegram changes ID allocation patterns

Newly created accounts may return a noticeably incorrect approximate date.

## How It Works

The script uses a list of known Telegram User ID and Unix timestamp mappings.

When you enter a User ID:

1. The script finds the nearest known IDs around it
2. It returns an estimated creation date

```
Enter a User ID: 123456789
Estimated Creation Date: Approximately 2019-06-14
Time Ago: 6 years ago
```

## Author

- Name: Nafis Muhtadi
- Telegram: [@itsSmartDev](https://t.me/itsSmartDev)

> Feel free to reach out if you have any questions or feedback.
