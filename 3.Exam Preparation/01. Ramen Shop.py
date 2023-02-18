from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])


while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()
    if bowl == customer:
        continue
    elif bowl > customer:

        bowls_of_ramen.append(bowl - customer)
    elif customer > bowl:

        customers.appendleft(customer - bowl)

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print("Bowls of ramen left: ", end='')
        print(*bowls_of_ramen, sep=", ")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left: ", end='')
    print(*customers, sep=', ')
