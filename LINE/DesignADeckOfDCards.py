"""
Constraints and assumptions
Is this a generic deck of cards for games like poker and black jack?
    Yes, design a generic deck then extend it to black jack
Can we assume the deck has 52 cards (2-10, Jack, Queen, King, Ace) and 4 suits?
    Yes
Can we assume inputs are valid or do we have to validate them?
    Assume they're valid
"""

from enum import Enum, auto
import random
import sys

class Suit(Enum):
    SPADE = auto()
    HEART = auto()
    DIA = auto()
    CLUB = auto()

class Val(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card():
    def __init__(self, val, suit):
        self.suit = suit
        self.val = val

class Deck():
    def __init__(self,):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def draw(self):
        if len(self.cards) > 0:
            card = self.cards.pop(0)
            return card
        else:
            # エラー投げるか
            raise Error("カードがありません")
    
    def shuffle(self):
        random.shuffle(self.cards)

    def info(self):
        print("今のデッキはカードが {}枚存在しています".format(len(self.cards)))

class Hands():
    def __init__(self):
        self.cards = []
    
    def draw(self, deck):
        card = deck.draw()
        self.cards.append(card)
    
    def pullOut(self, field, index):
        card = deck.pop(index)
        field.pusu(card)

    def info(self):
        print("今の手札はカードが {}枚存在しています".format(len(self.cards)))
        print("カードの詳細情報は")
        for card in self.cards:
            print("絵柄： {}, 値：　{}".format(card.suit, card.val))
    
    def total(self):
        total_val = 0
        for card in self.cards:
            if card.val.value == 1:
                print("Aを1として使うなら1を、11として使うなら2を選択してください")
                howUse = int(input())
                if howUse == 1:
                    total_val += 1
                elif howUse == 2:
                    total_val += 11
                else:
                    print("値が不正です")
                    sys.exit()
            else:
                total_val += card.val.value
        return total_val

class Field():
    def __init__(self):
        self.semetary = []
        self.fields = []
    
    def push(self, card):
        self.fields.append(card)
    
    def clear(self):
        self.semetary.extend(self.fields)
        self.fields = []
    
    def info(self):
        print("今の場ははカードが {}枚存在しています".format(self.fields))
        if len(self.fields) > 0:
            print("場のトップカードは {}:{} です".format(self.fields[0].suit, self.fields[0].val))
        print("今の墓地はカードが {}枚存在しています".format(self.semetary))

# デッキの初期化
deck = Deck()
for val in Val:
    for suit in Suit:
        card = Card(val, suit)
        deck.add(card)

deck.shuffle()
deck.info()

if __name__ == "__main__":
    print("Game Start")
    hand = Hands()
    while True:
        # カードをひく
        hand.draw(deck)
        
        # 情報をみる
        hand.info()

        # 勝負する、もう一回引く
        print("勝負するなら1を、もう一回引くなら2を選択してください")
        is_battle = int(input())
        if is_battle == 1:
            break
        elif is_battle != 2:
            print("値が不正です")
            sys.exit()
    
print(hand.total())
    