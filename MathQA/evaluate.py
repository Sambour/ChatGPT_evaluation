import json
import jsonlines

def evaluate(predictions:list, total:int, method:str):
    if method == 'acc':
        score = 0
        scores = {'geometry': 0, 'physics': 0, 'general': 0, 'gain': 0, 'probability': 0, 'other': 0}
        nums = {'geometry': 0, 'physics': 0, 'general': 0, 'gain': 0, 'probability': 0, 'other': 0}
        for pred in predictions:
            nums[pred['category']] += 1
            if pred['correct'] == pred['prediction']:
                score += 1
                scores[pred['category']] += 1
        score /= total
        scores = {c:(s/nums[c]) for c, s in scores.items()}
        scores['total'] = score

        return scores

if __name__ == "__main__":
    #with open('base_line_davinci.json', 'r') as f:
        #qas = json.load(f)
    
    with open('calc_and_understand_on_formated.json', 'r+') as f:
        qas = jsonlines.Reader(f)
    
        in_scope = 0
        dot_in_scope = 0
        answer_is_in_scope = 0
        option_in_scope = 0
        word_in_scope = 0
        rest = 0
        scope = ['a', 'b', 'c', 'd', 'e']
        formated = []
        unformated = []
        total = []

        for qa in qas:
            if qa['prediction'] in scope:
                in_scope += 1
                formated.append(qa)
                total.append(qa)
            elif qa['prediction'] == '.' and qa['predicted_rational'][:-1].split()[-1].strip(' ()').lower() in scope:
                dot_in_scope += 1
                qa['prediction'] = qa['predicted_rational'][:-1].split()[-1].strip(' ()').lower()
                formated.append(qa)
                total.append(qa)
            elif 'answer is ' in qa['predicted_rational'] and qa['predicted_rational'][qa['predicted_rational'].find('answer is ') + len('answer is '):].split()[0].strip(' ()').lower() in scope:
                answer_is_in_scope += 1
                qa['prediction'] = qa['predicted_rational'][qa['predicted_rational'].find('answer is ') + len('answer is '):].split()[0].strip(' ()').lower()
                formated.append(qa)
                total.append(qa)
            elif 'option ' in qa['predicted_rational'] and qa['predicted_rational'][qa['predicted_rational'].find('option ') + len('option '):].split()[0].strip(' ()').lower() in scope:
                option_in_scope += 1
                qa['prediction'] = qa['predicted_rational'][qa['predicted_rational'].find('option ') + len('option '):].split()[0].strip(' ()').lower()
                formated.append(qa)
                total.append(qa)
            else:
                qa['last 50'] = qa['predicted_rational'][-50:]
                last_split = qa['last 50'].strip('abcde ').split()
                flag = False
                for word in last_split:
                    if word.strip('(),. ').lower() in scope:
                        word_in_scope += 1
                        qa['prediction'] = word.strip('(),. ').lower()
                        formated.append(qa)
                        total.append(qa)
                        flag = True
                        break
                if not flag:
                    unformated.append(qa)
                    total.append(qa)
                    rest += 1
    
    score = evaluate(total, len(total), 'acc')
    print(len(formated))
    print(len(unformated))
    print(in_scope)
    print(dot_in_scope)
    print(answer_is_in_scope)
    print(option_in_scope)
    print(word_in_scope)
    print(rest)
    print(score)
    #with open('formated.json', 'w') as f:
        #json.dump(formated, f, indent=4)
    #with open('unformated.json', 'w') as f:
        #json.dump(unformated, f, indent=4)