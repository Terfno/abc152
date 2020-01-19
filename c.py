def main():
    N = int(input())
    iP = input().split(' ')

    P = [int(p) for p in iP]

    count = 0
    flag = 0
    for i in range(N):
        flag = 0
        for j in range(i):
            if(P[i] > P[j]):
                flag = 1
                break
        if(flag == 0):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
