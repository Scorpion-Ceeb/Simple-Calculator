import tkinter as tk
from colfonts import * 



class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x800')
        self.window.resizable(0,0)
        self.window.title = 'My Calculator'

        self.display_frame = self.create_buttons_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total_expression =''
        self.current_expression=''

        self.total_exp_frame, self.current_exp_frame = self.create_label_expressions()

        self.digits ={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),'.':(4,1)
        }
        self.buttons_operators=[]

        self.operators = {
            '/': '\u00F7','*':'\u00D7', '+':'+', '-':'-'
        }

        self.create_buttons()
        self.config_buttons_size()
        self.create_operators_buttons()
        self.create_clear_button()
        self.create_equals_button()



    def run(self):
        self.window.mainloop()

    def evaluate_expression(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        self.current_expression = str(eval(self.total_expression))

        self.total_expression =''
        self.update_current_label()

    def append_expression(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression=''

        self.update_total_label()
        self.update_current_label()

        self.check_buttons()

    def clear_expression(self):
        self.current_expression =''
        self.update_current_label()
        self.total_expression =''
        self.update_total_label()

        self.check_buttons()

    def update_total_label(self):
        self.total_exp_frame.config(text= self.total_expression)
    
    def update_current_label(self):
        self.current_exp_frame.config(text= self.current_expression)
    
    def add_to_expression(self, value):
        self.current_expression+=str(value)
        self.update_current_label()

        self.check_buttons()

    def config_buttons_size(self):
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
    
    def check_buttons(self):
        if self.disable_operators():
            for bton in self.buttons_operators:
                bton.config(state= tk.DISABLED)
        else:
            for bton in self.buttons_operators:
                bton.config(state= tk.NORMAL)

    def is_operator(self):

        for oper in list(self.operators.keys())[0:3]:
            if(self.total_expression[-1] == oper):
                return True
        
        return False
    
    def disable_operators(self):

        if len(self.current_expression) == 0 and len(self.total_expression) == 0:
            return True

        if (not(len(self.total_expression) == 0) and self.is_operator()) and (len(self.current_expression) == 0):
            return True
        
        return False

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, 
            borderwidth=0, font=DIGIT_FONT_SIZE, 
            command=lambda : self.evaluate_expression())
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
        self.buttons_operators.append(button)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text= 'C',bg=WHITE, fg=CLEAR_LABEL_COLOR, 
                borderwidth=0, font=DIGIT_FONT_SIZE, command= lambda :self.clear_expression())
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_operators_buttons(self):
        self.create_div_operator()
        self.create_mult_operator()
        self.create_sum_operator()
        self.create_subs_operator()

    def create_sum_operator(self):
        
        button = tk.Button(self.buttons_frame, text='+', bg=WHITE, fg=LABEL_COLOR, 
                borderwidth=0, font=DIGIT_FONT_SIZE, 
                command=lambda x='+': self.append_expression(x), state= tk.DISABLED)
        button.grid(row=2, column= 4, sticky=tk.NSEW)
        
        self.buttons_operators.append(button)

    def create_mult_operator(self):
        
        button = tk.Button(self.buttons_frame, text='\u00D7', bg=WHITE, fg=LABEL_COLOR, 
                borderwidth=0, font=DIGIT_FONT_SIZE, 
                command=lambda x='*': self.append_expression(x), state= tk.DISABLED)
        button.grid(row=1, column= 4, sticky=tk.NSEW)
        self.buttons_operators.append(button)
    
    def create_div_operator(self):
        
        button = tk.Button(self.buttons_frame, text='\u00F7', bg=WHITE, fg=LABEL_COLOR, 
                borderwidth=0, font=DIGIT_FONT_SIZE, 
                command=lambda x='/': self.append_expression(x), state= tk.DISABLED)
        button.grid(row=0, column= 4, sticky=tk.NSEW)
        self.buttons_operators.append(button)
    
    def create_subs_operator(self):
        
        button = tk.Button(self.buttons_frame, text='-', bg=WHITE, fg=LABEL_COLOR, 
                borderwidth=0, font=DIGIT_FONT_SIZE, 
                command=lambda x='-': self.append_expression(x))
        button.grid(row=3, column= 4, sticky=tk.NSEW)

    def create_buttons(self):

        for digit, grid_number in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, 
                    borderwidth=0, font=DIGIT_FONT_SIZE, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_number[0], column= grid_number[1], sticky=tk.NSEW)      

    def create_label_expressions(self):

        label_total = tk.Label(self.display_frame, text= self.total_expression,
            bg= LIGHT_GRAY, fg=LABEL_COLOR, anchor=tk.E, padx=24, font=SMALL_FONT_SIZE)
        
        label_total.pack(expand=True, fill='both')

        label_current = tk.Label(self.display_frame, text=self.current_expression,
            bg = LIGHT_GRAY, fg = LABEL_COLOR, anchor=tk.E, font=LARGE_FONT_SIZE)
        
        label_current.pack(expand=True, fill='both')

        return label_total, label_current

    def create_display_frame(self):

        frame = tk.Frame(self.window, height=200, bg= LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)

        frame.pack(expand=True, fill='both')

        return frame
    

if __name__ == '__main__':
    calulator = Calculator()
    calulator.run()
