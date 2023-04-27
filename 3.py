score={}
sum=0

team=['도울','지연','민지','세현','화진']

for i in team:
    own_score=int(input(f'[i]의 점수를 입력하세요:'))
    score[i]=num

score["도울"]=100
score["지연"]=10
score["민지"]=90
score["세현"]=80
score["화진"]=1

for v in score.values():
    sum+=v

print(f'학생들 점수의 평균은 {sum/len(score)}점입니다.')


