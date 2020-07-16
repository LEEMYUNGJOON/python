# 코드 테스트
# 함수나 클래스를 만들면 그 코드를 unittest 모듈로 테스트 할 수 있습니다.

# import unittest
# from 함수파일 import 함수명

# class 대문자변수(unittest.TestCase):

#     def 함수명(self):
#         확인하고자하는 내용
#         self.assert()

# unittest.main() # 이 파일에 들어있는 테스트 실행하기

# 함수테스트
# 함수를 테스트하려면 함수파일, 테스트파일이 필요합니다.

# 단위테스트
# 함수의 특정 동작 한 가지가 정확한지 확인하는 것.

# 테스트케이스
# 단위테스트의 묶음

# 실패한 테스트 점검
# 테스트 실패시 테스트를 수정하지 말고 테스트를 실패하게 만든 코드를 수정합니다.

# 단언 메서드
# assertEqual(a,b) a==b
# assertNotEqual(a,b) a!=b
# assertTrue(x) x가 True인가?
# assertFalse(x) x가 False인가?
# assertIn(item, list) item이 list안에 있는가?
# assertNotIn(item, list) item이 list안에 없는가?

# 클래스 테스트
# 모듈을 개선하면서 기존 동작을 망치지 않도록 클래스 테스트를 할 수 있다.

# setUp() 메서드
# 객체를 한 번만 만들고 각 테스트 메서드에서 사용할 수 있게 하는 setUp() 메서드