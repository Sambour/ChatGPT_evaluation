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
    
    with open('example_with_rationale.json', 'r+') as f:
        qas = jsonlines.Reader(f)
    
        in_scope = 0
        space_in_scope = 0
        frac_in_scope = 0
        comma_in_scope = 0
        rest = 0
        formated = []
        unformated = []
        total = []

        for qa in qas:
            qa['prediction'] = qa['prediction_rationale'].split('\n')[-1]
            if not qa['prediction'].isdigit() and '#### ' in qa['prediction']:
                    qa['prediction'] = qa['prediction'].split('#### ')[1].split()[0]
            if ',' in qa['prediction']:
                    qa['prediction'] = qa['prediction'].replace(',', '')
            if qa['prediction'].isdigit():
                in_scope += 1
                formated.append(qa)
                total.append(qa)
            elif ' ' in qa['prediction'] and qa['prediction'].split()[0].isdigit():
                space_in_scope += 1
                qa['prediction'] = qa['prediction'].split()[0]
                formated.append(qa)
                total.append(qa)
            elif qa['prediction'].endswith('.00') or qa['prediction'].endswith(':00'):
                frac_in_scope += 1
                qa['prediction'] = qa['prediction'][:-3]
                formated.append(qa)
                total.append(qa)
            elif qa['prediction'].endswith('%'):
                frac_in_scope += 1
                qa['prediction'] = qa['prediction'][:-1]
                formated.append(qa)
                total.append(qa)
            elif qa['prediction'].startswith('-') or qa['prediction'].startswith('$') and qa['prediction'][1:].isdigit():
                in_scope += 1
                qa['prediction'] = qa['prediction'][1:]
                formated.append(qa)
                total.append(qa)
            elif ',' in qa['prediction'] and qa['prediction'].replace(',', '').isdigit():
                comma_in_scope += 1
                qa['prediction'] = qa['prediction'].replace(',', '')
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
    print(rest)
    print(score)
    #with open('formated.json', 'w') as f:
        #json.dump(formated, f, indent=4)
    #with open('rationale_unformated.json', 'w') as f:
        #json.dump(unformated, f, indent=4)