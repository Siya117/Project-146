from tkinter import*

root = Tk()

root.title("Fibonacci series")
root.geometry("400x400")

enter_word = Entry(root)
label_series = Label(root, text = "Fibonnoci Series ")
label_sum = Label(root, text = "Fibbonoci Sum")


def fibonnoci():
    num = int(enter_word.get())
    first_num = 0
    sec_num = 1
    sum = 0
    counter = 1
    sum2 = 0
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "Fibbonoci Sum: " + str(sum2)
        counter = counter + 1
        first_num = sec_num
        sec_num = sum
        sum = first_num + sec_num
        sum2 += sum
                
btn = Button(root, text = "Show Series", command = fibonnoci)
       
enter_word.pack() 
btn.pack()
label_series.pack()
label_sum.pack()

        
root.mainloop()
        
        


