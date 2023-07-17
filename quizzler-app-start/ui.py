from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizerInter:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quizzler'
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score = Label(text='Score:', bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     text=';aksj;',
                                                     font=('arial', 20, 'italic'),
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2,  pady=40)
        self.right_img = PhotoImage(file='images\/true.png')
        self.right = Button(image=self.right_img, command=self.right_clicked)
        self.right.grid(column=0, row=2)
        self.wrong_img = PhotoImage(file='images\/false.png')
        self.wrong = Button(image=self.wrong_img, command=self.wrong_clicked)
        self.wrong.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')
    def right_clicked(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def wrong_clicked(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score.config(text=f'Score: {self.quiz.score}/10')
        else:
            self.canvas.config(bg='pink')
        self.window.after(1000, self.get_next_question)
