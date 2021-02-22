#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 22

def test_code():
    assert main.removeLast([1,2,3,4,5]) == [1, 2,  3, 4], "removeLast([1,2,3,4,5]) == [1, 2,  3, 4] failed"
    assert main.removeLast([1,2,3,4,5,6,7,8,9,10]) == [1, 2,  3, 4, 5, 6, 7, 8, 9], "removeLast([1,2,3,4,5,6,7,8,9,10]) == [1, 2,  3, 4, 5, 6, 7, 8, 9] failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
