#입력된 문자열을 검사하는데 특정 문자 다음에 다른 문자가 나올 경우 
# 문자열에서 그 글자 다음부터 끝까지 검사하여 똑같은 문자가 있는지 검사하고, 
# 이상 없으면 그룹 단어로 카운트했다.
N=int(input())

answer=0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer+=1
print(answer)

'''find는 해당하는 단어를 찾아서 index를 알려주는데 따로 값을 지정해주지 않으면 
첫번째 위치를 알려준다. 
따라서 만약 앞에 있는 단어의 find index가 뒤에있는 단어의 find index보다 크다면 그룹단어가 아니다.'''
N = int(input())
count = N

for j in range(N):
    word = input()
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]):
            count -= 1
            break
print(count)