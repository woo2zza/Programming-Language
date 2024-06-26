# 진법 변환
# 증명 => 대우 증명법 (역, 이  대우, 부정)
# 비트 연산

# 비트 연산
# bit 2진수로 표현된
# 2 진수 (binary number) 8진수 (octal number) 10진수 (decimal number) 16진수 (hex number)
# 10진수 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19...
# 16진수 0 1 2 3 4 5 6 7 8 9  A  B  C  D  E  F 10 11 12 13 ....
#       0x0 0x1 0x2 0x3 .... 0xA 0xB 0xC....
# 2진수
# 0000 0001 0010 0010 0011 0100 0110 ...
# 0b0 0b1 0b10 0b11 0b100...



# 10진수 -> 2진수
#       128 64 32 16 8 4 2 1
# 36 ->  0   0  1  0 0 1 0 0

# 2진수 -> 16진수
# 00100100 => 0010/0100 = 24

# 10진수 -> 16진수
# 75 -> 4b
# 01001011

# 10진수를 2진수, 8진수, 16진수로 변환하기
a = 13
b = bin(a) # 2진수
c = oct(a) # 8진수
d = hex(a) # 16진수
print(b, c, d) # 0b1101 0o15 0xd
print(type(b)) # <class 'str'>

# 다시 10진수로 변환하기
print(int(b, 2))
print(int(c, 8))
print(int(d, 16))

# 10진수를 n진수로 변환하기

def trans(mok):
    ans = []
    while mok >= 1:
        mok, rest = divmod(mok, n)
        ans.append(str(rest))

    return ans


n = int(input()) # n 진수
a = int(input())
ret = trans(a)
# 이후 거꾸로 출력

# 비트연산자
print(13 & 9) # and 연산자 / & -> ampersand
"""
& 둘다 참일 때만 1

13 -> 00001101
9 ->  00001001
      00001001
=> 9
"""

print(13 | 9) # or 연산자 / | -> bar
"""
& 둘 중 하나만 참일 때만1

13 -> 00001101
9 ->  00001001
      00001101
=> 13
"""

print(13 ^ 9) # xor 연산자 exclusive or / ^ -> caret
"""
^ : 둘이 다르면 참 / 둘이 같으면 거짓

13 -> 00001101
9 ->  00001001
      00000100
=> 4
"""

# shift 연산자
print(10 << 2)
"""
<< 비트를 2칸 왼쪽으로 밀어버리겠다

10
0001010
0010100
=> 40

10 * (2 ** 2) 과 같은 의미
"""

print(10 >> 2)
"""
<< 비트를 2칸 왼쪽으로 밀어버리겠다

10
0001010
0000010
=> 2

10 // (2 ** 2) 과 같은 의미
"""

# 비트의 타입은 문자열

# 명제와 증명
"""
식과 조건 => 명제
대우 증명법 => 부정, 역, 이, 대우

명제 : 6은 2의 배수이고 3의 배수이다
부정 : 6은 2의 배수가 아니거나 3의 배수이다

명제 : 6의 배수라면 3의 배수이다
역 : 6의 배수가 아니면 3의 배수가 아니다
이 : 3의 배수라면 6의배수다
대우 : 3의 배수가 아니면 6의 배수도 아니다.

대우 증명법 : 명제의 대우가 참이라면 그 명제는 참이다

명제 : n 제곱이 짝수면 n은 짝수다
대우 : n이 홀수면 n 제곱이 홀수다
      n = 2k + 1  4k^2 + 4k + 1
                    => 2(2k^2 + 2k) + 1 => 홀수
                    
     따라서 명제에 대한 대우는 홀수 즉, 참임으로 위 명제는 참이다
     

연습문제 : n제곱이 3의 배수라면 n은 3의 배수다

"""

"""
1번 진법 변환 / 비트연산 / join 잘쓰기
2번 변별력 문제
3번 대우증명법
"""