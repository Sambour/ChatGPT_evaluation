import json
import jsonlines

def evaluate(predictions:list, total:int, method:str):
    if method == 'acc':
        score = 0
        for pred in predictions:
            if pred['answer'] == pred['prediction']:
                score += 1
        score /= total

        return score

if __name__ == "__main__":
    #with open('base_line_davinci.json', 'r') as f:
        #qas = json.load(f)
    
    with open('baseline.json', 'r+') as f:
        qas = jsonlines.Reader(f)
    
        in_scope = 0
        first_in_scope = 0
        dot_in_scope = 0
        neg_in_scope = 0
        rest = 0
        formated = []
        unformated = []
        total = []

        for qa in qas:
            if ',' in qa['answer']:
                qa['answer'] = qa['answer'].replace(',', '')
            if qa['prediction'].startswith('$'):
                qa['prediction'] = qa['prediction'][1:]
            if ',' in qa['prediction'] and qa['prediction'].split(',')[0].isdigit():
                qa['prediction'] = qa['prediction'].split(',')[0]
            if qa['prediction'].isdigit():
                in_scope += 1
                formated.append(qa)
                total.append(qa)
            elif qa['prediction'].split()[0].isdigit():
                first_in_scope += 1
                qa['prediction'] = qa['prediction'].split()[0]
                formated.append(qa)
                total.append(qa)
            elif '.' in qa['prediction'] and qa['prediction'].split('.')[0].isdigit():
                dot_in_scope += 1
                qa['prediction'] = qa['prediction'].split('.')[0]
                formated.append(qa)
                total.append(qa)
            elif qa['prediction'].startswith('-') and qa['prediction'][1:].isdigit():
                neg_in_scope += 1
                qa['prediction'] = qa['prediction'][1:]
                formated.append(qa)
                total.append(qa)
            elif qa['prediction'].endswith('%') and qa['prediction'][:-1].isdigit():
                neg_in_scope += 1
                qa['prediction'] = qa['prediction'][:-1]
                formated.append(qa)
                total.append(qa)
            else:
                unformated.append(qa)
                total.append(qa)
                rest += 1
    
    score = evaluate(total, len(total), 'acc')
    print(len(formated))
    print(len(unformated))
    print(in_scope)
    print(first_in_scope)
    print(dot_in_scope)
    print(rest)
    print(score)
    with open('total.json', 'w') as f:
        json.dump(total, f, indent=4)
    with open('unformated.json', 'w') as f:
        json.dump(unformated, f, indent=4)