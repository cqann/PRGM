import collections
import time


inpt = 59702216318401831752516109671812909117759516365269440231257788008453756734827826476239905226493589006960132456488870290862893703535753691507244120156137802864317330938106688973624124594371608170692569855778498105517439068022388323566624069202753437742801981883473729701426171077277920013824894757938493999640593305172570727136129712787668811072014245905885251704882055908305407719142264325661477825898619802777868961439647723408833957843810111456367464611239017733042717293598871566304020426484700071315257217011872240492395451028872856605576492864646118292500813545747868096046577484535223887886476125746077660705155595199557168004672030769602168262
#inpt = "80871224585914546619083218645595"
nums = [int(x) for x in str(inpt)]
offset = 0#int("".join([str(x) for x in nums[0:7]]))
pattern = [0,1,0,-1]

t0 = time.time()
for i in range(100):
    mod_pat = list(pattern)
    begin1 = 0
    stop1 = 1
    begin2 = 2
    stop2 = 3
    zeroes = collections.deque([0])
    ones = collections.deque([1])
    neg_ones = collections.deque([-1])
    for n in range(len(nums)):
        '''
        result = 0
        for j in range(len(nums)):
            pat_index = (j+1)%len(mod_pat)
            
            if (pat_index >= stop1 and pat_index <= begin2) or pat_index >= stop2:
                result += int(nums[j]) * mod_pat[pat_index]
        '''
        nums[n] = str(sum([ int(nums[x]) * mod_pat[(x+1)%len(mod_pat)] for x in range(len(nums)) ]))[-1]
        zeroes.append(0)
        ones.append(1)
        neg_ones.append(-1)
        mod_pat = zeroes + ones + zeroes + neg_ones
        stop1 += 1 
        begin2 += 2
        stop2 += 3


print(time.time()-t0)
print(nums[offset:offset+8])

