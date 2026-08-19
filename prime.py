def prime(array):
    for num in array:
        if num <= 1:
            continue
        is_prime = True

        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            
array = [1,2,3,4,5,6]
prime(array)