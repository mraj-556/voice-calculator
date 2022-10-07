import speech_recognition as sr
from word2number import w2n
# import re

def preprocess(number):
    l = []
    number = number + '+'

    operators = ['+','plus','Plus','PLUS','-','minus','Minus','MINUS','*','Multiply','multiply','MULTIPLY''multiplied by','multiply with','multiplied with','multiplied','/','division','Division','DIVISION','divided by','devide']
    a = ''
    for idx,i in enumerate(number):
        # print(idx,len(number),i ,'   preprocess')
        if i not in operators and a not in operators:
            # print(i,'add')
            a+=i
        elif i in operators:
            l.append(a)
            # print(a,i,' appended')
            a=''
            l.append(i)
    return l[:-1]


def preprocess_spaces(number):
    for idx,i in enumerate(number):
        number[idx]=i.strip()
    return number

def calculate(numbers):         #  100 + 200 + 205 + 300 + 1 million
    numbers = preprocess(numbers)
    numbers = preprocess_spaces(numbers)
    if isinstance(numbers[0],str):
        result , to_do = int(w2n.word_to_num(numbers[0])) , 0
    elif numbers[0].isnumeric():
        result , to_do = numbers[0] , 0
    # print(numbers)
    for i  in range(2,len(numbers),2):
        try:
        # if True:
            l = ['+','plus','Plus','PLUS','-','minus','Minus','MINUS','*','Multiply','multiply','MULTIPLY''multiplied by','multiply with','multiplied with','multiplied','/','division','Division','DIVISION','divided by','devide']
            if numbers[i] not in l:
                # print('check : ',numbers[i])
                try:
                    numbers[i].isnumeric()
                    to_do = int(numbers[i])
                except isinstance(numbers[i],str):
                    to_do = int(w2n.word_to_num(numbers[i]))
                except numbers[i].isalnum():
                    print('Error in detection or wrong input ')

            if numbers[i-1] in l:
                if numbers[i-1] in ['+','plus','Plus','PLUS']:
                    # print('Result + : ',result,to_do)
                    result+=to_do
                    # print('Result + : ',result)
                elif numbers[i-1] in ['-','minus','Minus','MINUS']:
                    # print('Result - : ',result,to_do)
                    result-=to_do
                    # print('Result - : ',result)
                elif numbers[i-1] in ['*','Multiply','multiply','MULTIPLY','multiplied by','multiply with','multiplied with','multiplied']:
                    # print('Result * : ',result,to_do)
                    result*=to_do
                    # print('Result * : ',result)
                elif numbers[i-1] in ['/','division','Division','DIVISION','divided by','devide']:
                    # print('Result / : ',result,to_do)
                    result/=to_do
                    # print('Result / : ',result)
        except:
        # else:
            print('Sorry error in calculation')
            
    print('Result : ',result)

print('Speak your numbers')
voice = sr.Recognizer()
with sr.Microphone() as source:
    voice.pause_threshold = 0.6
    audio = voice.listen(source)
    try:
        said = voice.recognize_google(audio,language='en-us')
        print(said)
        calculate(said)
    except:
        print('Error in listening')

# calculate(input('enter data : '))