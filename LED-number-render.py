# each number can be represented as a matrix

SYMBOL="#"
nums=list()
nums.append([[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]])
nums.append([[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]])
nums.append([[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]])
nums.append([[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]])
nums.append([[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]])
nums.append([[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]])
nums.append([[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]])
nums.append([[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]])
nums.append([[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]])
nums.append([[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]])


def render_col(num):
    for row in nums[num]:
        for element in row:
            #print(element, sep="")
            if element == 1:
                print(SYMBOL,sep="",end="")
            else:
                print(" ",sep="",end="")
        print()

def render_row(num):
    for row in range(5):
        for digit in num:
            for bit in nums[digit][row]:
                if(bit == 1):
                    print(SYMBOL,sep="",end="")
                else:
                    print(" ",sep="",end="")
            print(" ",end="")
        print()
    
def generate_digit_list(num):
    l = list()
    while(num > 0):
        l.append(num%10)
        num=num//10
    l.reverse()
    return l

print(generate_digit_list(9081726354))

n = int(input())
render_row(generate_digit_list(n))