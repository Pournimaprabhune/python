txt="company12"
a=txt.isalnum()
print(a)


txt1="companyx"
print(txt1.isalpha())

txt2="50800"
print(txt2.isdigit())

txt3="hello wolrd!"
print(txt3.islower())

txt4=" "
print(txt4.isspace())

txt5="THIS IS NOW !"
print(txt5.isupper())

myTuple=("john","peter","vicky")
print("#".join(myTuple))