s1 = {1, 2, 3, 4}
s2 = {2, 4, 6, 8}

while True:
    print("""
    1. Union
    2. Intersection
    3. Is Disjoint
    4. Subset
    5. Pop
    6. Length
    7. Remove
    8. Add
    9. Equality
    10. Membership
    11. Exit
    """)
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        print("Union of sets:", s1.union(s2))
    elif ch == 2:
        print("Intersection of sets:", s1.intersection(s2))
    elif ch == 3:
        print("Are sets disjoint?", s1.isdisjoint(s2))
    elif ch == 4:
        print("Is s1 a subset of s2?", s1.issubset(s2))
    elif ch == 5:
        s1.pop()
        print("After pop, s1:", s1)
    elif ch == 6:
        print("Length of s1:", len(s1))
    elif ch == 7:
        ele = int(input("Enter element to remove: "))
        if ele in s1:
            s1.remove(ele)
            print("After removal, s1:", s1)
        else:
            print(f"Element {ele} not found in s1")
    elif ch == 8:
        ele = int(input("Enter element to add: "))
        s1.add(ele)
        print("After adding, s1:", s1)
    elif ch == 9:
        print("Are s1 and s2 equal?", s1 == s2)
    elif ch == 10:
        e = int(input("Enter element to check: "))
        print("Is the element in s1?", e in s1)
    elif ch == 11:
        break
    else:
        print("Invalid choice")
