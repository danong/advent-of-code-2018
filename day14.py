count = 74501

idx1, idx2 = 0, 1
scores = [3, 7]

while len(scores) < (count + 10):
    score_sum = scores[idx1] + scores[idx2]
    if score_sum < 10:
        scores.append(score_sum)
    else:
        scores.append(1)
        scores.append(score_sum % 10)
    idx1 = (idx1 + 1 + scores[idx1]) % len(scores)
    idx2 = (idx2 + 1 + scores[idx2]) % len(scores)

print(''.join(str(x) for x in scores[count:count + 10]))

target = '074501'
target = [int(x) for x in target]
print(target)
idx1, idx2 = 0, 1
scores = [3, 7]

count = 0
while True:
    if count % 100 == 0:
        print(count)
    score_sum = scores[idx1] + scores[idx2]
    if score_sum < 10:
        scores.append(score_sum)
    else:
        scores.append(1)
        scores.append(score_sum % 10)
    if scores[-len(target):] == target:
        print(len(scores) - len(target))
        break

    elif scores[-len(target)-1:-1] == target:
        print(len(scores) - len(target) - 1)
        break
    count += 1
    idx1 = (idx1 + 1 + scores[idx1]) % len(scores)
    idx2 = (idx2 + 1 + scores[idx2]) % len(scores)

# print(count)