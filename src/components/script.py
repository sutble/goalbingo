
d = {0:'a',1:'b',2:'c',3:'d',4:'e'}

positions = [15,5,6,22,17,21,10,3,8,23,9,16,25,4,11,19,14,7,13,12,1,20,24,18,2]

for i in range(25):
    id = f'{(i%5)+1}{d[i//5]}'
    s = f'<div class="item" id="{id}">{{goalMap[{positions[i]}]}}</div>'
    print(s)

# for i in range(1,26):
#     s = f'<li> <input id="{26-i}" on:input={{updateText}}/> </li>'
#     print(s)