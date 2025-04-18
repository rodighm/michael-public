import tkinter

#Calculation
def calc():
    try:
        devs = float(devs_entry.get())
        qe = float(qes_entry.get())
        benchwage = float(wage_entry.get())
        weeks = float(weeks_entry.get())
        prodhours = float(prodhours_entry.get())
        ptspersprtint = float(ptspersprint_entry.get())
        projsize = float(projsize_entry.get())
        
        
        qes = qe / devs
        sm = 1 / (devs + qes)
        pm = 1 / (devs + qes)
        persons = 1 + sm + pm + qes
        wage = benchwage * persons
        smwage = benchwage * sm
        pmwage = benchwage * pm
        qewage = benchwage * qes
        
        costperpt = ((prodhours * weeks)*wage)/ptspersprtint
        estcost = costperpt * projsize
        results_label.config(text = '---------------------------------------------------------------\n'
                             'Estimated Cost:\t\t\t'f"${estcost:,.2f}\n"
                             '---------------------------------------------------------------\n'
                             'Total Resources:\t\t\t'f"{persons:,.2f}\n" 
                             'Resource Wage:\t\t\t'f"${wage:,.2f}\n"
                             '\tFor Every Developer:\t'f"${benchwage:,.2f}\n"
                             '\tQuality Engineer:\t\t' f"${qewage:,.2f}\n"
                             '\tScrum Master:\t\t' f"${smwage:,.2f}\n"
                             '\tProduct Manager:\t\t'+ f"${pmwage:,.2f}\n"
                             '---------------------------------------------------------------\n'
                             'Cost per Point:\t\t\t'f"${costperpt:,.2f}\n" 
                             '===========================================\n'
                             'Product Managers and Scrum Masters are included in the calculation as a portion of a developer because a Product Manager or Scrum Master is aligned to multiple developers and quality engineers',
                             width = 50, 
                             anchor = "w", 
                             justify = "left",
                             wraplength=350 )
    except ValueError:
        print("Error: Please only enter numbers.")
        print('===================================\n')



#Form Start
window = tkinter.Tk()
window.title("Program Cost Estimator")

frame = tkinter.Frame(window)
frame.pack()


team_frame = tkinter.LabelFrame(frame, text = "Average Team Configuration")
team_frame.grid(row=0 , column=0, padx= 5, pady= 5)

devs_label = tkinter.Label(team_frame, text = "Average developers on a squad:", anchor="w", width = 40)
devs_label.grid(row=0, column=0)
devs_entry = tkinter.Entry(team_frame)
devs_entry.grid(row=0, column=1)

qes_label = tkinter.Label(team_frame, text = "Average quality engineers on a squad:", anchor = "w", width = 40)
qes_label.grid(row=1, column=0)
qes_entry = tkinter.Entry(team_frame)
qes_entry.grid(row=1,column=1)

wage_label = tkinter.Label(team_frame, text = 'Benchmark wage (hourly):', anchor = "w", width = 40)
wage_label.grid(row=2, column=0)
wage_entry = tkinter.Entry(team_frame)
wage_entry.grid(row=2, column=1)

sprint_frame = tkinter.LabelFrame(frame, text = "Sprint Configuration")
sprint_frame.grid(row=3 , column=0, padx= 5, pady= 5)

weeks_label = tkinter.Label(sprint_frame, text = 'Weeks per sprint:', anchor = "w", width = 40)
weeks_label.grid(row=4, column=0)
weeks_entry = tkinter.Entry(sprint_frame)
weeks_entry.grid(row=4, column=1)

prodhours_label = tkinter.Label(sprint_frame, text = 'Production hours a week:', anchor = "w" , width = 40)
prodhours_label.grid(row=5, column = 0)
prodhours_entry = tkinter.Entry(sprint_frame)
prodhours_entry.grid(row = 5, column = 1)

ptspersprint_label = tkinter.Label(sprint_frame, text = 'Average points for a developer:', anchor = "w", width = 40 )
ptspersprint_label.grid(row=6, column=0)
ptspersprint_entry = tkinter.Entry(sprint_frame)
ptspersprint_entry.grid(row=6, column=1)

project_frame = tkinter.LabelFrame(frame, text = "Project Configuration")
project_frame.grid(row=7 , column=0, padx= 5, pady= 5)

projsize_label = tkinter.Label(project_frame, text = 'Project Size (points)', anchor = "w", width = 40)
projsize_label.grid(row=8, column=0)
projsize_entry = tkinter.Entry(project_frame)
projsize_entry.grid(row=8, column=1)



#button
button = tkinter.Button(frame, text="Estimate", command=calc)
button.grid(row=9, column=0, padx=5, pady=5)

#======================================================



# Results frame
results_frame = tkinter.LabelFrame(frame, text = "Project Configuration")
results_frame.grid(row=10 , column=0, padx= 5, pady= 5)

# Results label
results_label = tkinter.Label(results_frame, text="")
results_label.pack()
#======================================================




#button action
window.mainloop()


