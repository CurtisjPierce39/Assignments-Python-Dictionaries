#Question 2 Task 1

def add_service_ticket():

    service_ticket = {
        "ticket number": len(service_tickets_list) + 1,
        "customer": "",
        "issue": "",
        "status": "Open"
}

    service_ticket["customer"] = input("Please enter customer name: ")
    service_ticket["issue"] = input("Please explain the issue: ")
    service_ticket["status"] = input("What is the status of this ticket?: (Open/Closed)")

    return service_ticket

def update_status(service_ticket):
    if len(service_tickets_list) == 0:
        print("Status:", service_ticket["status"])
    new_status = input("Enter updated status (Open/Closed): ")
    service_ticket["status"] = new_status

def display_tickets(service_ticket):
    if len(service_ticket) == 0:
        print("---No service tickets on file---")

    print("---Ticket Number:", service_ticket["ticket number"])
    print("---Customer:", service_ticket["customer"])
    print("---Issue: ", service_ticket["issue"])
    print("---Status: ", service_ticket["status"])

service_tickets_list = {}

def main():
    while True:
        print("Service Ticket System")
        print("****Menu****")
        print("1. Add New Service Ticket")
        print("2. Update Ticket Status")
        print("3. Display All Tickets")
        print("4. Exit System")

        user_input = input("Please select an option (1/2/3/4): ")
        
        if user_input == '1':
            add_ticket = add_service_ticket()
            service_tickets_list[add_ticket["ticket number"]] = add_ticket
            print("---New Ticket Added!---")
        
        elif user_input == '2':
            ticket_number = int(input("Enter ticket number to update: "))
            if ticket_number in service_tickets_list:
                update_status(service_tickets_list[ticket_number])
                print("---Ticket Status Updated---")
            else:
                print("---No Service Tickets to Update!---")
        
        elif user_input == '3':
            ticket_number = int(input("Choose a ticket to view: "))
            if ticket_number in service_tickets_list:
                display_tickets(service_tickets_list[ticket_number])
            else:
                print("---No Service Tickets to View!---")
        
        elif user_input == '4':
            print("Thank you for using the Service Ticket System! Have a Nice Day!")
            break

        else:
            print("---Entry not available. Please try again.---")

main()