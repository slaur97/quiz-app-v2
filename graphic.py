from tkinter import *
from functionality import run_questions
class win:
    def __init__(self, run:run_questions):
        self.run=run
        self.window=Tk()
        self.window.config(padx=100,pady=100,background="gray",width=500,height=500)
        self.stop=False
        
       
        self.create()
   
        
    def check_answer(self):
        if self.button0.get() == 1 and self.check_button0.cget("text") == self.correct_answer:
            self.run.score+=1
        if self.button1.get() == 1 and self.check_button1.cget("text") == self.correct_answer:
            self.run.score+=1
        if self.button2.get() == 1 and self.check_button2.cget("text") == self.correct_answer:
            self.run.score+=1
        if self.button3.get() == 1 and self.check_button3.cget("text") == self.correct_answer:
            self.run.score+=1
        print(self.run.number_questions)
        if(self.run.number_questions==38):
            self.canvas.itemconfig(self.canvas_text, text = f"Scor Final {self.run.score}")
            self.check_button0.destroy()
            self.check_button1.destroy()
            self.check_button2.destroy()
            self.check_button3.destroy()
            self.score_label.destroy()
            self.stop=True
            
    def destroy_check_button(self): 
        self.check_answer()
        self.check_button0.destroy()
        self.check_button1.destroy()
        self.check_button2.destroy()
        self.check_button3.destroy()
        self.create()

    def create(self):   
        if self.stop == False:
            self.score_label=Label(text=F"score:{self.run.score}", foreground="black")
            self.score_label.grid(row=0,column=1)
            self.canvas=Canvas(width=300,height=250,background="gray",highlightthickness=0)
            self.canvas_text=self.canvas.create_text(150,
                                                    125,
                                                    width=280,
                                                    text=self.run.next_question(),
                                                    fill="black",
                                                    font=("Arial",15,"bold"))
            self.canvas.grid(row=1,column=0,columnspan=2) # columnspan specifica ca se intinde pe 2 coloane
            self.button_correct=None

            list_answers=self.run.next_answers()
            self.correct_answer=self.run.correct_answers()
    
            
                    
            self.button0,self.button1,self.button2,self.button3=IntVar(),IntVar(),IntVar(),IntVar()

            

        
            self.check_button0=Checkbutton(variable=self.button0,text=list_answers[0],background="gray")    
            self.check_button0.grid(row=2,column=0,padx=20,pady=20)
            

        
            self.check_button1=Checkbutton(variable=self.button1,text=list_answers[1],background="gray")    
            self.check_button1.grid(row=2,column=1)

            self.check_button2=Checkbutton(variable=self.button2,text=list_answers[2],background="gray")    
            self.check_button2.grid(row=3,column=0)

            self.check_button3=Checkbutton(variable=self.button3,text=list_answers[3],background="gray")    
            self.check_button3.grid(row=3,column=1)

            photo=PhotoImage(file="image_next.png")
            button_next=Button(image=photo,command=self.destroy_check_button)
            button_next.grid(row=4,column=0,columnspan=2)

        self.window.mainloop()
