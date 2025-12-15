"""Module creating a GUI to compare Gear from LOTRO"""


import pickle
import customtkinter as ctk


items = []
essence_values = {
    'vitality': 3185,
    'primary': 2609, 
    'crit': 5277,
    'mastery': 4380,
    'finesse': 6994,
    'mitigation': 4221,
    'outheal': 12102
}
classes = {
    # 0:Might, 1:Agility, 2:Will
    # 0:Crit, 1:Finesse, 2:Mastery, 3:OGH, 4:Physmit, 5:Tactmit

    'Beorning': [[1, 0, 3, 3, 1, 1], [2, 1, 2, 2, 0, 0], [0, 1, 1, 1, 1.5, 1.5]],
    'Brawler': [[1, 0, 3, 3, 1, 1], [2, 1, 2, 2, 0, 0], [0, 1, 1, 1, 1.5, 1.5]],
    'Burglar': [[1.5, 1.5, 2, 2, 0, 0], [1, 0, 3, 3, 1, 1], [0.5, 1.5, 2, 2, 1, 0]],
    'Captain': [[1, 0, 3, 3, 1, 1], [2, 1, 2, 2, 0, 0], [0, 1, 1, 1, 1.5, 1.5]],
    'Champion': [[1, 0, 3, 3, 1, 1], [2, 1, 2, 2, 0, 0], [0, 1, 1, 1, 1.5, 1.5]],
    'Guardian': [[1, 0, 3, 3, 1, 1], [2, 1, 2, 2, 0, 0], [0, 1, 1, 1, 1.5, 1.5]],
    'Hunter': [[1.5, 1.5, 2, 2, 0, 0], [1, 0, 3, 3, 1, 1], [0.5, 1.5, 2, 2, 1, 0]],
    'Loremaster': [[1.5, 1.5, 2, 2, 0, 0], [2, 1, 2, 2, 0, 0], [1, 0, 3, 3, 1, 1]],
    'Mariner': [[1.5, 1.5, 2, 2, 0, 0], [1, 0, 3, 3, 1, 1], [0.5, 1.5, 2, 2, 1, 0]],
    'Minstrel': [[1, 0, 2, 4, 0, 0], [2, 1, 2, 2, 0, 0], [1, 0, 3, 3, 1, 1]],
    'Runekeeper': [[1, 0, 2, 4, 0, 0], [2, 1, 2, 2, 0, 0], [1, 0, 3, 3, 1, 1]],
    'Warden': [[1.5, 1.5, 2, 2, 0, 0], [1, 0, 3, 3, 1, 1], [0, 1, 1, 1, 1.5, 1.5]]
}


class NavFrame(ctk.CTkFrame):
    """Frame which contains Checkboxes to select stuff"""
    def __init__(self, master):
        super().__init__(master)
        self.class_select = ctk.CTkOptionMenu(self, values=list(classes.keys()), width=200)
        self.vitality_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))
        self.might_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))
        self.agility_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))
        self.will_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))
        self.crit_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))
        self.mastery_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))
        self.finesse_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))
        self.physmit_checkbox = ctk.CTkCheckBox(self, text='', width=140, variable=ctk.IntVar(self, 1))
        self.tactmit_checkbox = ctk.CTkCheckBox(self, text='', width=140, variable=ctk.IntVar(self, 1))
        self.ogheal_checkbox = ctk.CTkCheckBox(self, text='', width=140, variable=ctk.IntVar(self, 1))
        self.slot_checkbox = ctk.CTkCheckBox(self, text='', width=80, variable=ctk.IntVar(self, 1))

        self.class_select.grid()
        self.vitality_checkbox.grid(row=0, column=1)
        self.might_checkbox.grid(row=0, column=2)
        self.agility_checkbox.grid(row=0, column=3)
        self.will_checkbox.grid(row=0, column=4)
        self.crit_checkbox.grid(row=0, column=5)
        self.mastery_checkbox.grid(row=0, column=6)
        self.finesse_checkbox.grid(row=0, column=7)
        self.physmit_checkbox.grid(row=0, column=8)
        self.tactmit_checkbox.grid(row=0, column=9)
        self.ogheal_checkbox.grid(row=0, column=10)
        self.slot_checkbox.grid(row=0, column=11)


class ItemFrame(ctk.CTkFrame):
    """Frame which contains Entry Fields for Item Values"""
    def __init__(self, master):
        super().__init__(master)
        self.name_entry = ctk.CTkEntry(self, placeholder_text='Name', width=200)
        self.vitality_entry = ctk.CTkEntry(self, placeholder_text='Vitality', width=80)
        self.might_entry = ctk.CTkEntry(self, placeholder_text='Might', width=80)
        self.agility_entry = ctk.CTkEntry(self, placeholder_text='Agility', width=80)
        self.will_entry = ctk.CTkEntry(self, placeholder_text='Will', width=80)
        self.crit_entry = ctk.CTkEntry(self, placeholder_text='Crit', width=80)
        self.mastery_entry = ctk.CTkEntry(self, placeholder_text='Mastery', width=80)
        self.finesse_entry = ctk.CTkEntry(self, placeholder_text='Finesse', width=80)
        self.physmit_entry = ctk.CTkEntry(self, placeholder_text='Physical Mitigation')
        self.tactmit_entry = ctk.CTkEntry(self, placeholder_text='Tactical Mitigation')
        self.ogheal_entry = ctk.CTkEntry(self, placeholder_text='Outgoing Healing')
        self.slot_entry = ctk.CTkEntry(self, placeholder_text='Slots', width=80)
        self.result_label = ctk.CTkLabel(self, text='0.0', width=80)
        self.save_button = ctk.CTkButton(self, text='\u2714', command=self.calculate)
        self.abort_button = ctk.CTkButton(self, text='\u274C', command=self.abort)

        self.name_entry.grid()
        self.vitality_entry.grid(row=0, column=1)
        self.might_entry.grid(row=0, column=2)
        self.agility_entry.grid(row=0, column=3)
        self.will_entry.grid(row=0, column=4)
        self.crit_entry.grid(row=0, column=5)
        self.mastery_entry.grid(row=0, column=6)
        self.finesse_entry.grid(row=0, column=7)
        self.physmit_entry.grid(row=0, column=8)
        self.tactmit_entry.grid(row=0, column=9)
        self.ogheal_entry.grid(row=0, column=10)
        self.slot_entry.grid(row=0, column=11)
        self.result_label.grid(row=0, column=12)
        self.save_button.grid(row=0, column=13)
        self.abort_button.grid(row=0, column=14)

        items.append(self)

    def calculate(self):
        """Calculates an item and displays it"""
        might = int(0 if (x := self.might_entry.get())=='' else eval(safe_translate(x)))
        agility = int(0 if(x := self.agility_entry.get())=='' else eval(safe_translate(x)))
        will = int(0 if(x := self.will_entry.get())=='' else eval(safe_translate(x)))
        selected_class_multipliers = classes[nav_frame.class_select.get()]
        result_vit = int(0 if (x := self.vitality_entry.get())=='' else eval(safe_translate(x)))/essence_values['vitality'] if nav_frame.vitality_checkbox.get() else 0
        result_crit = (int(0 if (x := self.crit_entry.get())=='' else eval(safe_translate(x)))+selected_class_multipliers[0][0]*might+selected_class_multipliers[1][0]*agility+selected_class_multipliers[2][0]*will)/essence_values['crit'] if nav_frame.crit_checkbox.get() else 0
        result_mastery = (int(0 if(x := self.mastery_entry.get())=='' else eval(safe_translate(x)))+selected_class_multipliers[0][2]*might+selected_class_multipliers[1][2]*agility+selected_class_multipliers[2][2]*will)/essence_values['mastery'] if nav_frame.mastery_checkbox.get() else 0
        result_physmit = (int(0 if(x := self.physmit_entry.get())=='' else eval(safe_translate(x)))+selected_class_multipliers[0][4]*might+selected_class_multipliers[1][4]*agility+selected_class_multipliers[2][4]*will)/essence_values['mitigation'] if nav_frame.physmit_checkbox.get() else 0
        result_tactmit = (int(0 if(x := self.tactmit_entry.get())=='' else eval(safe_translate(x)))+selected_class_multipliers[0][5]*might+selected_class_multipliers[1][5]*agility+selected_class_multipliers[2][5]*will)/essence_values['mitigation'] if nav_frame.tactmit_checkbox.get() else 0
        result_ogh = (int(0 if(x := self.ogheal_entry.get())=='' else eval(safe_translate(x)))+selected_class_multipliers[0][3]*might+selected_class_multipliers[1][3]*agility+selected_class_multipliers[2][3]*will)/essence_values['outheal'] if nav_frame.ogheal_checkbox.get() else 0
        result_finesse = (int(0 if(x := self.finesse_entry.get())=='' else eval(safe_translate(x)))+selected_class_multipliers[0][1]*might+selected_class_multipliers[1][1]*agility+selected_class_multipliers[2][1]*will)/essence_values['finesse'] if nav_frame.finesse_checkbox.get() else 0
        result_slots = int(0 if(x := self.slot_entry.get())=='' else eval(safe_translate(x))) if nav_frame.slot_checkbox.get() else 0
        result = round(result_vit+result_crit+result_mastery+result_physmit+result_tactmit+result_ogh+result_finesse+result_slots, 2)
        self.result_label.configure(text=result, width=80)

    def abort(self):
        """Removes this itemframe"""
        items.remove(self)
        for i, item in enumerate(items):
            item.grid(row=i+1)
        self.destroy()
    
    def to_list(self):
        """Converts CtkFrame to List"""
        return [self.name_entry.get(), self.vitality_entry.get(), self.might_entry.get(), self.agility_entry.get(), self.will_entry.get(), self.crit_entry.get(), self.mastery_entry.get(), self.finesse_entry.get(), self.physmit_entry.get(), self.tactmit_entry.get(), self.ogheal_entry.get(), self.slot_entry.get(), self.result_label.cget('text')]
    
    def from_list(self, list):
        """Fills this CTkFrame with data from List"""
        if len(list[0])>0: self.name_entry.insert(0, list[0])
        if len(list[1])>0: self.vitality_entry.insert(0, list[1])
        if len(list[2])>0: self.might_entry.insert(0, list[2])
        if len(list[3])>0: self.agility_entry.insert(0, list[3])
        if len(list[4])>0: self.will_entry.insert(0, list[4])
        if len(list[5])>0: self.crit_entry.insert(0, list[5])
        if len(list[6])>0: self.mastery_entry.insert(0, list[6])
        if len(list[7])>0: self.finesse_entry.insert(0, list[7])
        if len(list[8])>0: self.physmit_entry.insert(0, list[8])
        if len(list[9])>0: self.tactmit_entry.insert(0, list[9])
        if len(list[10])>0: self.ogheal_entry.insert(0, list[10])
        if len(list[11])>0: self.slot_entry.insert(0, list[11])
        self.result_label.configure(text=list[12])
        return self


def add_item():
    """Adds an Itemrow and moves the button down"""
    new_item = ItemFrame(root)
    new_item.grid(row=len(items), sticky='w')
    add_button.grid(row=len(items)+1)


def on_close():
    """Saves the state of the window"""
    with open('save.pickle', 'wb') as f:
        d = [l.to_list() for l in items]
        pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
    root.destroy()


def safe_translate(string):
    """Removes everthing from a string except numbers and +-*"""
    return ''.join(c for c in string if c in '0123456789+-*')


ctk.set_default_color_theme('dark-blue') # "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode('dark') # "system" (standard), "dark", "light"
root = ctk.CTk()
root.geometry('1630x500')
root.title('Gear Comparer')
add_button = ctk.CTkButton(root, text='+', command=add_item)
nav_frame = NavFrame(root)
nav_frame.grid(sticky='w')
try:
    with open('save.pickle', 'rb') as file:
        data = list(pickle.load(file))
        if len(data) == 0:
            first_item = ItemFrame(root)
            first_item.grid(row=1, sticky='w')
        for l in data:
            ItemFrame(root).from_list(l).grid(row=len(items), sticky='w')
except Exception as e:
    first_item = ItemFrame(root)
    first_item.grid(row=1, sticky='w')
add_button.grid(row=len(items)+1)
root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()
