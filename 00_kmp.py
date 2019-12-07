from typing import List

# dfa[j]: search[j+1] != text[i+1] 이면, text[i+1]을 dfa[j]에 들어있는 search의 index와 비교를 해야 함

def kmp(text: str, search: str) -> List[int]: # return all indices
  # initialize dfa machine
  i, j = 1, 0
  dfa = [0]
  while i < len(search):
    # QUESTION: does this part gurantee O(1)?
    while j>0 and search[i] != search[j]:
      j = dfa[j-1]
    # QUESTION: why?
    if search[i] == search[j]:
      j += 1
    dfa.append(j)
    i += 1

  # do search
  j, indices = 0, []
  for i, c in enumerate(text):
    # QUESTION: does this part gurantee O(1)?
    while j>0 and c != search[j]:
      j = dfa[j-1]
    if c == search[j]:
      if j+1 == len(search):
        indices.append(i-len(search)+1)
        # QUESTION: what happen after doing j = dfa[j]?
        # 이미 indices에 추가 되었으므로, 그 부분을 한 번 틀렸다고 가정하고, j를 갱신해줌
        j = dfa[j]
      else:
        j += 1

  return indices


print(kmp("abxabcabcaby", "abcaby")) # [6]
print(kmp("abxabcabcaby", "bcab")) # [4, 7]