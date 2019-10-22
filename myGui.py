from guizero import App, Text, TextBox, PushButton

app = App(title='Michael Cook', bg='purple', width=300, height=300)
username = 'Michael'
password = 'Stinky'
picture =
def check_input():
    if un_box.value == username and pw_box.value == password:
        message = Text(app, text='Correct')
    else:
        message = Text(app, text='Incorrect')

un_box = TextBox(app)
pw_box = TextBox(app)
submit = PushButton(app, text='SUBMIT', command=check_input)

# text1 = Text(app, text='Hello SCHMIDT!', size=100, font='Blackadder ITC', color=(0, 0, 240), align='center')
# app.yesno(title='Yes or No', text='Would you like to close this window?')
# app.warn(title='oh no!', text='Something bad has happened!')

app.display()
