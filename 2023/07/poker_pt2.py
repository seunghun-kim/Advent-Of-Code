from enum import Enum

lines = []
# with open("./2023/07/example.txt") as f:
with open("./2023/07/input.txt") as f:
    lines = f.readlines()

class HandType(Enum):
    FIVE_OF_A_KIND = 0
    FOUR_OF_A_KIND = 1
    FULL_HOUSE = 2
    THREE_OF_A_KIND = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH_CARD = 6

strengh_order = "AKQT98765432J"

def calc_type(hand):
    counts = []
    joker_count = hand.count('J')
    hand = hand.replace('J', '')
    while len(hand) > 0:
        counts.append(hand.count(hand[0]))
        hand = hand.replace(hand[0], '')
    counts.sort()
    if len(counts) == 0:
        counts.append(joker_count)
    else:
        counts[-1] += joker_count

    if 5 in counts:
        return HandType.FIVE_OF_A_KIND
    elif 4 in counts:
        return HandType.FOUR_OF_A_KIND
    elif 3 in counts:
        if 2 in counts:
            return HandType.FULL_HOUSE
        else:
            return HandType.THREE_OF_A_KIND
    elif 2 in counts:
        if counts.count(2) == 2:
            return HandType.TWO_PAIR
        else:
            return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD

def calc_rank(hand):
    # x.aabbccddee 형태로 등급을 표현.
    # 예를 들어,KK677은 TWO_PAIR이므로 x는 4
    # aabbccddee 각각 카드 5 장의 우선순위를 나타냄. 우선순위가 2자리일 수 있으므로 소수점 2자리씩 차지.
    # 0에 가까울수록 높은 등급의 카드
    hand_type = calc_type(hand)
    strength_list = [strengh_order.index(x) for x in hand]
    result = hand_type.value
    for i, val in enumerate(strength_list):
        result += pow(100, (i + 1) * -1) * val
    return result

hand_bid_list = []
for line in lines:
    hand, bid = line.strip().split(' ')
    hand_rank = calc_rank(hand)
    print("Hand {} is {}, rank = {}".format(hand, HandType(int(hand_rank)).name,hand_rank))
    hand_bid_list.append((hand_rank, hand, bid))

hand_bid_list.sort(reverse=True)
# print(hand_bid_list)

total_winnings = 0
for i in range(len(hand_bid_list)):
    total_winnings += int(hand_bid_list[i][2]) * (i + 1)
print(total_winnings)