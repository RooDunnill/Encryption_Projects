# a b c d e f g h i j k l m n o p q r s t u v w x y z
# 1 2 3 4 5 6 7 8 9 1011121314151617181920212223242526
import numpy as np
import re
from collections import Counter
import time
key_test = "Winteriscoming"
message_test = """In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole,
filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy
hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and
that means comfort.
It had a perfectly round door like a porthole, painted green, with a
shiny yellow brass knob in the exact middle. The door opened on to a tubeshaped hall like a tunnel: a very comfortable tunnel without smoke, with
panelled walls, and floors tiled and carpeted, provided with polished
chairs, and lots and lots of pegs for hats and coats—the hobbit was fond of
visitors. The tunnel wound on and on, going fairly but not quite straight
into the side of the hill—The Hill, as all the people for many miles round
called it—and many little round doors opened out of it, first on one side
and then on another. No going upstairs for the hobbit: bedrooms,
bathrooms, cellars, pantries (lots of these), wardrobes (he had whole
rooms devoted to clothes), kitchens, dining-rooms, all were on the same
floor, and indeed on the same passage. The best rooms were all on the lefthand side (going in), for these were the only ones to have windows, deepset round windows looking over his garden, and meadows beyond, sloping
down to the river. This hobbit was a very well-to-do hobbit, and his name was Baggins.
The Bagginses had lived in the neighbourhood of The Hill for time out of
mind, and people considered them very respectable, not only because most
of them were rich, but also because they never had any adventures or did
anything unexpected: you could tell what a Baggins would say on any
question without the bother of asking him. This is a story of how a
Baggins had an adventure, and found himself doing and saying things
altogether unexpected. He may have lost the neighbours’ respect, but he
gained—well, you will see whether he gained anything in the end.
The mother of our particular hobbit—what is a hobbit? I suppose
hobbits need some description nowadays, since they have become rare and
shy of the Big People, as they call us. They are (or were) a little people,
about half our height, and smaller than the bearded Dwarves. Hobbits have
no beards. There is little or no magic about them, except the ordinary
everyday sort which helps them to disappear quietly and quickly when
large stupid folk like you and me come blundering along, making a noise
like elephants which they can hear a mile off. They are inclined to be fat in
the stomach; they dress in bright colours (chiefly green and yellow); wear
no shoes, because their feet grow natural leathery soles and thick warm
brown hair like the stuff on their heads (which is curly); have long clever
brown fingers, good-natured faces, and laugh deep fruity laughs
(especially after dinner, which they have twice a day when they can get it). Now you know enough to go on with. As I was saying, the mother of this
hobbit—of Bilbo Baggins, that is—was the famous Belladonna Took, one
of the three remarkable daughters of the Old Took, head of the hobbits who
lived across The Water, the small river that ran at the foot of The Hill. It
was often said (in other families) that long ago one of the Took ancestors
must have taken a fairy wife. That was, of course, absurd, but certainly
there was still something not entirely hobbitlike about them, and once in a
while members of the Took-clan would go and have adventures. They
discreetly disappeared, and the family hushed it up; but the fact remained
that the Tooks were not as respectable as the Bagginses, though they were
undoubtedly richer. Not that Belladonna Took ever had any adventures after she became
Mrs. Bungo Baggins. Bungo, that was Bilbo’s father, built the most
luxurious hobbit-hole for her (and partly with her money) that was to be
found either under The Hill or over The Hill or across The Water, and
there they remained to the end of their days. Still it is probable that Bilbo,
her only son, although he looked and behaved exactly like a second edition
of his solid and comfortable father, got something a bit queer in his make-
up from the Took side, something that only waited for a chance to come
out. The chance never arrived, until Bilbo Baggins was grown up, being
about fifty years old or so, and living in the beautiful hobbit-hole built by
his father, which I have just described for you, until he had in fact
apparently settled down immovably. parently settled down immovably.
By some curious chance one morning long ago in the quiet of the
world, when there was less noise and more green, and the hobbits were
still numerous and prosperous, and Bilbo Baggins was standing at his door
after breakfast smoking an enormous long wooden pipe that reached
nearly down to his woolly toes (neatly brushed)—Gandalf came by.
Gandalf! If you had heard only a quarter of what I have heard about him,
and I have only heard very little of all there is to hear, you would be
prepared for any sort of remarkable tale. Tales and adventures sprouted up
all over the place wherever he went, in the most extraordinary fashion. He
had not been down that way under The Hill for ages and ages, not since his
friend the Old Took died, in fact, and the hobbits had almost forgotten
what he looked like. He had been away over The Hill and across The Water
on businesses of his own since they were all small hobbit-boys and hobbitgirls.
All that the unsuspecting Bilbo saw that morning was an old man with
a staff. He had a tall pointed blue hat, a long grey cloak, a silver scarf over
which his long white beard hung down below his waist, and immense
black boots.
“Good Morning!” said Bilbo, and he meant it. The sun was shining, and
the grass was very green. But Gandalf looked at him from under long
bushy eyebrows that stuck out further than the brim of his shady hat.
“What do you mean?” he said. “Do you wish me a good morning, or
mean that it is a good morning whether I want it or not; or that you feel
good this morning; or that it is a morning to be good on?”
“All of them at once,” said Bilbo. “And a very fine morning for a pipe
of tobacco out of doors, into the bargain. If you have a pipe about you, sit
down and have a fill of mine! There’s no hurry, we have all the day before
us!” Then Bilbo sat down on a seat by his door, crossed his legs, and blew
out a beautiful grey ring of smoke that sailed up into the air without
breaking and floated away over The Hill. “Very pretty!” said Gandalf. “But I have no time to blow smoke-rings
this morning. I am looking for someone to share in an adventure that I am
arranging, and it’s very difficult to find anyone.”
“I should think so—in these parts! We are plain quiet folk and have no
use for adventures. Nasty disturbing uncomfortable things! Make you late
for dinner! I can’t think what anybody sees in them,” said our Mr. Baggins,
and stuck one thumb behind his braces, and blew out another even bigger
smokering. Then he took out his morning letters, and began to read,
pretending to take no more notice of the old man. He had decided that he
was not quite his sort, and wanted him to go away. But the old man did not
move. He stood leaning on his stick and gazing at the hobbit without
saying anything, till Bilbo got quite uncomfortable and even a little cross.
“Good morning!” he said at last. “We don’t want any adventures here,
thank you! You might try over The Hill or across The Water.” By this he
meant that the conversation was at an end.
“What a lot of things you do use Good morning for!” said Gandalf.
“Now you mean that you want to get rid of me, and that it won’t be good
till I move off.”
“Not at all, not at all, my dear sir! Let me see, I don’t think I know your
name?”
“Yes, yes, my dear sir—and I do know your name, Mr. Bilbo Baggins.
And you do know my name, though you don’t remember that I belong to
it. I am Gandalf, and Gandalf means me! To think that I should have lived
to be good-morninged by Belladonna Took’s son, as if I was selling
buttons at the door!”
“Gandalf, Gandalf! Good gracious me! Not the wandering wizard that
gave Old Took a pair of magic diamond studs that fastened themselves and
never came undone till ordered? Not the fellow who used to tell such
wonderful tales at parties, about dragons and goblins and giants and the
rescue of princesses and the unexpected luck of widows’ sons? Not the
man that used to make such particularly excellent fireworks! I remember
those! Old Took used to have them on Midsummer’s Eve. Splendid! They
used to go up like great lilies and snapdragons and laburnums of fire and
hang in the twilight all evening!” You will notice already that Mr. Baggins
was not quite so prosy as he liked to believe, also that he was very fond of
flowers. “Dear me!” he went on. “Not the Gandalf who was responsible for so many quiet lads and lasses going off into the Blue for mad adventures?
Anything from climbing trees to visiting elves—or sailing in ships, sailing
to other shores! Bless me, life used to be quite inter—I mean, you used to
upset things badly in these parts once upon a time. I beg your pardon, but I
had no idea you were still in business.”
“Where else should I be?” said the wizard. “All the same I am pleased
to find you remember something about me. You seem to remember my
fireworks kindly, at any rate, and that is not without hope. Indeed for your
old grandfather Took’s sake, and for the sake of poor Belladonna, I will
give you what you asked for.”
“I beg your pardon, I haven’t asked for anything!”
“Yes, you have! Twice now. My pardon. I give it you. In fact I will go
so far as to send you on this adventure. Very amusing for me, very good
for you—and profitable too, very likely, if you ever get over it.”
“Sorry! I don’t want any adventures, thank you. Not today. Good
morning! But please come to tea—any time you like! Why not tomorrow?
Come tomorrow! Good bye!” With that the hobbit turned and scuttled
inside his round green door, and shut it as quickly as he dared, not to seem
rude. Wizards after all are wizards.
“What on earth did I ask him to tea for!” he said to himself, as he went
to the pantry. He had only just had breakfast, but he thought a cake or two
and a drink of something would do him good after his fright.
Gandalf in the meantime was still standing outside the door, and
laughing long but quietly. After a while he stepped up, and with the spike
on his staff scratched a queer sign on the hobbit’s beautiful green frontdoor. Then he strode away, just about the time when Bilbo was finishing
his second cake and beginning to think that he had escaped adventures
very well.
The next day he had almost forgotten about Gandalf. He did not
remember things very well, unless he put them down on his Engagement
Tablet: like this: Gandalf Tea Wednesday. Yesterday he had been too
flustered to do anything of the kind.
Just before tea-time there came a tremendous ring on the front-door
bell, and then he remembered! He rushed and put on the kettle, and put out
another cup and saucer, and an extra cake or two, and ran to the door. “I am so sorry to keep you waiting!” he was going to say, when he saw
that it was not Gandalf at all. It was a dwarf with a blue beard tucked into
a golden belt, and very bright eyes under his dark-green hood. As soon as
the door was opened, he pushed inside, just as if he had been expected.
He hung his hooded cloak on the nearest peg, and “Dwalin at your
service!” he said with a low bow.
“Bilbo Baggins at yours!” said the hobbit, too surprised to ask any
questions for the moment. When the silence that followed had become
uncomfortable, he added: “I am just about to take tea; pray come and have
some with me.” A little stiff perhaps, but he meant it kindly. And what
would you do, if an uninvited dwarf came and hung his things up in your
hall without a word of explanation?
They had not been at table long, in fact they had hardly reached the
third cake, when there came another even louder ring at the bell.
“Excuse me!” said the hobbit, and off he went to the door.
“So you have got here at last!” That was what he was going to say to
Gandalf this time. But it was not Gandalf. Instead there was a very oldlooking dwarf on the step with a white beard and a scarlet hood; and he too
hopped inside as soon as the door was open, just as if he had been invited.
“I see they have begun to arrive already,” he said when he caught sight
of Dwalin’s green hood hanging up. He hung his red one next to it, and
“Balin at your service!” he said with his hand on his breast.
“Thank you!” said Bilbo with a gasp. It was not the correct thing to say,
but they have begun to arrive had flustered him badly. He liked visitors,
but he liked to know them before they arrived, and he preferred to ask
them himself. He had a horrible thought that the cakes might run short,
and then he—as the host: he knew his duty and stuck to it however painful
—he might have to go without.
“Come along in, and have some tea!” he managed to say after taking a
deep breath.
“A little beer would suit me better, if it is all the same to you, my good
sir,” said Balin with the white beard. “But I don’t mind some cake—seedcake, if you have any.”
“Lots!” Bilbo found himself answering, to his own surprise; and he
found himself scuttling off, too, to the cellar to fill a pint beer-mug, and then to a pantry to fetch two beautiful round seed-cakes which he had
baked that afternoon for his after-supper morsel.
When he got back Balin and Dwalin were talking at the table like old
friends (as a matter of fact they were brothers). Bilbo plumped down the
beer and the cake in front of them, when loud came a ring at the bell again,
and then another ring.
“Gandalf for certain this time,” he thought as he puffed along the
passage. But it was not. It was two more dwarves, both with blue hoods,
silver belts, and yellow beards; and each of them carried a bag of tools and
a spade. In they hopped, as soon as the door began to open—Bilbo was
hardly surprised at all.
“What can I do for you, my dwarves?” he said.
“Kili at your service!” said the one. “And Fili!” added the other; and
they both swept off their blue hoods and bowed.
“At yours and your family’s!” replied Bilbo, remembering his manners
this time.
“Dwalin and Balin here already, I see,” said Kili. “Let us join the
throng!”
“Throng!” thought Mr. Baggins. “I don’t like the sound of that. I really
must sit down for a minute and collect my wits, and have a drink.” He had
only just had a sip—in the corner, while the four dwarves sat round the
table, and talked about mines and gold and troubles with the goblins, and
the depredations of dragons, and lots of other things which he did not
understand, and did not want to, for they sounded much too adventurous—
when, ding-dong-a-ling-dang, his bell rang again, as if some naughty little
hobbit-boy was trying to pull the handle off.
“Someone at the door!” he said, blinking.
“Some four, I should say by the sound,” said Fili. “Besides, we saw
them coming along behind us in the distance.”



 """
#clean_m_test = re.sub('\W+', "", message_test)
#clean_m_test = clean_m_test.lower()
def encrypt(message, key):  #encryption function
    m_list = []   #creates a list to put the message in, one letter at a time
    k_list = []   #creates a lits to put each letter of the key in
    c_list = []   #you get the gist
    cypher_text = ''    #empty string for the outputted cypher
    m_len = len(message)     #used to make the key the same length 
    k_len = len(key)         #used to measure the inital key size
    mult = int(m_len/k_len)  #works out how many times to iterate the key through
    mult_r = m_len % k_len   #self explanitory
    for letter in message:   #converts to ASCII number values
        m_list.append(ord(letter) - 97)  #converts message into a list with each letter seperate
    for i in range(mult):    #probs could have used a while loop or array here
        for letter in key:   #converts the key to ASCII
            k_list.append(ord(letter) - 97) #errrrr, i dont think this for i in range loop does anything?
    for i in range(mult_r):  #adds a portion of the key to make it the same length as the message
        k_list.append(k_list[i])  #yaknow the gist
    for i in range(m_len):   #applies the key ASCII value to the message one to make the cypher text
        c_list.append(k_list[i] + m_list[i])
    for number in c_list:    #this is to make the ASCII number stay in the alphabet range
        cypher_text += chr(number % 26 + 97) #you could not do this to make it ig have a larger key space
    return cypher_text                       #but then you run the risk of an adversary knowing roughly 
                                             #where in the ASCII table you are
def decrypt(cypher, key):#same shit just in reverse basically
    c_len = len(cypher)
    k_len = len(key)
    mult = int(c_len/k_len) #didnt wanna use the values from the other function so just redefined
    mult_r = c_len % k_len
    c_list = []
    k_list = []
    m_list = []
    message_text = ''
    for letter in cypher:
        c_list.append(ord(letter) - 97)#converts again to numbers
    for i in range(mult):
        for letter in key:
            k_list.append(ord(letter) - 97)
    for i in range(mult_r):
        k_list.append(k_list[i])
    for i in range(c_len):
        m_list.append(c_list[i] - k_list[i])
    for number in m_list:
        if number < 0:  #main diff is that if the value is below 0 it shifts it back up
            number += 26   #similar to the modulo function in the encryption one
        else:
            number = number
        let = chr(number + 97)
        message_text += let  #adds to the message text, could be more compact
    return message_text
#clean_cy_test = encrypt(clean_m_test, key_test)#used to make the text all letters

def k_length_find(cypher): #this is a work in progress, good luck following it XD
        c_list = []
        c_count = []
        cy_len = len(cypher)
        letter_val =  ["a"  , "b"  , "c"  , "d"  , "e"  , "f"  , "g"  , "h"  , "i"  , "j"  , "k"  , "l"  , "m"  , "n"  , "o"  , "p"  , "q"  , "r"  , "s"  , "t"  , "u"  , "v"  , "w"  , "x"  , "y"  , "z"  ] 
        letter_freq = np.array([0.084966, 0.020720, 0.045388, 0.033844, 0.111607, 0.018121, 0.022705, 0.030034, 0.075448, 0.001965, 0.011016, 0.05493, 0.030129, 0.066544, 0.071635, 0.031671, 0.001962, 0.075809, 0.057351, 0.069509, 0.036308, 0.010074, 0.012899, 0.002902, 0.017779, 0.002722])
        letter_freq2 = np.array([0.082,   0.015,    0.028,    0.043,    0.127,    0.022,    0.020,    0.061,    0.070,    0.0015,   0.0077,   0.040,   0.024,    0.067,    0.075,    0.019,    0.00095,  0.060,    0.063,    0.091,    0.028,    0.0098,   0.024,    0.0015,   0.02,     0.00074])
        base_sum_squared = np.sum(letter_freq2 ** 2)
        sum = np.sum(letter_freq)
        stream = []
        for letter in cypher:
            c_list.append(ord(letter) - 97)
        c_len = len(cypher)
        key_length_acc = []
        for k in range(7):
            stream_size = int(c_len/(k+1))
            c_count = []
            square = 0
            for i in range(26):
                c_count.append(0)
            for i in range(stream_size):
                stream.append(c_list[(i) * (k+1)])
            for i in range(stream_size):
                c_count[stream[i]] += 1
            squared_sum = 0
            sum_count = 0
            #print(c_count)
            for i in range(25):
                sum_count += c_count[i]
            for i in range(25):
                squared_sum += (c_count[i]/sum_count) ** 2
            #print(squared_sum)
            key_length_acc.append(abs(squared_sum - base_sum_squared))
        #print(base_sum_squared)
        #print(key_length_acc)





#def vig_break(cypher):
  #  return


#k_length_find(clean_cy_test)

    
print("""Welcome to my encryption/decryption software. 
Currently, the encryption uses Vignere encryption, however,
this will be updated.
""")
time.sleep(1)
print("""Code breaking will (maybe) come soon!
I want to work on adding a way to stop adversaries from using
the letter freq hack on this
I want to code an assymetric protocol next
Hope you enjoy!  
      """)
time.sleep(1)
#k_length_find(cypher_test)
protocol = int(input("Press 1 for encryption, 2 for decryption and 3 for cracker:"))
if protocol == 1:
    message_in = str(input("Enter the message to be encrypted: ")).strip().lower()
    key_in = str(input("Enter the key to encrypt the message with: ")).strip().lower()
    print(encrypt(message_in,key_in))
elif protocol == 2:
    cypher_in = str(input("Enter the cypher: ")).strip().lower()
    key_in = str(input("Enter the key to encrypt the message with: ")).strip().lower()
    print(decrypt(cypher_in, key_in))
elif protocol == 3:
    print("Not currently Available :(")
    exit()
else:
    print("Not a valid input:")
    exit()



        
