import re
from functools import reduce


def hash(self):
    return reduce(lambda prev, cur: (prev + cur) * 17 % 256, (ord(x) for x in self), 0)


with open('../inputs/day15.txt') as file:
    line = file.read().split(',')
    print(sum(hash(text) for text in line))
    boxes = [[] for _ in range(256)]
    for i, text in enumerate(line):
        label, op, *num = re.findall(r'(\w+|\d+|=|-)', text)
        box = boxes[hash(label)]
        label_indexes = {l: i for i, (l, _) in enumerate(box)}
        if op == '=':
            if label not in label_indexes:
                box.append((label, int(num[0])))
            else:
                box[label_indexes[label]] = (label, int(num[0]))
        elif label in label_indexes:
            boxes[hash(label)] = [(lbl, value) for lbl, value in box if lbl != label]
    print(sum(
        box_num * i * val[1]
        for box_num, box in enumerate(boxes, start=1)
        for i, val in enumerate(box, start=1)
    ))
