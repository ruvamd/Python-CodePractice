import pytest
import re
import automated_interview
# def test_question():
#     assert sorted_questions==

regex_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def test_email(answer):
    if (re.search(regex_email,answer)):
        print('valid email')
    else:
        print('not valid email format')
    



