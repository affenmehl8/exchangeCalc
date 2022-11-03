from tkinter import *
from tkinter.ttk import Separator


class ExchangeCalc:
    root = Tk()
    root.title("Exchange Calculator")
    cur1_name = ""
    cur2_name = ""

    decimal_places = IntVar(value=17)

    def format_float(self, val: float):
        return ('{0:.'+str(self.decimal_places.get())+'f}').format(val)

    def main(self):
        top_frame = Frame(self.root)
        top_frame.pack(side=TOP)

        label_cur1 = Label(top_frame, text="Enter Currency 1:")
        label_cur1.grid(column=0, row=0)

        entry_cur1 = Entry(top_frame)
        entry_cur1.grid(column=1, row=0)

        label_cur2 = Label(top_frame, text="Enter Currency 2:")
        label_cur2.grid(column=0, row=1)

        entry_cur2 = Entry(top_frame)
        entry_cur2.grid(column=1, row=1)

        def update_labels():
            self.cur1_name = entry_cur1.get()
            self.cur2_name = entry_cur2.get()
            label_cur11.configure(text=self.cur1_name + ":")
            label_cur21.configure(text=self.cur2_name + ":")
            label_cur12.configure(text=self.cur1_name + ":")
            label_cur22.configure(text=self.cur2_name + ":")
            label_amt.configure(text="Traded amount in " + self.cur1_name + ":")

            mid_label_cur11.configure(text=self.cur1_name + ":")
            mid_label_cur21.configure(text=self.cur2_name + ":")
            mid_label_cur12.configure(text=self.cur1_name + ":")
            mid_label_cur22.configure(text=self.cur2_name + ":")


        btn1 = Button(top_frame, text="Set Currencies", command=update_labels)
        btn1.grid(column=0, row=2)

        sep0 = Separator(self.root, orient="horizontal")  # ----------------------------------------------------------------------
        sep0.pack(side=TOP, fill=X)

        mid_frame = Frame(self.root)
        mid_frame.pack(side=TOP)

        mid_label_main = Label(mid_frame, text="Swap Rates:", font=("Arial", 16, "bold"), justify=LEFT)
        mid_label_main.pack(side=TOP)

        mid_left_frame = Frame(mid_frame)
        mid_left_frame.pack(side=LEFT)
        mid_label_cur11 = Label(mid_left_frame)
        mid_label_cur11.grid(column=0, row=0)
        mid_entry_cur11 = Entry(mid_left_frame, justify=LEFT)
        mid_entry_cur11.grid(column=1, row=0)
        mid_label_cur21 = Label(mid_left_frame)
        mid_label_cur21.grid(column=0, row=1)
        mid_entry_cur21 = Entry(mid_left_frame, justify=LEFT)
        mid_entry_cur21.delete(0, 'end')
        mid_entry_cur21.insert(0, '1')
        mid_entry_cur21.grid(column=1, row=1)

        def swap_rates():
            if mid_entry_cur11['state'] == 'normal': #linke Seite auf rechte Verrechnen
                mid_val_cur11 = float(mid_entry_cur11.get())
                mid_val_cur21 = float(mid_entry_cur21.get())

                mid_val_cur12 = 1
                mid_val_cur22 = mid_val_cur21 / mid_val_cur11

                mid_entry_cur12.configure(state="normal")
                mid_entry_cur22.configure(state="normal")
                mid_entry_cur12.delete(0, 'end')
                mid_entry_cur22.delete(0, 'end')
                mid_entry_cur12.insert(0, self.format_float(mid_val_cur12))
                mid_entry_cur22.insert(0, self.format_float(mid_val_cur22))
                mid_entry_cur12.configure(state="disabled")
                mid_entry_cur22.configure(state="disabled")

                print(self.format_float(mid_val_cur11))
            elif mid_entry_cur12['state'] == 'normal': #rechte Seite auf linke Verrechnen
                mid_val_cur12 = float(mid_entry_cur12.get())
                mid_val_cur22 = float(mid_entry_cur22.get())

                mid_val_cur11 = mid_val_cur12 / mid_val_cur22
                mid_val_cur21 = 1

                mid_entry_cur11.configure(state="normal")
                mid_entry_cur21.configure(state="normal")
                mid_entry_cur11.delete(0, 'end')
                mid_entry_cur21.delete(0, 'end')
                mid_entry_cur11.insert(0, self.format_float(mid_val_cur11))
                mid_entry_cur21.insert(0, self.format_float(mid_val_cur21))
                mid_entry_cur11.configure(state="disabled")
                mid_entry_cur21.configure(state="disabled")
            else:
                raise ValueError('Unexpected Value for flip')


        btn_swap = Button(mid_frame, text="<->", anchor="center", command=swap_rates)
        btn_swap.pack(side=LEFT)

        mid_right_frame = Frame(mid_frame)
        mid_right_frame.pack(side=LEFT)
        mid_label_cur12 = Label(mid_right_frame)
        mid_label_cur12.grid(column=0, row=0)
        mid_entry_cur12 = Entry(mid_right_frame, justify=LEFT)
        mid_entry_cur12.delete(0, 'end')
        mid_entry_cur12.insert(0, '1')
        mid_entry_cur12.configure(state="disabled")
        mid_entry_cur12.grid(column=1, row=0)
        mid_label_cur22 = Label(mid_right_frame)
        mid_label_cur22.grid(column=0, row=1)
        mid_entry_cur22 = Entry(mid_right_frame, justify=LEFT, state="disabled")
        mid_entry_cur22.grid(column=1, row=1)

        flip = IntVar(value=0)
        def switch_input(s):
            if flip.get() == 0:
                mid_entry_cur11.configure(state="normal")
                mid_entry_cur21.configure(state="normal")
                mid_entry_cur12.configure(state="disabled")
                mid_entry_cur22.configure(state="disabled")
            elif flip.get() == 1:
                mid_entry_cur11.configure(state="disabled")
                mid_entry_cur21.configure(state="disabled")
                mid_entry_cur12.configure(state="normal")
                mid_entry_cur22.configure(state="normal")
            else:
                raise ValueError('Unexpected Value for flip')


        mid_scale = Scale(self.root, orient="horizontal", from_=0, to=1, variable=flip, command=switch_input)
        mid_scale.pack(side=TOP, fill=X)

        sep1 = Separator(self.root, orient="horizontal")  # ----------------------------------------------------------------------
        sep1.pack(side=TOP, fill=X)

        bottom_frame = Frame(self.root)
        bottom_frame.pack(side=TOP)

        label_best_rate = Label(bottom_frame, text="Best Case Exchange Rate:", font=("Arial", 16, "bold"), justify=LEFT)
        label_best_rate.pack(side=TOP)

        bottom_frame_a = Frame(bottom_frame)
        bottom_frame_a.pack(side=TOP)

        label_cur11 = Label(bottom_frame_a)
        label_cur11.grid(column=0, row=0)
        entry_best_cur1 = Entry(bottom_frame_a, justify=LEFT)
        entry_best_cur1.grid(column=1, row=0)

        label_cur21 = Label(bottom_frame_a)
        label_cur21.grid(column=0, row=1)
        entry_best_cur2 = Entry(bottom_frame_a, justify=LEFT)
        entry_best_cur2.grid(column=1, row=1)

        # ----------------------------------------------------------------------

        label_real_rate = Label(bottom_frame, text="Your Exchange Rate:", font=("Arial", 16, "bold"), justify=LEFT)
        label_real_rate.pack(side=TOP)

        bottom_frame_b = Frame(bottom_frame)
        bottom_frame_b.pack(side=TOP)

        label_cur12 = Label(bottom_frame_b)
        label_cur12.grid(column=0, row=0)
        entry_real_cur1 = Entry(bottom_frame_b)
        entry_real_cur1.grid(column=1, row=0)

        label_cur22 = Label(bottom_frame_b)
        label_cur22.grid(column=0, row=1)
        entry_real_cur2 = Entry(bottom_frame_b)
        entry_real_cur2.grid(column=1, row=1)

        sep2 = Separator(bottom_frame, orient="horizontal")  # ----------------------------------------------------------------------
        sep2.pack(side=TOP, fill=X)

        bottom_frame_c = Frame(bottom_frame)
        bottom_frame_c.pack(side=TOP)

        label_amt = Label(bottom_frame_c)
        label_amt.grid(column=0, row=0)
        entry_amt = Entry(bottom_frame_c)
        entry_amt.grid(column=1, row=0)

        def calculate_values():
            # get values to calculate amounts
            cur1_best_val = float(entry_best_cur1.get())
            cur2_best_val = float(entry_best_cur2.get())
            cur1_real_val = float(entry_real_cur1.get())
            cur2_real_val = float(entry_real_cur2.get())
            amt_val = float(entry_amt.get())





            # calculate amounts
            label_could_get.configure(text="You could get " + self.cur2_name + ":")
            could_get_val: float = (cur2_best_val / cur1_best_val) * amt_val
            entry_could_get.configure(state="normal")
            entry_could_get.delete(0, 'end')
            entry_could_get.insert(0, self.format_float(could_get_val))
            entry_could_get.configure(state="disabled")

            label_will_get.configure(text="You will get " + self.cur2_name + ":")
            will_get_val: float = (cur2_real_val / cur1_real_val) * amt_val
            entry_will_get.configure(state="normal")
            entry_will_get.delete(0, 'end')
            entry_will_get.insert(0, self.format_float(will_get_val))
            entry_will_get.configure(state="disabled")

            thats_val: float = will_get_val * (float(cur1_best_val)/float(cur2_best_val))
            label_will_get_in_cur1.configure(text="That's {} in {} by best rate!".format(self.format_float(thats_val), self.cur1_name))

            label_loss_cur1.configure(text="loss of " + self.cur1_name + ":")
            loss_cur1_val = float(amt_val) - thats_val
            entry_loss_cur1.configure(state="normal")
            entry_loss_cur1.delete(0, 'end')
            entry_loss_cur1.insert(0, self.format_float(loss_cur1_val))
            entry_loss_cur1.configure(state="disabled")

            label_loss_cur2.configure(text="loss of " + self.cur2_name + ":")
            loss_cur2_val = could_get_val - will_get_val
            entry_loss_cur2.configure(state="normal")
            entry_loss_cur2.delete(0, 'end')
            entry_loss_cur2.insert(0, self.format_float(loss_cur2_val))
            entry_loss_cur2.configure(state="disabled")

            label_loss_perc.configure(text="percentile loss:")
            perc_loss_val = 1-(will_get_val/could_get_val)
            entry_loss_perc.configure(state="normal")
            entry_loss_perc.delete(0, 'end')
            entry_loss_perc.insert(0, self.format_float(perc_loss_val))
            entry_loss_perc.configure(state="disabled")

        btn2 = Button(bottom_frame_c, text="Calculate", command=calculate_values)
        btn2.grid(column=0, row=1)

        sep3 = Separator(bottom_frame,
                         orient="horizontal")  # ----------------------------------------------------------------------
        sep3.pack(side=TOP, fill=X)

        bottom_frame_d = Frame(bottom_frame)
        bottom_frame_d.pack(side=TOP)

        label_could_get = Label(bottom_frame_d)
        label_could_get.grid(column=0, row=0)
        entry_could_get = Entry(bottom_frame_d, state="disabled")
        entry_could_get.grid(column=1, row=0)

        label_will_get = Label(bottom_frame_d)
        label_will_get.grid(column=0, row=1)
        entry_will_get = Entry(bottom_frame_d, state="disabled")
        entry_will_get.grid(column=1, row=1)

        label_will_get_in_cur1 = Label(bottom_frame_d)
        label_will_get_in_cur1.grid(column=0, row=2)

        label_loss_cur1 = Label(bottom_frame_d)
        label_loss_cur1.grid(column=0, row=3)
        entry_loss_cur1 = Entry(bottom_frame_d, state="disabled")
        entry_loss_cur1.grid(column=1, row=3)

        label_loss_cur2 = Label(bottom_frame_d)
        label_loss_cur2.grid(column=0, row=4)
        entry_loss_cur2 = Entry(bottom_frame_d, state="disabled")
        entry_loss_cur2.grid(column=1, row=4)

        label_loss_perc = Label(bottom_frame_d)
        label_loss_perc.grid(column=0, row=5)
        entry_loss_perc = Entry(bottom_frame_d, state="disabled")
        entry_loss_perc.grid(column=1, row=5)

        sep4 = Separator(bottom_frame,  orient="horizontal")  # ----------------------------------------------------------------------
        sep4.pack(side=TOP, fill=X)

        label_real_rate = Label(bottom_frame, text="How many decimal places?", font=("Arial", 16, "bold"), justify=LEFT)
        label_real_rate.pack(side=TOP)

        scale = Scale(bottom_frame, orient="horizontal", from_=0, to=17, variable=self.decimal_places)
        scale.pack(side=TOP, fill=X)

        self.root.mainloop()




        # halt son calc: bester kurs mit gegebenem kurs vergleichen und dann loose werte prozentual und absolut ausgeben
        # mit gui