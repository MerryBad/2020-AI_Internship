from pyswip import *

N = 3 # 원반 개수

def notify(t):
    print("%s --> %s" % tuple(t))
notify.arity = 1

prolog = Prolog()
registerForeign(notify)     # 외부 함수 prolog에 등록
prolog.consult("hanoi.pl")  # prolog 프로그램 파일 읽어들이기
list(prolog.query("hanoi(%d)" % N))