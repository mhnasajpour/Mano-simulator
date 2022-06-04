from compile import Compile

code = """
ORG 100
LDA A
ADD B
STA C
HLT

ORG 400
A, DEC 5
B, HEX F
C, DEC 0
END
"""


a = Compile()

is_ok, commands = a.start(code)
print(is_ok)
print(commands)
