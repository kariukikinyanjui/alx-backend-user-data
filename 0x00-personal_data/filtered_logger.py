#!/usr/bin/env python3
'''A function that returns the log message obfuscated'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    pattern = re.compile(
            r'(' + '|'.join(fields) + r')=([^' + separator + r']+)')
    return pattern.sub(r'\1=' + redaction, message)


if __name__ == '__main__':
    main()
