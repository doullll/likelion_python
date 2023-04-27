score={}
sum=0

team=['도울','지연','민지','세현','화진']

for i in team:
    own_score=int(input(f'{i}의 점수를 입력하세요:'))
    score[i]=own_score

for v in score.values():
    sum+=v

print(f'학생들 점수의 평균은 {sum/len(score)}점입니다.')


