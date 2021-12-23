import datetime
class Console:
    def print_child(self, child):
        print("The child with the id " + str(child.child_id) + " has the name " + str(
            child.child_name) + ", the date of birth " + str(child.date_of_birth) + ", the adress " + str(
            child.address) + " and he was " + child.child_behaviour.name)

    def print_item(self, item):
        print("The item with the id " + str(item.item_id) + " has the name " + item.item_name)

    def print_letter(self, letter):
        print("The letter with the id " + str(letter.letter_id) + " that was written by the child with the id " + str(
            letter.child_id) + " in the date " + str(
            letter.date_when_was_written) + " has the folowing items " + letter.item_1.item_name + " and " + letter.item_2.item_name)
    def calculate_age(self,child):
        today = datetime.date.today()
        this_year_birthday=datetime.date(today.year,child.date_of_birth.month,child.date_of_birth.day)
        if this_year_birthday < today:
            age=today.year-child.date_of_birth.year
        else:
            age=today.year-child.date_of_birth.year-1
        return age
    def print_letter_with_all_info(self,letter,child):
        print("Dear Santa,"
              "I am "+child.child_name + " I am "+str(self.calculate_age(child)) +" years old. I live at " +child.address+" I have been a very " +child.child_behaviour.name +" child this year! What I would like the most this Christmas is "+letter.item_1.item_name +","+ letter.item_2.item_name)