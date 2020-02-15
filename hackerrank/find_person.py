def found_person(people, num):
    for idx in range(num):
        person = str(input()).lower()
        if person in people.keys():
            print(f'{person}={people[person]}')
        else:
            print('Not found')

if __name__ == '__main__':
    n = -1
    while n < 1 or n > 10**5:
        n = int(input())
    
    dic_people = {}
    for idx in range(n):
        person, phone = str(input()).lower().split(' ')
        dic_people[person] = phone
    
    found_person(dic_people, n)