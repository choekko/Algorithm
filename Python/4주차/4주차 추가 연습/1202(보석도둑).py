"�Ϳ� ������ �� Ǫ�̳׿�
������ �ξ� ���Ͻó׿� �η����ϴ� 

ù��° ������ ��ȭ�� ��ü�� ���� ����ѵ�
dp[i] = max((dp[i - 3] + stair[i - 1]  + stair[i]), (dp[i - 2] + stair[i]))
���� �̷��� ��ȭ���� ����� dp�� 1���� �迭�� ������� �ִ��󱸿�. Ȥ�� ������ �ɱ��ؼ� ���ܺ��ϴ�. 

�ι�°���������� �湮 �迭 ��� check�� ���� -1�� ���� �ƴ����� �湮üũ�� ������ �� �����ϴ�! 

����° ������ ���� �յ� ���� ����µ� ����ϰ� �ʹ� �� Ǫ�� �� �����ϴ�. 
�Ѽ� ������ϴ�.

���� �����̽��ϴ�! "


from sys import stdin
import heapq

stdin = open("input.txt", "r") 

dia_num, bag_num = map(int, stdin.readline().split())

dia = [list(map(int, stdin.readline().split())) for _ in range(dia_num)]
dia.sort(key = lambda x : x[0])

bag_weight = [int(stdin.readline()) for _ in range(bag_num)]
bag_weight.sort()

heap = []

dia_idx = 0
rst = 0
for weight in bag_weight:
	while True :
		if dia_idx < dia_num and dia[dia_idx][0] <= weight :
			heapq.heappush(heap, -dia[dia_idx][1])
			dia_idx += 1
			continue
		if heap : 
			rst += -(heapq.heappop(heap))
		break
print(rst)