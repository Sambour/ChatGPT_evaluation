import json
Opts = ['A', 'B', 'C', 'D']

cnt = 0
with open('sampled_test.txt', 'r') as f:
    file = f.readlines()
    for line in file:
        cnt += 1
        if (cnt%50 != 0):
            continue
        line = json.loads(line)
        context =  line['text']
        answer = line['answer']
        question = line['question']
        options = line['options']
        print('Context:',context)
        print('Question:', question)
        print('Answer Options:')
        for i, opt in enumerate(options):
            print(Opts[i]+':', opt)

        print('Correct Answer:', Opts[answer])
        print('<stop>')
