# 코드테스트--
# 함수나 클래스를 만들면 unittest모듈로 테스트할 수 있다.

# import unittest
# from 함수파일 import 함수명

# class 대문자변수(unittest.TestCase):

#     def 함수명(self):
#         확인하고자하는 내용
#         self.assert()

# unittest.main()

#함수테스트--
#함수를 테스트하려면 함수,테스트파일이 필요합니다.

#단위테스트
#함수의 특정 동작 한가지가 정확한지 확인하는것

#테스트케이스
#단위테스트의 모음

# 실패한 테스트 점검
# 테스트 실패시 테스트를 수정하지말고 테스트를 실패하게 만든 코드를 수정하기

# 단언 메서드
# assertEqual(a,b)
# assertNotEqual(a,b)
# assertIn(item, list)
# assertTrue(x)
# assertFalse(x)
# assertNotIn(item, list)

# 클래스 테스트
# 모듈을 개선하면서 기존 동작을 망치치 않게 하려면?

# setUp() 메서드를 사용한다.
# 객체를 한번만 만들고 각 테스트 메서드에서 사용할 수 있게한다.

import unittest

from 함수파일 import 함수명:
class 대문자변수(unittest.TestCase):

    def 함수명(self):
        확인내용
        self.assert()
unittest.main()