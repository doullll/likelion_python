n = int(input('몇 개의 수를 입력하실 건가요?(개): '))
x = int(input('어떤 숫자보다 큰 수들을 출력할까요?: '))

num_list=[]
final_list=[]

for i in range(n):
    num=int(input(f'{i+1}번 숫자를 입력하세요: '))
    num_list.append(num)

for i in range(n):
    if num_list[i]>x:
        final_list.append(num_list[i])

print(f'입력하신 숫자 중 {x}보다 큰 숫자는 {final_list}입니다.')  