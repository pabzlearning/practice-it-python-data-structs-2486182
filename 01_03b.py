from collections import Counter

def main():
    #Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)

    print(inventory)

    inventory.subtract(STA001=5)
    inventory.subtract(SAL002=20)
    inventory.subtract(ENT004=13)

    print(inventory)

    inventory.update(STA001=9)
    inventory.update(ENT004=1)

    
    #sell 5 starters, 3 salads, and 3 entrees
    #make 9 more starters and 1 more entree
    print(inventory)

if __name__ == "__main__":
    main()