jumin = "210217-1234567"

print("성별 : " + jumin[7])
print("출생년도 : " + jumin[0:2]) # :의미-->0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 앞에 숫자 없으면 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-6:])
# 맨 뒤에서 시작에서 앞으로 6번째까지

