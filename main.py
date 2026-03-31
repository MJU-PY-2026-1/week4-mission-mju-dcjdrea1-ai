# 파일이름 :
# 작 성 자 :이윤재

buket_list = []

restaurant = input("맛집 리스트 입력: ")
buket_list.append(restaurant)
restaurant = input("맛집 리스트 입력: ")
buket_list.append(restaurant)
restaurant = input("맛집 리스트 입력: ")
buket_list.append(restaurant)

print(f'리스트:{buket_list}')

vip_restaurant = input("맛집 리스트 추가: ")
buket_list.insert(0,vip_restaurant)

print(f'리스트:{buket_list}')

visited = input("도장 깨기: ")
buket_list.remove(visited)

print(f'리스트:{buket_list}')
