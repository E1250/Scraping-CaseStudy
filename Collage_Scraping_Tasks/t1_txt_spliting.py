"""
you have a flowers string, reads every line of the string, and saves it as a dictionary. 
Then, take user input (user's first name and last name) with message like this:
     (Enter your First [space] Last name only:)
Then, parse the user input to identify the first letter of the first name.
Use the first letter of user's first name to print the flower name with the same first letter

Example:
    Enter your First [space] Last name only: Mohamed Ahmed

then the user type for example: Mohamed Ahmed
the output should be: Monks Hood
"""

d = {}
flowers = """A: African Daisy
B: Bellflower
C: Coral Bells
D: Desert Rose
E: English Bluebell
F: Forget Me Not
G: Goldenrod
H: Heliotrope
I: Impatiens
J: Jamesia americana
K: Kangaroo Paw
L: Lily of the Valley
M: Monks Hood
N: Nemophila
O: Ox Eye Daisy
P: Peace Lily
Q: Quaker Ladies
R: Rain Lily
S: Snapdragon
T: Trumpet Vine
U: Urn Plant
V: Viola wittrockiana
W: Whirling Butterflies
X: Xanthoceras sorbifolium
Y: Yellow Archangel
Z: Zinnia elegans"""
# Solution 1
d.update({i.split(":")[0]: i.split(":")[1] for i in flowers.split('\n')})
# Another solution
lst = flowers.split('\n')
for i in lst:
    k,v = i.split(':')
    d.update({k:v})

name = input("Enter your First [space] Last name only:").split(" ")[0]

print(d[name[0].capitalize()])
