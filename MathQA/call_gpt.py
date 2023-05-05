import openai
import json


def call_api(prompt: str) -> str:
    instruct = {"role": "system", "content": 'Strictly follow the input format. You must select one option from a, b, c, d, or e without any punctuation at the end with a new line.'}
    prediction = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}], 
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
a ) 1200 , b ) 120 , c ) 360 , d ) 240 , e ) none of these
Answer:
explanation : let the original no . of students be x . according to situation , 40 x + 120 * 32 = ( x + 120 ) 36 \u21d2 x = 120 so , required no . of students after joining the new students = x + 120 = 240 . therefore , d\n#### d
<stop>
Question: a rectangular floor that measures 15 meters by 18 meters is to be covered with carpet squares that each measure 3 meters by 3 meters . if the carpet squares cost $ 12 apiece , what is the total cost for the number of carpet squares needed to cover the floor ?
a ) $ 200 , b ) $ 240 , c ) $ 360 , d ) $ 960 , e ) $ 1,920
Answer:
the width of the rectangular floor ( 15 m ) is a multiple of one side of the square ( 3 m ) , and the length of the floor ( 18 m ) is also a multiple of the side of the square . so the number of carpets to cover the floor is ( 15 / 3 ) * ( 18 / 3 ) = 30 . the total cost is 30 * 12 = $ 360 . the answer is , therefore , c\n#### c
<stop>
Question: 6 workers should finish a job in 8 days . after 3 days came 4 workers join them . how many days m do they need to finish the same job ?
a ) 3 , b ) 4 , c ) 5 , d ) 6 , e ) 7
Answer:
let rate of one worker be r = > ( 6 * r ) * 8 = 1 ( rate * time = work ) = > r = 1 / 48 = > work remaining after 3 days 1 - ( 3 * 6 ) / 48 = 30 / 48 after 4 ppl joined in ( ( 6 + 4 ) * time ) / 48 = 30 / 48 time m = 3 days to finish the task imo a\n#### a
<stop>
Question: the banker ' s gain of a certain sum due 3 years hence at 10 % per annum is rs . 36 . what is the present worth ?
a ) rs . 400 , b ) rs . 300 , c ) rs . 500 , d ) rs . 350 , e ) none of these
Answer:
explanation : t = 3 years r = 10 % td = ( bg \u00d7 100 ) / tr = ( 36 \u00d7 100 ) / ( 3 \u00d7 10 ) = 12 \u00d7 10 = rs . 120 td = ( pw \u00d7 tr ) / 100 \u21d2 120 = ( pw \u00d7 3 \u00d7 10 ) / 100 \u21d2 1200 = pw \u00d7 3 pw = 1200 / 3 = rs . 400 . therefore , a\n#### a
<stop>
Question: a gardener is going to plant 2 red rosebushes and 2 white rosebushes . if the gardener is to select each of the bushes at random , one at a time , and plant them in a row , what is the probability that the 2 rosebushes in the middle of the row will be the red rosebushes ?
a ) 1 / 12 , b ) 1 / 6 , c ) 1 / 5 , d ) 1 / 3 , e ) ½
Answer:
we are asked to find the probability of one particular pattern : wrrw . total # of ways a gardener can plant these four bushes is the # of permutations of 4 letters wwrr , out of which 2 w ' s and 2 r ' s are identical , so 4 ! / 2 ! 2 ! = 6 ; so p = 1 / 6 . therefore , b\n#### b
<stop>
Question: what is the number of integers from 1 to 1100 ( inclusive ) that are divisible by neither 11 nor by 35 ?
a ) 884 , b ) 890 , c ) 892 , d ) 910 , e ) 945
Answer:
normally , i would use the method used by bunuel . it ' s the most accurate . but if you are looking for a speedy solution , you can use another method which will sometimes give you an estimate . looking at the options ( most of them are spread out ) , i wont mind trying it . ( mind you , the method is accurate here since the numbers start from 1 . ) in 1000 consecutive numbers , number of multiples of 11 = 1000 / 11 = 90 ( ignore decimals ) in 1000 consecutive numbers , number of multiples of 35 = 1000 / 35 = 28 number of multiples of 11 * 35 i . e . 385 = 1000 / 385 = 2 number of integers from 1 to 1000 that are divisible by neither 11 nor by 35 = 1000 - ( 90 + 28 - 2 ) { using the concept of sets here ) = 945 think : why did i say the method is approximate in some cases ? think what happens if the given range is 11 to 1010 both inclusive ( again 1000 numbers ) what is the number of multiples in this case ? therefore, e\n#### e
<stop>

'''
    prompt = 'Question: ' + qa['Problem'] + '\n' + qa['options'] + '\nAnswer:'
    prompt = context + prompt
    result = call_api(prompt)
    # print(result)
    return result


def modified_cot(qa: dict) -> str:
    context = '''
Question: average age of students of an adult school is 40 years . 120 new students whose average age is 32 years joined the school . as a result the average age is decreased by 4 years . find the number of students of the school after joining of the new students .
a ) 1200 , b ) 120 , c ) 360 , d ) 240 , e ) none of these
Following what steps can we solve this problem?
1. Understand the problem: We are given the average age of students in an adult school and the average age decreases by 4 years when 120 new students join the school. We need to find the number of students in the school after the new students join.\n\n2. Set up equations: Let x be the number of students in the school before the new students join. Then, we can set up the following equation based on the given information:\n\n(40x + 32*120)/(x + 120) = 36\n\nThis equation represents the fact that the average age decreases by 4 years when the new students join.\n\n3. Solve for x: We can simplify the equation as follows:\n\n40x + 3840 = 36x + 4320\n4x = 480\nx = 120\n\nTherefore, there were 120 students in the school before the new students joined.\n\n4. Find the total number of students: We can find the total number of students after the new students join by adding the number of new students to the original number of students:\n\nTotal number of students = 120 + 120 = 240\n\nTherefore, the answer is d.
Answer: d
<stop>
Question: a rectangular floor that measures 15 meters by 18 meters is to be covered with carpet squares that each measure 3 meters by 3 meters . if the carpet squares cost $ 12 apiece , what is the total cost for the number of carpet squares needed to cover the floor ?
a ) $ 200 , b ) $ 240 , c ) $ 360 , d ) $ 960 , e ) $ 1,920
Following what steps can we solve this problem?
1. Understand the problem: We are given the dimensions of a rectangular floor and the cost of each carpet square. We need to find the total cost of the carpet squares needed to cover the floor.\n\n2. Determine the number of carpet squares needed: We can determine the number of carpet squares needed by dividing the area of the floor by the area of each carpet square:\n\nNumber of carpet squares = (15 x 18) / (3 x 3) = 30\n\n3. Calculate the total cost: We can calculate the total cost by multiplying the number of carpet squares by the cost per square:\n\nTotal cost = 30 x $12 = $360\n\nTherefore, the answer is c.
Answer: c
<stop>
Question: 6 workers should finish a job in 8 days . after 3 days came 4 workers join them . how many days m do they need to finish the same job ?
a ) 3 , b ) 4 , c ) 5 , d ) 6 , e ) 7
Following what steps can we solve this problem?
1. Understand the problem: We are given the number of workers and the time it takes for them to finish a job. After a certain number of days, additional workers join the team and we need to find the new time it takes to finish the job.\n\n2. Calculate the rate of work: We can calculate the rate of work per worker per day by dividing the total work by the number of workers and the number of days:\n\nRate of work = 1 / (6 x 8) = 1 / 48\n\n3. Calculate the work done in the first 3 days: We can calculate the work done by the 6 workers in the first 3 days as follows:\n\nWork done in 3 days = (6 x 3 x 1/48) = 18/48 = 3/8\n\n4. Calculate the remaining work: We can calculate the remaining work as follows:\n\nRemaining work = 1 - 3/8 = 5/8\n\n5. Calculate the new rate of work per worker per day: We can calculate the new rate of work per worker per day by adding the number of workers who joined and multiplying by the original rate of work per worker per day:\n\nNew rate of work per worker per day = (6 + 4) x 1 / 48 = 10 / 48 = 5/24\n\n6. Calculate the new time to finish the job: We can calculate the new time to finish the job by dividing the remaining work by the new rate of work per worker per day:\n\nNew time to finish the job = (5 / 8) / (5 / 24) = 3 days\n\nTherefore, the answer is a.
Answer: a
<stop>
Question: an empty fuel tank with a capacity of 218 gallons was filled partially with fuel a and then to capacity with fuel b . fuel a contains 12 % ethanol by volume and fuel b contains 16 % ethanol by volume . if the full fuel tank contains 30 gallons of ethanol , how many gallons of fuel a were added ?
a ) 122 , b ) 150 , c ) 100 , d ) 80 , e ) 50
Following what steps can we solve this problem?
1. Understand the problem: We are given information about the ethanol content of two types of fuel and the total amount of ethanol in a full fuel tank. We need to find the amount of fuel A added to the tank.\n\n2. Set up equations: Let x be the amount of fuel A added to the tank. Then, we can set up the following equation based on the given information:\n\n0.12x + 0.16(218 - x) = 30\n\nThis equation represents the fact that the total amount of ethanol in the tank is 30 gallons.\n\n3. Solve for x: We can simplify the equation as follows:\n\n0.12x + 34.88 - 0.16x = 30\n-0.04x = -4.88\nx = 122\n\nTherefore, 122 gallons of fuel A were added to the tank.\n\n4. Check the answer: We can check our answer by verifying that the total amount of ethanol in the tank is indeed 30 gallons:\n\n0.12(122) + 0.16(218 - 122) = 14.64 + 18.88 = 33.52\n\nThis is slightly more than 30 gallons, but this is likely due to rounding errors in the given ethanol percentages and volumes.\n\nTherefore, the answer is a.\nAnswer: a
Answer: a
<stop>
Question: a gardener is going to plant 2 red rosebushes and 2 white rosebushes . if the gardener is to select each of the bushes at random , one at a time , and plant them in a row , what is the probability that the 2 rosebushes in the middle of the row will be the red rosebushes ?
a ) 1 / 12 , b ) 1 / 6 , c ) 1 / 5 , d ) 1 / 3 , e ) ½
Following what steps can we solve this problem?
1. Understand the problem: We are given information about the colors of rosebushes and the probability of selecting certain combinations. We need to find the probability of a specific combination.\n\n2. Determine the total number of possible combinations: There are 4 rosebushes, so there are 4! = 24 possible ways to arrange them in a row.\n\n3. Determine the number of ways the red rosebushes can be in the middle: The red rosebushes can be in the middle in four ways: W1R1R2W2, W1R2R1W2, W2R1R2W1, or W2R2R1W1.\n\n4. Determine the probability: The probability of the red rosebushes being in the middle is the number of ways they can be in the middle divided by the total number of possible combinations:\n\nProbability = 4/24 = 1/6\n\nTherefore, the answer is b.\nAnswer: b
Answer: b
<stop>
Question: what is the number of integers from 1 to 1000 ( inclusive ) that are divisible by neither 11 nor by 35 ?
a ) 884 , b ) 890 , c ) 892 , d ) 910 , e ) 945
Following what steps can we solve this problem?
1. Understand the problem: We are given a range of integers and we need to find the number of integers in that range that are not divisible by 11 or 35.\n\n2. Determine the number of multiples of 11: We can determine the number of multiples of 11 in the range by dividing the endpoints by 11 and rounding down:\n\nNumber of multiples of 11 = floor(1000/11) = 90\n\n3. Determine the number of multiples of 35: We can determine the number of multiples of 35 in the range by dividing the endpoints by 35 and rounding down:\n\nNumber of multiples of 35 = floor(1000/35) = 28\n\n4. Determine the number of multiples of 385: We can determine the number of multiples of 385 in the range by dividing the endpoints by 385 and rounding down:\n\nNumber of multiples of 385 = floor(1000/385) = 2\n\n5. Determine the number of integers not divisible by 11 or 35: We can use the principle of inclusion-exclusion to determine the number of integers not divisible by 11 or 35:\n\nNumber of integers not divisible by 11 or 35 = 1000 - (90 + 28 - 2) = 945\n\nTherefore, the answer is e.\nAnswer: e
Answer: e
<stop>

'''
    prompt = 'Question: ' + qa['Problem'] + '\n' + qa['options'] + '\nFollowing what steps can we solve this problem?\n'
    prompt = context + prompt
    result = call_api(prompt)
    # print(result)
    return result


if __name__ == "__main__":
    output_name = 'example_with_rationale_mod.json'
    with open('data/test.json', 'r') as f:
        qas = json.load(f)
    
    predictions = []
    cnt = 0
    print('Total: ' + str(len(qas)))
    for qa in qas[cnt:]:
        print('Now Processing: ' + str(cnt))
        cnt += 1
        result = modified_cot(qa).strip()
        prediction = {'Problem':qa['Problem'], 'Rationale':qa['Rationale'],
                      'options':qa['options'], 'correct':qa['correct'],
                      'annotated_formula':qa['annotated_formula'], 'linear_formula':qa['linear_formula'],
                      'category':qa['category'], 'predicted_rational': result, 'prediction': result[-1]}
        predictions.append(prediction)

        with open(output_name, 'a') as f:
            json.dump(prediction, f)
            f.write('\n')
    
    print('Completed!')
    #with open(output_name, 'w') as f:
        #json.dump(predictions, f, indent=4)

    #score = evaluate(predictions, 'acc')
    #print(score)