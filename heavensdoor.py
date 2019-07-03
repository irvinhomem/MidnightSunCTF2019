import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


door_url = "http://heavensdoor-01.play.midnightsunctf.se:10488"

operation = 'knock'
#arguments = ['0','0','0','0','0','0','0','0','0','0']
arguments = [0,0,0,0,0,0,0,0,0,0]
separator = '/'

def make_requests():
    test = str(arguments)

    #url_params = separator.join(str(arguments))
    url_params = separator.join([str(i) for i in arguments])

    print(type(url_params))
    #print("Test:" + test)
    print("Test:", url_params)

    full_url = door_url + '/' + operation + '/' + url_params

    print(full_url)

    r = requests.get(full_url)
    print('Status:' + str(r.status_code))
    print(r.content)

    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)

    #my_data = soup.find("i", text="Suddenly,").text
    my_data = soup.find("i").contents

    print(my_data)

    right_side = my_data[0].split('t')[1]
    print(right_side)

    #var1 = right_side
    values = right_side.split('res')
    var_1 = values[0]
    var_2 = values[1]
    print("Val1=" + var_1 + "and Val2=" + var_2)

    time_value = find_between(var_1, '(', ')')
    result = find_between(var_2, '(', ')')

    print("Time =" + time_value)
    print("RESULT =" + result)

    #return([time_value, result])
    return {'t':time_value, 'res': result}

def find_between(my_text, start, end):
    answer = my_text[my_text.find(start) + len(start):my_text.rfind(end)]
    return answer

test_values = []
for i in range(100):
    test_values.append(make_requests())

print(test_values)

plt.plot(test_values.get('t'), test_values['res'], marker='o')
plt.show()