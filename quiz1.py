# Q1
import re
import numpy as np

string = "bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot"
result = re.findall("b[ao]t", string)
print(result)


# Q2
def l2_dist(a, b):
    result = ((a - b) * (a - b)).sum()
    result = result**0.5
    return result


# Generate 20x20 array
a = np.random.rand(20, 20)
b = np.random.rand(20, 20)

print(l2_dist(a.T, b.T))
print(l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1))))
print(l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20))))
print(l2_dist(a, b))

# Q3
a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1, 4, 4)

# print(a4.ndim() == 1)
print(a1.shape == a2.shape)
print(a3.shape == a4.shape)
print(a5.shape == a1.shape)
# Strange in a3 and a4 shape, which is arange function

# Q4
old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0
print(old)

# Q5
question = np.arange(0, 36, 1)
question = question.reshape(6, 6)
question

question[2:4, 2:4]

# Q6
s = "ACBCAC"
print(re.findall("^AC", s))
print(re.findall("^[AC]", s))
print(re.findall("[^A]C", s))
print(re.findall("AC", s))

# Q7
s = "ACAABAACAAAB"
result = re.findall("A{1,2}", s)
L = len(result)
L

# Q8
with open("./data/q8.txt", "r") as file:
    q8 = file.read()

print(re.findall("\d{3}[-]\d{3}[-]\d{4}", q8))
print(re.findall("[(]\d{3}[)]\d{3}[-]\d{4}", q8))
print(re.findall("[(]\d{3}[)]\s\d{3}[-]\d{4}", q8))
print(re.findall("\d{3}\s\d{3}[-]\d{4}", q8))

# Q9
q9 = "I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything"

print(re.findall("(?<=https:\/\/)([.]*)", q9))
print(re.findall("(?<=[https]:\/\/)([A-Za-z0-9.]*)", q9))
print(re.findall("(?<=https:\/\/)([A-Za-z0-9]*)", q9))
print(re.findall("(?<=https:\/\/)([A-Za-z0-9.]*)", q9))

# Q10
text = r"""Everyone has the following fundamental freedoms:
    (a) freedom of conscience and religion;
    (b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
    (c) freedom of peaceful assembly; and
    (d) freedom of association."""

pattern = "\(.\)"
print(len(re.findall(pattern, text)))
pattern = "[a-d]"
print(len(re.findall(pattern, text)))
pattern = "freedom"
print(len(re.findall(pattern, text)))
pattern = "(.)"
print(len(re.findall(pattern, text)))
