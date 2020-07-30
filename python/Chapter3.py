
print(range(10))






# class Person:
#     count = 0  # 클래스 속성
#
#     def __init__(self):
#         Person.count += 1  # 인스턴스가 만들어질 때
#         # 클래스 속성 count에 1을 더함
#
#     @classmethod
#     def print_count(cls):
#         print('{0}명 생성되었습니다.'.format(cls.count))  # cls로 클래스 속성에 접근
#
#
# james = Person()
# maria = Person()
# durby = Person()
# crazy = Person()
#
# Person.print_count()  # 2명 생성되었습니다.

# class Game:
#     shared_items = []
#
#     def put_items(self, request):
#         return self.shared_items.append(request)
#
#     def delete_items(self, request):
#         return self.shared_items.remove(request)
#
#
# player1 = Game()
# player1.put_items('Sword')
# print(player1.shared_items)
#
# player2 = Game()
# player2.delete_items('Sword')
# print(player2.shared_items)

# player1 = Lineage.objects.put_items('Sword')
# print(player1.shared_items)


# class Person:
#     bag = []
#
#     def put_bag(self, stuff):
#         self.bag.append(stuff)
#
# james = Person()
# james.put_bag('책')
#
# maria = Person()
# maria.put_bag('열쇠')
#
# print(james.bag)
# print(maria.bag)