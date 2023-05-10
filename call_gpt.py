import openai
import json
import time
import openai
import sklearn
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

openai.api_key = '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'


context = '''
Context: A fourteen-year study of finches on the Galapagos islands concluded that there is a definite relationship between climate and the population size of finch species that thrive at various times. During droughts, more members of large finch species survive because their bills are large enough to crack large, hard seeds, giving them a food supply unavailable to smaller birds. In rainy years, fewer members of the large finch species survive because the additional moisture fosters the growth of plants that produce small seeds. The larger finch varieties have to consume enormous numbers of small seeds to meet their energy demands, and some just cannot eat them fast enough.
Question: Which one of the following must be assumed in order to justify the conclusion that climatic variations cause a major difference in survival rates of small and large finches?
Answer Options:
A: During drought conditions, the weather promotes the growth of plants that produce small, hard seeds.
B: A lengthy period of rainy weather results in fewer large, hard seeds being produced.
C: In rainy periods, the small finches gather enough food to grow much larger and heavier, but their ultimate size is limited by their inability to eat small seeds fast.
D: The Galapagos climate during this fourteen- year period had about as much dry weather as it had wet weather.
Correct Answer: B
<stop>
Context: Commentary marketing refers to a marketing model in which merchants use reviews of products and services to guide customers' consumption tendency and promote product promotion and sales.
Question: Which of the following is commentary marketing?
Answer Options:
A: A research institute of traditional Chinese medicine held a series of public welfare lectures on traditional Chinese medicine ointment prescriptions. many plaster beneficiaries spoke personally, which aroused the concern of many citizens, and the plasters in pharmacies also sold well
B: A shopping website set up a reputation evaluation mechanism for buyers to help sellers screen customers with malicious bad reviews and put them on the blacklist, which quickly increased the turnover of the store
C: After a restaurant launched the activity of collecting praise for lobster, nearly 2,000 fans questioned its activity rules and lobster quality, and its turnover dropped sharply
D: A well-known household appliance company has launched a new product, and the professional evaluation of experts in the industry is prominently printed on the outer package. as soon as the product is put on the market, it is very popular
Correct Answer: D
<stop>
Context: All unemployed artists are sympathetic to social justice. And no employed artists are interested in the prospect of great personal fame.
Question: If the claims made above are true, then which one of the following must be true?
Answer Options:
A: If an artist is sympathetic to social justice, that artist is unemployed.
B: If there are artists interested in the prospect of great personal fame, they are sympathetic to social justice.
C: All artists are either sympathetic to social justice or are interested in the prospect of great personal fame.
D: All artists uninterested in the prospect of great personal fame are sympathetic to social justice.
Correct Answer: B
<stop>
Context: There are four siblings A B C D. A said D is the youngest sister. B said there is only one boy among the siblings, and C said I am A's sister.
Question: If all of the above is true, which of the following is true?
Answer Options:
A: A is second, it's a boy; B is third, it's a girl.
B: B is second, it's a girl; C is first, it's a girl.
C: C is second, it's a girl; D is fourth, it's a girl.
D: A is second, it's a girl; C is first, it's a girl.
Correct Answer: A
<stop>
Context: A crime research report revealed that 60% of serious criminal cases in a city in the past three years were committed by 350 habitual criminals on record. The report also reveals that more than half of the perpetrators of serious criminal cases are also drug addicts.
Question: If the above assertions are true, which of the following options must be true?
Answer Options:
A: There may be no drug addicts among the 350 habitual criminals.
B: Among the 350 habitual criminals, there must be drug addicts.
C: Most of the 350 habitual criminals are drug addicts.
D: Most of the drug addicts are among 350 habitual criminals.
Correct Answer: A
<stop>
Context: A telescopic adaptive control system can perform different control functions according to the model, quantity and sequence of system components. The control system can only be composed of several of the five components A, B, C, D and E in order from left to right, and the combination of components into the control system must comply with the following laws: (1) two or more components can form the control system, and the components of the system can be the same or different; (2) Component A cannot appear on the leftmost side of the control system; (3) If component B exists in the system, it appears more than once; (4) In the control system, C can neither be the last component nor the penultimate component; (5) As long as component a appears, component B must appear; (6) If e is the last component, component B must appear.
Question: Which of the followings is the possible composition of the control system?
Answer Options:
A: ABBD
B: BECB
C: CBBE
D: DCAE
Correct Answer: C
<stop>
Context: Congress has passed a law that scales back the tax credits offered to purchasers of hybrid cars. Because of this, the number of hybrid cars sold each year, which has approximately doubled in each of the last five years, is likely to flatten in the next few years.
Question: Which of the following statements, if true, most weakens the conclusion that the number of hybrid cars sold annually is likely to flatten in the next few years?
Answer Options:
A: Manufacturers have significantly increased their budgets for advertisements touting the fuel efficiency of hybrid cars.
B: Hybrid vehicles have a reputation for having less power than comparable non-hybrid vehicles.
C: Most people buy hybrid cars for reasons other than to save money in the long run.
D: Gasoline prices are projected to fall over the next few years.
Correct Answer: C
<stop>
Context: The basic attribution error is that people often attribute other people's behavior to personality or attitude, but ignore the importance of their situation.
Question: Which of the following is basic attribution error?
Answer Options:
A: Xiao Zhang didn't do well in the exam. He felt really stupid
B: Xiao Zhang did not do well in the exam. He thought that it was not that he did not study well, but that the teacher's questions were too out of line
C: Xiao Li lost his wallet on the street, came back to regret his carelessness, and his classmate Xiao Zhang comfort him that it is only environmental problems, here is a lot of thieves
D: Xiao Li examination did not test well, Xiao Zhang that must be Xiao Li usually do not work hard, and in fact Xiao Li recently something happened at home, some of his emotional impact
Correct Answer: D
<stop>
Context: The newly extruded milk contains lysozyme and other antibacterial active ingredients. The lysozyme activity of a cup of raw milk was reduced by 50% when heated in the microwave oven to 50 degree. However, if raw milk is heated to 50 degree using a conventional heat source, the lysozyme activity in it is almost the same as before heating, so the enzyme is inactivated not by heating but by the microwave that generates heat.
Question: Which of the following, if true, most weakens the argument?
Answer Options:
A: When raw milk is heated to 100 degree, lysozyme activity is completely inactivated.
B: The damage of enzyme in raw milk by heating could be compensated by adding other enzymes, but the damage of enzyme by microwave could not be compensated.
C: It takes longer to heat liquid milk to 50 degree with a conventional heat source than it does with a microwave.
D: A microwave oven heating a liquid causes the internal temperature to be higher than the surface temperature of the liquid.
Correct Answer: D
<stop>
Context: A certain city music festival set up seven categories of awards: pop, folk, rock, ethnic, electronic music, rap, and jazz. In the nomination of shortlisted names, it is known that: (1) At least 6 categories are shortlisted: (2) At least 2 categories are shortlisted among pop, folk and rock: (3) If both rock and ethnic categories are shortlisted, then electronic music and rap At least one category is not shortlisted.
Question: Based on the above information, which of the following can be derived?
Answer Options:
A: The pop category was not shortlisted.
B: The folk song category was not shortlisted.
C: The rock category was not shortlisted.
D: The Jazz category was not shortlisted.
Correct Answer: C
<stop>
'''

def call_api(prompt: str) -> str:
    prediction = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": context + prompt}],
                    temperature=0,
                    max_tokens=500,
                    top_p=1.0,
                    stop="<stop>",
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
    return prediction['choices'][0]['message']['content']

Opts = ['A', 'B', 'C', 'D']
Opts_map = {'A': 0, 'B':1, 'C':2, 'D':3}

def baseline(qa: dict) -> str:
    context =  qa['text']
    question = qa['question']
    options = qa['options']
    prompt = 'Context: ' + context + '\n' + 'Question: ' + question + '\n'  + 'Answer Options:\n'
    for i, opt in enumerate(options):
        prompt += Opts[i]+': ' + opt
    prompt += '\n Correct Answer: '
    # print(prompt)
    result = call_api(prompt)
    return result


def expalined(qa: dict) -> str:
    prompt = 'Context: ' + qa['Problem'] + '\n' + qa['options'] + '\nFollowing what steps can we solve this problem?\n'
    result = call_api(prompt)
    return result

def premised(qa: dict) -> str:
    label = 0 if qa['label']=="not entailed" else 1
    maj_premise = ' '.join(qa['major_premise'])
    min_premise = ' '.join(qa['minor_premise'])
    hypo = qa['conclusion']
    prompt = "Given the fact: " + maj_premise + ' ' + min_premise + " Does it follow that: " + hypo + " Yes or no?"
    # print(prompt)
    result = call_api(prompt)
    return result

def evaluate(predictions:list, method:str):
    if method == 'acc':
        score = 0
        for pred in predictions:
            if pred['correct'] == pred['prediction']:
                score += 1
        score /= len(predictions)
        return score

if __name__ == "__main__":
    with open('DATA/LOGIQA/sampled_test.txt', 'r') as f:
        file = f.readlines()

    predictions = []
    y_true = []
    y_pred = []
    cnt = 0
    for line in file:
        cnt +=1
        if cnt > 100:
            break
        qa = json.loads(line)
        y_true.append(qa['answer'])
        result = baseline(qa).strip()
        prediction = {'id':qa['id'],
                      'predicted_rational': result,
                      'prediction': result[-1]}
        if result[-1] in Opts_map:
            y_pred.append(Opts_map[result[-1]])
        else:
            y_pred.append(-1)
        predictions.append(prediction)
        time.sleep(5)

    with open('base_line.json', 'w') as f:
        json.dump(prediction, f)
        f.write('\n')
    # f_score = f1_score(y_true, y_pred, average='binary')
    # p_score = precision_score(y_true, y_pred, average='binary')
    # r_score = recall_score(y_true, y_pred, average='binary')
    acc = accuracy_score(y_true, y_pred)
    # print(y_true)
    # print(y_pred)

    # print("Total count:", cnt)
    # print("F score:", f_score)
    # print("Precision:", p_score)
    # print("Recall", r_score)
    print("Accuracy", acc)
