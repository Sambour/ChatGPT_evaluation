import openai
import json
import jsonlines


def call_api(prompt: str) -> str:
    instruct = {"role": "system", "content": 'Strictly follow the input format. You must output the number in the end followed by "####".'}
    prediction = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}], 
                    max_tokens=500, stop="<stop>", temperature=0)
    return prediction['choices'][0]['message']['content']


def baseline(qa: dict) -> str:
    context = '''
Answer the questions follow the format below.
Question: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Answer: 72
<stop>
Question: A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?
Answer: 121
<stop>
Question: Bella bought stamps at the post office. Some of the stamps had a snowflake design, some had a truck design, and some had a rose design. Bella bought 11 snowflake stamps. She bought 9 more truck stamps than snowflake stamps, and 13 fewer rose stamps than truck stamps. How many stamps did Bella buy in all?
Answer: 38
<stop>
Question: Ann, Bill, Cate, and Dale each buy personal pan pizzas cut into 4 pieces. If Bill and Dale eat 50% of their pizzas and Ann and Cate eat 75% of the pizzas, how many pizza pieces are left uneaten?
Answer: 6
<stop>
Question: A concert ticket costs $40. Mr. Benson bought 12 tickets and received a 5% discount for every ticket bought that exceeds 10. How much did Mr. Benson pay in all?
Answer: 476
<stop>

'''
    prompt = 'Question: ' + qa['question'] + '\nAnswer:'
    prompt = context + prompt
    result = call_api(prompt)
    return result


def cot(qa: dict) -> str:
    context = '''
Answer the questions follow the format below.
Question: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Answer:
explanation: Natalia sold 48/2 = <<48/2=24>>24 clips in May.\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.
answer: #### 72
<stop>
Question: A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?
Answer:
explanation: Let S be the number of people on the first hundred years\u2019 ship.\nThe second hundred years\u2019 ship had twice as many as the first, so it had 2S people.\nThe third hundred years\u2019 ship had twice as many as the second, so it had 2 * 2S = <<2*2=4>>4S people.\nAll the ships had S + 2S + 4S = 7S = 847 people.\nThus, the ship that the monster ate in the first hundred years had S = 847 / 7 = <<847/7=121>>121 people on it.
answer: #### 121
<stop>
Question: Bella bought stamps at the post office. Some of the stamps had a snowflake design, some had a truck design, and some had a rose design. Bella bought 11 snowflake stamps. She bought 9 more truck stamps than snowflake stamps, and 13 fewer rose stamps than truck stamps. How many stamps did Bella buy in all?
Answer:
explanation: The number of truck stamps is 11 + 9 = <<11+9=20>>20.\nThe number of rose stamps is 20 \u2212 13 = <<20-13=7>>7.\nBella bought 11 + 20 + 7 = <<11+20+7=38>>38 stamps in all.
answer: #### 38
<stop>
Question: Ann, Bill, Cate, and Dale each buy personal pan pizzas cut into 4 pieces. If Bill and Dale eat 50% of their pizzas and Ann and Cate eat 75% of the pizzas, how many pizza pieces are left uneaten?
Answer:
explanation: In total, there are 4 x 4 = <<4*4=16>>16 pizza pieces.\nBill and Dale eat 2 x 4 x 50% = <<2*4*50*.01=4>>4 pieces.\nAnn and Cate eat 2 x 4 x 75% = <<2*4*75*.01=6>>6 pieces.\nThe four of them eat 4 + 6 = <<4+6=10>>10 pieces.\nThere are 16 - 10 = <<16-10=6>>6 pizza pieces uneaten.
answer: #### 6
<stop>
Question: A concert ticket costs $40. Mr. Benson bought 12 tickets and received a 5% discount for every ticket bought that exceeds 10. How much did Mr. Benson pay in all?
Answer:
explanation: Mr. Benson had a 5% discount for each of the 12 - 10 = <<12-10=2>>2 tickets.\nSo, those two tickets had a $40 x 5/100 = $<<40*5/100=2>>2 discount each.\nHence, each ticket cost $40 - $2 = $<<40-2=38>>38 each.\nThus, two discounted tickets amount to $38 x 2 = $<<38*2=76>>76.\nAnd the other ten tickets amount to $40 x 10 = $<<40*10=400>>400.\nHence, Mr. Benson paid a total of $400 + $76 = $<<400+76=476>>476.
answer: #### 476
<stop>

'''
    prompt = 'Question: ' + qa['question'] + '\nAnswer:'
    prompt = context + prompt
    result = call_api(prompt)
    # print(result)
    return result


if __name__ == "__main__":
    output_name = 'example_with_rationale.json'
    with open('total.json', 'r') as f:
        qas = json.load(f)
    
    predictions = []
    cnt = 186
    print('Total: ' + str(len(qas)))
    for qa in qas[cnt:]:
        print('Now Processing: ' + str(cnt))
        cnt += 1
        result = cot(qa).strip()
        prediction = {'question':qa['question'], 'rationale':qa['rationale'], 'answer':qa['answer'], 'prediction_rationale': result, 'prediction': result.split('\n')[-1]}
        predictions.append(prediction)

        with open(output_name, 'a') as f:
            json.dump(prediction, f)
            f.write('\n')
    
    print('Completed!')
    #with open(output_name, 'w') as f:
        #json.dump(predictions, f, indent=4)

    #score = evaluate(predictions, 'acc')
    #print(score)