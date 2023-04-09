def debug_test(debug1):
  if debug1 == '성공':
    return ("성공해")
  else:
    return ("탈락")

debug1 = "맞냐"
find_result = debug_test(debug1)

print(find_result)
  