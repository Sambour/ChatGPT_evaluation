import json

fo = open('sampled_test.txt', 'w')


with open('test.txt', 'r') as f:
    file = f.readlines()
    n = 1
    l = 0
    max = 0
    count = 0
    count4 = 0
    nc =  0

    wc = 0
    mxwc = 0
    for line in file:
        if count%3 ==0:
            fo.write(line);
            nc +=1
        line = json.loads(line)
        text = line['options']
        context = line['text']
        t = len(context.split(" "))
        wc += t
        if t>mxwc:
            mxwc = wc
        if len(text)==4:
            count4 += 1
        for option in text:
            s = 0
            l = l + len(option.split(" "))
            s = s + len(option.split(" "))
            n += 1
            if s >= max:
                max = s
        count+=1

    result = l/n
    print(count4)
    print(nc)
    print(result)
    print(max)

    print(wc/len(file))
    print(mxwc)
