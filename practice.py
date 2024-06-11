import random

# 게임 반복 여부
play_again = True

while play_again:
  # 플레이어 선택
  player_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")

  # 컴퓨터 선택
  computer_choice = random.choice(["가위", "바위", "보"])

  # 승패 판정
  if player_choice == computer_choice:
    print("비겼습니다!")
  elif (player_choice == "가위" and computer_choice == "보") or \
       (player_choice == "바위" and computer_choice == "가위") or \
       (player_choice == "보" and computer_choice == "바위"):
    print("이겼습니다!")
  else:
    print("졌습니다!")

  # 다시 플레이 여부
  play_again = input("한 번 더 하시겠습니까? (Y/N): ").upper() == "Y"
