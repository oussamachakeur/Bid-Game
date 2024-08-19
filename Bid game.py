'''students_scores= {"oussama":99 , "james":81, "baroudi":79, "riad":60}
students_grades={}
#convert the score to grade 
for students , scores in students_scores.items():
    if 91<= scores<=100:
        students_grades[students]="ouststanding"
    elif (81 <= scores<=90):
        students_grades[students]="exellent"   
    elif ( 71<= scores<=80):
        students_grades[students]="acceptable"
    elif scores <=70:
        students_grades[students]="fail"
    else:
        students_grades[students]="wrong input" 
print(students_grades)'''

'''country_log=[{"country":"germany","num_of_visit": 5 ,"cities":["dortmund","munich","shtutgart"] }]

def add_new_country(country,visit,cities ):
     country_log.append({"country":country,"num_of_visit": visit , "cities":cities})
     print(country_log)


add_new_country(input("which country you visited: "),int(input('how many time you visited : ')) , cities = [input("name of cities: ")])'''

from replit import clear




choices={}

def choose():
    Name= input("please enter ur name ")
    bid = int(input("please enter ur bid : $ "))
    choices[Name]=bid


def big_bit():
    bid_list=[]
    for name , bid in choices.items():
        bid_list.append(bid)
    top = max(bid_list)
    payer = None
    for name ,bid in choices.items():
        if choices[name]==top:
            payer = name
    return payer , top
    
print("hello and welcome the bid game ")
print("today we will bid on this picture and se who will get it ")
play = True
while play is True : 
    choose()
    payer,top = big_bit()
    clear()
    answer = input('do u wanna add an new player (yes/.no): ').strip().low()
    if answer== "no":
        print("the one who will pay is  "+ payer + " he will pay: $ "+str(top))
        play= False
    else:
        continue

    

