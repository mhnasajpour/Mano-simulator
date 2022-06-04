from Compile import Compile

code = """
sta  ,  ORG\t100
q, LDA A /dsf*
ADD   b
STA\tc \t\t/ hello oo
 ** STA\tc +\t\t  /sdf
STA\tc/sdf
  hlt
org 700
a  ,  deC 11
b* *, dec# 200
c , hex ff
  end 
"""


preprocessing = Compile(code)
print(preprocessing.serialize())
