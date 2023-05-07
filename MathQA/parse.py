import json
 
with open('mathqa_with_explanation_has_answer.json', 'r') as f:
  base = json.load(f)

with open('mathqa_modified_explanation_has_answer.json', 'r') as f:
  modified = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
#print(json.dumps(base[0], indent=4))
#print(json.dumps(modified[0], indent=4))

print(len(base), len(modified))
#print(json.dumps(base[2495], indent=4))
#print(json.dumps(modified[2294], indent=4)) they are same up to 2294

base_problems = set([x["Problem"] for x in base])
modified_problems = set([x["Problem"] for x in modified])
common_problems = base_problems.intersection(modified_problems)

base = [problem for problem in base if problem["Problem"] in common_problems]
modified = [problem for problem in modified if problem["Problem"] in common_problems]

base = sorted(base, key=lambda x: x["Problem"])
modified = sorted(modified, key=lambda x: x["Problem"])

N = len(base)

corr_incorr = []
incorr_corr = []


for i in range(N):
    base_correct = base[i]["correct"] == base[i]["prediction"]
    modified_correct = modified[i]["correct"] == modified[i]["prediction"]
    if base_correct and not modified_correct:
       corr_incorr.append((base[i], modified[i]))
    if not base_correct and modified_correct:
       incorr_corr.append((base[i], modified[i]))

print(len(base), len(corr_incorr), len(incorr_corr))

print

with open("corr_incorr.txt", 'w', encoding='utf8') as fp:
    for p in corr_incorr[:10]:
        # write each item on a new line
        fp.write(str(json.dumps(p[0], indent=4, ensure_ascii=False)))
        fp.write("\n")
        fp.write(str(json.dumps(p[1], indent=4, ensure_ascii=False)))
        fp.write("\n")

with open("incorr_corr.txt", 'w', encoding='utf8') as fp:
    for p in incorr_corr[:10]:
        # write each item on a new line
        fp.write(str(json.dumps(p[0], indent=4, ensure_ascii=False)))
        fp.write("\n")
        fp.write(str(json.dumps(p[1], indent=4, ensure_ascii=False)))
        fp.write("\n")


"""for i in range(N):
  if not base[i]["Problem"] == modified[i]["Problem"]:
    print(f"no match at idx={i}")
    break

i = 1
print(base[i]["Problem"] == modified[i]["Problem"])"""