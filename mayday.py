# this program decode NATO Phonetic Alphabet to leet phrases . for example SOS call in mayday answered by a ship , but its seems as gobbledygook !!!
gobbledygook ='Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven'
numbers_dict = {"Zero": '0', "One": '1', "Two": '2', "Three": '3', "Four": '4', "Five": '5',"Six": '6', "Seven": '7', "Eight": '8', "Nine": '9', "Dash":"-" }

gook_list = gobbledygook.split(' ')
result_list = []
for item in gook_list:
    if item in numbers_dict:
        result_list.append(numbers_dict[item])
    else:
        result_list.append(item[0])
result_str = ''.join(result_list)
print("\n===============>>>\n",result_str,"\n===============>>>\n")