word = "bottles"   # 단어에 bottles을 입력
for beer_num in range(99, 0, -1):   # 넘버가 99부터 0까지 1씩 떨어지는 동안에
    print(beer_num, word, "of beer on the wall.")   # 갯수 + 단어 가 남아있다고 한다.
    print(beer_num, word, "of beer")   # 있다고 한다
    print("Take one down.")   # 
    print("Pass it around.")   # 
    if beer_num == 1:   # 만약 맥주가 1잔 남으면
        print("No more bottles of beer on the wall.")   # 더이상 남은 맥주가 없습니다.
    else:   # 1개보다 많으면
        new_num = beer_num - 1   # 새로운 숫자에 맥주 숫자를 대입한다.
        if new_num == 1:   # 만약 새로운 숫자가 1이면 (=맥주 숫자가 2면) 
            word = "bottle" 
        print(new_num, word, "of beer on the wall.")   # 더이상 남은 맥주가 없습니다.
    print()