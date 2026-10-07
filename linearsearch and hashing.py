# Comment
import time
names3 = [
    "Aiden", "Amelia", "Andrew", "Anna", "Anthony", "Aria", "Arthur", "Aubrey",
    "Benjamin", "Bella", "Brandon", "Brooklyn", "Caleb", "Camila", "Cameron", "Caroline",
    "Charles", "Charlotte", "Chase", "Chloe", "Christian", "Claire", "Christopher", "Clara",
    "Daniel", "Daisy", "David", "Delilah", "Dylan", "Eleanor", "Elijah", "Elizabeth",
    "Ella", "Ellie", "Emily", "Emma", "Ethan", "Eva", "Evelyn", "Ezra",
    "Faith", "Felix", "Fiona", "Finn", "Florence", "Gabriel", "Gabriella", "Gavin",
    "Gemma", "George", "Georgia", "Grace", "Grayson", "Hailey", "Hannah", "Harper",
    "Harrison", "Hazel", "Henry", "Hudson", "Hunter", "Isabella", "Isaac", "Isla",
    "Jack", "Jackson", "Jacob", "Jade", "James", "Jasmine", "Jason", "Jasper",
    "Jayden", "Jaxon", "Jennifer", "Jeremiah", "Jessica", "John", "Jonathan", "Joseph",
    "Josephine", "Joshua", "Josie", "Julia", "Julian", "Juliette", "Kai", "Katherine",
    "Kayla", "Kaylee", "Kennedy", "Kevin", "Kinsley", "Knox", "Landon", "Laura",
    "Lauren", "Layla", "Leah", "Leo", "Leon", "Leonardo", "Levi", "Liam",
    "Lillian", "Lily", "Lincoln", "Logan", "Lola", "Lucas", "Lucy", "Luke",
    "Luna", "Madeline", "Madison", "Mackenzie", "Maeve", "Maria", "Mariah", "Mark",
    "Mason", "Matthew", "Maya", "Megan", "Melanie", "Michael", "Michelle", "Mila",
    "Miles", "Molly", "Morgan", "Naomi", "Natalie", "Nathan", "Nathaniel", "Nora",
    "Noah", "Nolan", "Nora", "Oliver", "Olivia", "Owen", "Paisley", "Parker",
    "Penelope", "Peter", "Peyton", "Piper", "Preston", "Quinn", "Rachel", "Raelynn",
    "Reagan", "Rebecca", "Reese", "Remy", "Riley", "Robert", "Roman", "Ruby",
    "Ryan", "Sadie", "Samantha", "Samuel", "Sarah", "Savannah", "Scarlett", "Sebastian",
    "Serenity", "Sienna", "Simon", "Skylar", "Sofia", "Sophia", "Spencer", "Stella",
    "Stephen", "Steven", "Summer", "Sydney", "Taylor", "Theodore", "Thomas", "Tiffany",
    "Tristan", "Tyler", "Valentina", "Valerie", "Vanessa", "Violet", "Vivian", "Wesley",
    "William", "Willow", "Wyatt", "Xavier", "Yasmin", "Zachary", "Zoe", "Abigail",
    "Adalyn", "Adam", "Adeline", "Adrian", "Adriana", "Alana", "Alan", "Alayna",
    "Albert", "Alexa", "Alexander", "Alexandra", "Alexis", "Alice", "Alina", "Allison",
    "Allyson", "Amanda", "Amber", "Amira", "Amy", "Ana", "Andrea", "Angel",
    "Angela", "Angelina", "Annie", "April", "Ariana", "Arianna", "Ariel", "Ashley",
    "Asher", "Aspen", "Athena", "Audrey", "Aurora", "Austin", "Autumn", "Avery",
    "Bailey", "Barbara", "Beatrice", "Beau", "Beckett", "Becky", "Bianca", "Blake",
    "Blair", "Blaire", "Brady", "Braelyn", "Brayden", "Braylee", "Brent", "Brianna",
    "Brian", "Bridget", "Brielle", "Brody", "Brooke", "Bryan", "Bryce", "Brynn",
    "Caden", "Caitlin", "Calvin", "Carly", "Carson", "Carter", "Casey", "Cassidy",
    "Catherine", "Cecilia", "Celeste", "Cesar", "Chad", "Charlie", "Chelsea", "Cheryl",
    "Cindy", "Colby", "Cole", "Colin", "Connor", "Cooper", "Courtney", "Crystal",
    "Damian", "Damon", "Danielle", "Daphne", "Darren", "Dawn", "Dean", "Declan",
    "Dennis", "Derek", "Desiree", "Destiny", "Diego", "Dominic", "Dorian", "Dorothy",
    "Eddie", "Edgar", "Edith", "Edward", "Edwin", "Elaina", "Elaine", "Elena",
    "Eliana", "Elise", "Eliza", "Elizabeth", "Emerson", "Emilia", "Emmanuel", "Eric",
    "Erica", "Erik", "Erin", "Esme", "Esther", "Eugene", "Evan", "Everett",
    "Faith", "Felicia", "Fernando", "Finley", "Frances", "Francis", "Frank", "Gabriela",
    "Gage", "Garrett", "Giselle", "Gloria", "Grant", "Griffin", "Gwendolyn", "Haley",
    "Halle", "Harmony", "Harvey", "Hayden", "Heidi", "Helen", "Holden", "Hope",
    "Ian", "Imogen", "Irene", "Iris", "Isaiah", "Isabel", "Ivan", "Ivy",
    "Jackie", "Jacob", "Jalen", "Jameson", "Jamie", "Jared", "Javier", "Jayla",
    "Jenna", "Jeremy", "Jesse", "Jill", "Joanna", "Jocelyn", "Joel", "Jonah",
    "Jordan", "Jorge", "Joy", "Juan", "Judith", "Judy", "Justin", "Kaitlyn",
    "Kara", "Karen", "Karina", "Karla", "Kate", "Katelyn", "Kathleen", "Katie",
    "Kayden", "Keira", "Keith", "Kelly", "Kelsey", "Kendall", "Kerry", "Kimberly",
    "Kingston", "Kira", "Kristen", "Kristin", "Kyle", "Kylee", "Lacey", "Lana",
    "Laura", "Lauren", "Lawrence", "Leilani", "Lena", "Leslie", "Liam", "Lindsey",
    "Lisa", "Livia", "Lorenzo", "Louise", "Lucia", "Luis", "Lydia", "Mabel",
    "Mack", "Madelyn", "Magnolia", "Marcus", "Margaret", "Margot", "Mariana", "Marissa",
    "Martha", "Martin", "Mary", "Mason", "Matilda", "Max", "Maxwell", "Mckenzie",
    "Melody", "Melissa", "Mia", "Miguel", "Mikayla", "Miley", "Mina", "Miranda",
    "Miriam", "Molly", "Monica", "Mya", "Myra", "Nadia", "Nash", "Natalia",
    "Nate", "Neil", "Nicholas", "Nicole", "Nina", "Noelle", "Norman", "Nova",
    "Oscar", "Paige", "Paul", "Paula", "Payton", "Phoebe", "Poppy", "Priscilla",
    "Rafael", "Raquel", "Raven", "Raymond", "Rene", "Riley", "River", "Rochelle",
    "Rodney", "Roger", "Rosalie", "Rose", "Roselyn", "Rowan", "Roy", "Russell",
    "Sabrina", "Sage", "Salem", "Sally", "Samson", "Sandra", "Santiago", "Sasha",
    "Sawyer", "Scott", "Selena", "Serena", "Shane", "Shannon", "Shawn", "Shelby",
    "Shirley", "Sierra", "Silas", "Skye", "Sloane", "Sonia", "Sonya", "Stacy",
    "Stanley", "Summer", "Tara", "Tate", "Tessa", "Tess", "Tobias", "Tony",
    "Travis", "Trevor", "Trinity", "Troy", "Valeria", "Veronica", "Victoria", "Vincent",
    "Wade", "Walter", "Warren", "Waylon", "Wendy", "Weston", "Whitney", "Will",
    "Winona", "Xander", "Yara", "Yvette", "Zachariah", "Zara", "Zayden", "Zelda"
]

names = ['Alice',"Bob","Charlie","Josh",'James', 'Ethan','David','Jackson','Peter','Mohammed','Joseph','Kim','Michael','Ian','Chris','Aziz','Eeshan','Karl','Thomas','Brian']
user = input("Enter a name to search: ")

start_time = time.perf_counter()
def linsearch(user):
    lincount = 0
    for i in range(len(names3)):
        if names3[i] == user:
            lincount += 1
            return "Found at position", i, lincount
        lincount += 1
    return "not found", lincount

print(linsearch(user))
end_time = time.perf_counter()
timetaken = end_time - start_time
print(f"{timetaken:.40f}")

names4 = [[None] for _ in range(500)]

names2 = [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None]]
def hashing(user):
    product = 1
    for letter in user:
        product = product * ord(letter)
    value = product / 1000
    value = value % 10
    return int(value) 


def search(user):
    hashcount = 0
    index = hashing(user)
    print(index)
    for i in names4[index]:
        if i == user:
            hashcount +=1
            return "Found", hashcount
        hashcount +=1
    return "Not Found", hashcount

for i in names3:
    index = hashing(i)
    if names4[index][0] == None:
        names4[index][0] = i
    else:
        names4[index].append(i)
# print(names4)
start_time2 = time.perf_counter()
print(search(user))
end_time2 = time.perf_counter()
total = end_time2 - start_time2
print(f"{total:.40f}")  

def bubblesort(names3):
    for i in range(len(names3)):
        swapped = False
        for j in range(0,len(names3)-i-1):
            if names3[j] > names3[j+1]:
                names3[j],names3[j+1] = names3[j+1],names3[j]
                swapped = True
        if not swapped:
            break
    return names3

names5 = bubblesort(names3)
# print(names5)

def binsearch(names5,user):
    value = user
    found = False
    comparisons = 0
    low = 0
    high = len(names5)-1
    while low <= high:
        mid = (low+high)//2
        comparisons +=1
        if names5[mid] == value:
            found = True
            break
        elif names5[mid] < value:
            low = mid+1
        else:
            high=mid-1
    if found:
        return "Found", comparisons
    else:
        return "Not Found", comparisons
binstart = time.perf_counter()
print(binsearch(names5,user))
binend = time.perf_counter()
bintotal = binend - binstart
print(f"{bintotal:.40f}")