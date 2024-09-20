def fizz_buzz_with_sum(n):
    prev_sum=0
    for i in range(1, n+1):
        curr_val=prev_sum+i  
        prev_sum=curr_val
        if curr_val%3==0 and curr_val%5==0:
            print(f"{curr_val}: FizzBuzz")
        elif curr_val%3==0:
            print(f"{curr_val}: Fizz")
        elif curr_val%5==0:
            print(f"{curr_val}: Buzz")
        else:
            print(curr_val)
fizz_buzz_with_sum(30)