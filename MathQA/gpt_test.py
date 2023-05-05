import openai
import json


def call_api(prompt: str) -> str:
    instruct = {"role": "system", "content": 'Strictly follow the input format. You must select one option from a, b, c, d, or e that best fit the answer? List each intermediate step in calculation and equation solving.'}
    prediction = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[instruct, {"role": "user", "content": prompt}], 
                    max_tokens=500, stop="<stop>", temperature=0)
    return prediction['choices'][0]['message']['content']


def baseline(qa: dict) -> str:
    context = '''
Question: average age of students of an adult school is 40 years . 120 new students whose average age is 32 years joined the school . as a result the average age is decreased by 4 years . find the number of students of the school after joining of the new students .
a ) 1200 , b ) 120 , c ) 360 , d ) 240 , e ) none of these
Answer: d
<stop>
Question: a rectangular floor that measures 15 meters by 18 meters is to be covered with carpet squares that each measure 3 meters by 3 meters . if the carpet squares cost $ 12 apiece , what is the total cost for the number of carpet squares needed to cover the floor ?
a ) $ 200 , b ) $ 240 , c ) $ 360 , d ) $ 960 , e ) $ 1,920
Answer: c
<stop>
Question: 6 workers should finish a job in 8 days . after 3 days came 4 workers join them . how many days m do they need to finish the same job ?
a ) 3 , b ) 4 , c ) 5 , d ) 6 , e ) 7
Answer: a
<stop>
Question: the banker ' s gain of a certain sum due 3 years hence at 10 % per annum is rs . 36 . what is the present worth ?
a ) rs . 400 , b ) rs . 300 , c ) rs . 500 , d ) rs . 350 , e ) none of these
Answer: a
<stop>
Question: a gardener is going to plant 2 red rosebushes and 2 white rosebushes . if the gardener is to select each of the bushes at random , one at a time , and plant them in a row , what is the probability that the 2 rosebushes in the middle of the row will be the red rosebushes ?
a ) 1 / 12 , b ) 1 / 6 , c ) 1 / 5 , d ) 1 / 3 , e ) ½
Answer: b
<stop>
Question: what is the number of integers from 1 to 1100 ( inclusive ) that are divisible by neither 11 nor by 35 ?
a ) 884 , b ) 890 , c ) 892 , d ) 910 , e ) 945
Answer: e
<stop>

'''
    prompt = 'Question: ' + qa['Problem'] + '\n' + qa['options'] + '\nAnswer:'
    prompt = context + prompt
    result = call_api(prompt)
    return result


def cot(qa: dict) -> str:
    context = '''
Question: average age of students of an adult school is 40 years . 120 new students whose average age is 32 years joined the school . as a result the average age is decreased by 4 years . find the number of students of the school after joining of the new students .
a ) 1200 , b ) 120 , c ) 360 , d ) 240 , e ) 180
Following what steps can we solve this problem?
1. Understand the problem: We are given the average age of students in an adult school and the average age decreases by 4 years when 120 new students join the school. We need to find the number of students in the school after the new students join.\n\n2. Set up equations: Let x be the number of students in the school before the new students join. Then, we can set up the following equation based on the given information:\n\n(40x + 32*120)/(x + 120) = 36\n\nThis equation represents the fact that the average age decreases by 4 years when the new students join.\n\n3. Solve for x: We can simplify the equation as follows:\n\n40x + 3840 = 36x + 4320\n4x = 480\nx = 120\n\nTherefore, there were 120 students in the school before the new students joined.\n\n4. Find the total number of students: We can find the total number of students after the new students join by adding the number of new students to the original number of students:\n\nTotal number of students = 120 + 120 = 240\n\nTherefore, the answer is d.
Answer: d
<stop>

'''
    prompt = 'Question: ' + qa['Problem'] + '\n' + qa['options'] + '\nFollowing what steps can we solve this problem?'
    prompt = context + prompt
    result = call_api(prompt)
    # print(result)
    return result


if __name__ == "__main__":
    output_name = 'calc_and_understand_on_formated.json'
    predictions = []
    cnt = 0
    with open('formated.json', 'r') as f:
        qas = json.load(f)
    for qa in qas:
        if qa['prediction'] != qa['correct']:
            print(cnt)
            result = cot(qa).strip()
            prediction = {'Problem':qa['Problem'], 'Rationale':qa['Rationale'],
                            'options':qa['options'], 'correct':qa['correct'],
                            'annotated_formula':qa['annotated_formula'], 'linear_formula':qa['linear_formula'],
                            'category':qa['category'], 'predicted_rational': result, 'prediction': result[-1]}
            predictions.append(prediction)

            with open(output_name, 'a') as f:
                json.dump(prediction, f)
                f.write('\n')
        cnt += 1
        #print(result)
    #with open(output_name, 'w') as f:
        #json.dump(prediction, f, indent=4)

    #score = evaluate(predictions, 'acc')
    #print(score)