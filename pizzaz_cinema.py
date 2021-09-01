import sys

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~ Welcome to Pizzaz cinema ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()

data = [
    ["The Shining.", "1980.", "2h 26m.", "10:00.", "Room 1"],
    ["Your Name.", "2016.", "1h 52m.", "13:00.", "Room 1"], 
    ["Fate/Stay Night: Heaven's Feel - III. Spring Song.", "2020.", "2h 0m.", "15:00.", "Room 1"], 
    ["The Night Is Short, Walk on Girl.", "2017.", "1h 32m.", "17:30.", "Room 1"],
    ["The Truman Show.", "1998.", "1h 47m.", "19:30.", "Room 1"], 
    ["Genocidal Organ.", "2017.", "1hr 55m.", "21:45.", "Room 1"], 

    ["Jacob's Ladder.", "1990.", "1h 56m.", "10:00.", "Room 2"], 
    ["Parasite.", "2019.", "2h 12m.", "12:15.", "Room 2"], 
    ["The Dark Knight.", "2008.", "2h 32min.", "14:45.", "Room 2"],
    ["Blade Runner 2049.", "2017.", "2h 44m.", "17:45.", "Room 2"], 
    ["The Mist.", "2007.", "2h 6m.", "21:00.", "Room 2"], 
    ["Demon Slayer: Mugen Train.", "2020.", "1h59min.", "23:20.", "Room 2"], 

    ["The Matrix.", "1999.", "2h 16m.", "10:00.", "Room 3"], 
    ["Inception.", "2010.", "2h 42m.", "11:30.", "Room 3"], 
    ["Shutter Island.", "2010.", "2h 19m.", "14:30.", "Room 3"], 
    ["Soul.", "2020.", "1hr 40m.", "17:00.", "Room 3"], 
    ["Mrs. Brown.", "1997.", "1h 41min.", "19:00.", "Room 3"], 
    ["Peppa Pig: Festival of Fun.", "2019.", "1h 8min.", "21:00.", "Room 3"], 
    ["Titanic.", "1997.", "3h 30min.", "22:15.", "Room 3"]
]

seats = [35, 136, 42]


#this function asks for a movie name and checks if the movie name exists
def ask_for_movie_name():
    found_movie = ""
    found = False
    while found == False:
        movie_input = input("What is the name of the movie you want to watch? ").lower()     
        for line in data:  
            movie_name = line[0].rstrip(".").lower()
            if movie_input == movie_name:
                found = True
                found_movie = movie_name
                break       
        if found == False:
            try_again = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ").lower()
            while try_again != "y" and try_again != "n":
                try_again = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ").lower()
            if try_again == "n":
                break
    return found_movie

#this function asks for number of people for a group booking
def ask_for_number_of_people():
    number_of_people = 0
    while number_of_people < 2:
        number_of_people = int(input("How many persons will you like to book for? "))
        if number_of_people < 2:
            invalid_group = input("Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ").lower()
            while invalid_group != "y" and invalid_group != "n":
                invalid_group = input("Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ").lower()
            if invalid_group == "n":
                break
    return number_of_people

#this function searches for the capacity of a room given the movie name        
def seats_of_movie(movie_name):
    number_of_seats = 0
    for line in data:  
        line_movie_name = line[0].rstrip(".").lower()
        if movie_name == line_movie_name:
            room = int(line[4][-1])
            number_of_seats = seats[room - 1]         
    return number_of_seats

#this function will get input for ordering popcorn and their sizes for each person
def popcorn_time(number_of_people):
    popcorn_prices = []
    n = 1
    while n <= number_of_people:
        popcorn_order = input("For person {}, would you like to order popcorn? Y/N".format(n)).lower()
        while popcorn_order != "y" and popcorn_order != "n":
            popcorn_order = input("For person {}, would you like to order popcorn? Y/N".format(n)).lower()
        if popcorn_order == "y":
            popcorn_size = input("Person {} wants popcorn. What size Small, Medium or Large? (S/M/L)".format(n)).lower()
            while popcorn_size != "s" and popcorn_size != "m" and popcorn_size != "l":
                popcorn_size = input("Person {} wants popcorn. What size Small, Medium or Large? (S/M/L)".format(n)).lower()
            if popcorn_size == "s":
                popcorn_prices.append(3.50)
            elif popcorn_size == "m":
                popcorn_prices.append(5.00)
            elif popcorn_size == "l":
                popcorn_prices.append(7.00)
        else:
            popcorn_prices.append(0)
        n += 1
    return popcorn_prices

#this function calculates and prints the seating arrangement    
def seat_allocation(number_of_people):
    n = 1
    while n <= number_of_people:
        seat_number = 2 * n - 1
        print("The seat number for person {} is #{} ".format(n, seat_number))
        n += 1

#this function searches for and calculates the hour of a given movie
def movie_hour(movie_name):
    hour = 0
    for line in data:  
        line_movie_name = line[0].rstrip(".").lower()
        if movie_name == line_movie_name:
            line_time = line[3].rstrip(".").split(":")
            hour = int(line_time[0])
    return hour

#this function calculates whether the amount paid can be divisible by 5c
def divisible_by_5c(price):
  return int(price * 20) == price * 20

#this function gets input for the amount paid as well as calculating the change given
def give_change(final_price):
    paid_amount = float(input("Enter the amount paid: $"))
    while True:
        if not divisible_by_5c(paid_amount):
            print("The input given is not divisible by 5c. Enter a valid payment.")
            paid_amount = float(input("Enter the amount paid: $"))
        elif paid_amount < final_price:
            print("The user is ${:.2f} short. Ask the user to pay the correct amount.".format(final_price - paid_amount))
            paid_amount = float(input("Enter the amount paid: $"))
        else:
            break    
    change = round(paid_amount - final_price, 2)
    print("Change: ${:.2f}".format(change))

    denoms = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05]
    denoms_print = ["$100", " $50", " $20", " $10", " $ 5", " $ 2", " $ 1", " 50c", " 20c", " 10c", "  5c"]
    i = 0
    while change > 0:
        if change >= denoms[i]:
            multiple = change // denoms[i]
            change = round(change - (multiple * denoms[i]), 2)
            print("{}: {}".format(denoms_print[i], int(multiple)))

        i += 1

#this function displays the receipt for popcorn and ticket purchases as well as the discounts offered
def ticket_time(hour, popcorn_prices, number_of_people):
    time_of_ticket = 0
    ticket_price = 0
    if hour < 16:
        ticket_price = 13.00
        time_of_ticket = "before 16:00"
    else:
        ticket_price = 15.00
        time_of_ticket = "from 16:00"
    n = 0
    accumulative_cost = 0
    while n < number_of_people:
        person_cost = popcorn_prices[n] + ticket_price
        accumulative_cost = accumulative_cost + person_cost
        n += 1
    if number_of_people == 1:
        print("For {} person, the initial cost is ${:.2f}".format(number_of_people, accumulative_cost))
    else:
        print("For {} persons, the initial cost is ${:.2f}".format(number_of_people, accumulative_cost))
    n = 0
    number_of_popcorn = 0
    total_popcorn_price = 0
    while n < number_of_people:
        print(' Person {}: Ticket {}'.format(n + 1, time_of_ticket).ljust(34, ' ') + '$' + '{:.2f}'.format(ticket_price).rjust(5, ' '))
        popcorn_size = ""
        if popcorn_prices[n] == 0:
            n += 1
            continue
        elif popcorn_prices[n] == 3.50:
            popcorn_size = "Small"
        elif popcorn_prices[n] == 5.00:
            popcorn_size = "Medium"
        elif popcorn_prices[n] == 7.00:
            popcorn_size = "Large"
        print(' Person {}: {} popcorn'.format(n + 1, popcorn_size).ljust(34, ' ') + '$' + '{:.2f}'.format(popcorn_prices[n]).rjust(5, ' '))

        number_of_popcorn += 1
        total_popcorn_price = total_popcorn_price + popcorn_prices[n]
        n += 1
    print()
    final_price = accumulative_cost
    if accumulative_cost <= 100:
        print(' No discounts applied'.ljust(34, ' ') + '$' + '0.00'.rjust(5, ' '))
    else:
        total_ticket_price = number_of_people * ticket_price
        total_ticket_discount = round(total_ticket_price / 10, 2)
        total_popcorn_discount = round(total_popcorn_price / 5, 2)
        print(' Discount applied tickets x{}'.format(number_of_people).ljust(33, ' ') + '-$' + '{:.2f}'.format(total_ticket_discount).rjust(5, ' '))
        print(' Discount applied popcorn x{}'.format(number_of_popcorn).ljust(33, ' ') + '-$' + '{:.2f}'.format(total_popcorn_discount).rjust(5, ' '))
        final_price = accumulative_cost - total_popcorn_discount - total_ticket_discount
    print()
    final_price = round(round(final_price * 20) / 20, 2)
    print('The final price is'.ljust(34, ' ') + '$' + '{:.2f}'.format(final_price).rjust(5, ' '))
    give_change(final_price)

#if there is no switch provided print below message
if len(sys.argv) < 2:
    print("Usage: python3 pizzaz.py [ --show <timenow> | --book | --group ]")

#show switch options
elif sys.argv[1] == "--show" and len(sys.argv) == 3:
    #check README
    if len(sys.argv[2]) == 5 and sys.argv[2][0].isdigit() and sys.argv[2][1].isdigit() and sys.argv[2][3].isdigit() and sys.argv[2][4].isdigit() and sys.argv[2][2] == ":":
        time = sys.argv[2].split(":")
        hours = int(time[0])
        minutes = int(time[1])
        if hours >= 0 and hours < 24 and minutes >= 0 and minutes < 60:
            for line in data:
                line_time = line[3].rstrip(".").split(":")
                line_hours = int(line_time[0])
                line_minutes = int(line_time[1])
                if line_hours > hours:
                    print(" ".join(line))
                elif line_hours == hours and line_minutes >= minutes:
                    print(" ".join(line))
            print()
            print("Bye.")
        else:
            print("Sorry. This program does not recognise the time format entered. ")
            print()
            print("Bye.")
    else:
        print("Sorry. This program does not recognise the time format entered. ")
        print()
        print("Bye.")

elif sys.argv[1] == "--book" and len(sys.argv) == 2:
    found = False
    #finding movie
    movie_name = 0
    while found == False:
        movie_input = input("What is the name of the movie you want to watch? ").lower()     
        for line in data:  
            movie_name = line[0].rstrip(".").lower()
            if movie_input == movie_name:
                found = True
                break       
        if found == False:
            try_again = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ").lower()
            while try_again != "y" and try_again != "n":
                try_again = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ").lower()
            if try_again == "n":
                print("Bye.")
                break
    if found == True:
        #popcorn options
        popcorn_price = 0
        popcorn = input("Would you like to order popcorn? Y/N ").lower()
        while popcorn != "y" and popcorn != "n":
            popcorn = input("Would you like to order popcorn? Y/N ").lower()
        if popcorn == "y":
            size = input("You want popcorn. What size Small, Medium or Large? (S/M/L) ").lower()
            while size != "s" and size != "m" and size != "l":
                size = input("You want popcorn. What size Small, Medium or Large? (S/M/L) ").lower()
            if size == "s":
                popcorn_price = 3.50
            elif size == "m":
                popcorn_price = 5.00
            elif size == "l":
                popcorn_price = 7.00
        else:
            popcorn_price = 0
        #print seating
        print("The seat number for person 1 is #17")
        
        #receipt of ticket, popcorn and discounts
        ticket_time(movie_hour(movie_name), [popcorn_price], 1)
        print("Bye.")
        
elif sys.argv[1] == "--group" and len(sys.argv) == 2: 
    while True:
        #finding movie
        movie_name = ask_for_movie_name()
        if movie_name == "":
            print("Bye.")
            break
        #ask for number of people
        number_of_people = ask_for_number_of_people()
        if number_of_people < 2:
            print("Bye.")
            break
        #check for enough seating for given movie
        number_of_seats = seats_of_movie(movie_name)
        capacity = 0
        if number_of_seats % 2 == 0:
            capacity = number_of_seats // 2
        else:
            capacity = number_of_seats // 2 + 1
        if number_of_people > capacity:
            retry = input("Sorry, we do not have enough space to hold {} people in the theater room of {} seats. Enter Y to try a different movie name or N to quit.".format(number_of_people, capacity)).lower()
            while retry != "y" and retry != "n":
                retry = input("Sorry, we do not have enough space to hold {} people in the theater room of {} seats. Enter Y to try a different movie name or N to quit.".format(number_of_people, capacity)).lower()
            if retry == "n":
                print("Bye.")
                break
            else:
                continue
        #popcorn options
        popcorn_prices = popcorn_time(number_of_people)
        
        #printing seating allocations
        seat_allocation(number_of_people)

        #receipt of tickets, popcorn and any discounts including initial cost and final cost
        ticket_time(movie_hour(movie_name), popcorn_prices, number_of_people)
        print("Bye.")
        break

#if the switch options are not recognised        
else:
    print("Sorry. This program does not recognise the switch options. ")
    print()
    print("Bye.")


