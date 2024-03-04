from collections import deque
def main():
    #add code here
    food = deque(maxlen=5)
    food.append("APP001")
    print(food)
    ordered_food = ["APP02", "MAIN001", "DES001", "DES002"]
    food.extend(ordered_food)
    print(food)
    food.append("APP03")
    print(food)
    food.appendleft("MAIN002")
    print(food)
    return

if __name__ == "__main__":
    main()