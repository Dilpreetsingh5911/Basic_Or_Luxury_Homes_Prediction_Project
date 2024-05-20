# Importing necessary libraries
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

root = Tk()
root.geometry('1500x700')
root.title('ML Project')
root.config(bg='lightsteelblue3')

# Load images
img = Image.open('image_datasets/home_image.png')
i = ImageTk.PhotoImage(img)

im = Image.open('image_datasets/Interior-Design2.jpg')
luxury_house_img = ImageTk.PhotoImage(im)

ima = Image.open('image_datasets/arrow_image.jpg')
arrow_image = ImageTk.PhotoImage(ima)

# First page function
def first_page():
    def submit():
        def clearall():
            user_reset_answer = messagebox.askquestion('Reset', 'Do You Want To Reset.')
            if user_reset_answer == 'yes':
                # Destroy all widgets
                for widget in root.winfo_children():
                    widget.destroy()
                first_page()

        # Check if entries are empty
        if (not square_meter_entry.get() or not number_of_rooms_entry.get() or
                not has_yard_entry.get() or not has_pool_entry.get() or
                not floors_entry.get() or not city_code_entry.get() or
                not made_in_entry.get() or not is_new_build_entry.get() or
                not has_strome_protector_entry.get() or not basement_entry.get() or
                not garage_entry.get() or not storage_room_entry.get() or
                not guest_room_entry.get() or not price_entry.get()):
            messagebox.showinfo('Details', 'Enter Details')
            return
            

        # Retrieve data from entries
        data = [
            int(square_meter_entry.get()),
            int(number_of_rooms_entry.get()),
            int(has_yard_entry.get()),
            int(has_pool_entry.get()),
            int(floors_entry.get()),
            int(city_code_entry.get()),
            int(made_in_entry.get()),
            int(is_new_build_entry.get()),
            int(has_strome_protector_entry.get()),
            int(basement_entry.get()),
            int(garage_entry.get()),
            int(storage_room_entry.get()),
            int(guest_room_entry.get()),
            int(price_entry.get())
        ]

        # Load model and make prediction
        prediction_value = model.predict([data])[0]
        print('prediction_value :',prediction_value)

        # Clear previous elements
        button_label_frame.destroy()
        submit_button.destroy()
        arrow_img.destroy()

        # Show prediction result
        label_frame = LabelFrame(root, text='Predicted Value', font='arial 20 italic', bd=20, relief=GROOVE, bg='lightsteelblue3')
        label_frame.grid(row=15, column=1)

        result_text = 'Luxury Home' if prediction_value == 'Luxury' else 'Basic Home'
        l16 = Label(label_frame, text=result_text, font='arial 30 bold', bg='lightsteelblue2')
        l16.pack()

        # Clear and done buttons
        clear_label_frame = LabelFrame(root, text='', font='arial 20 italic', bd=15, relief=GROOVE, bg='lightsteelblue3')
        clear_label_frame.grid(row=15, column=0)
        reset_button = Button(clear_label_frame, text='Reset', font='arial 20 bold', bg='lightsteelblue2', command=clearall)
        reset_button.pack()

        done_label_frame = LabelFrame(root, text='', font='arial 20 italic', bd=15, relief=GROOVE, bg='lightsteelblue3')
        done_label_frame.grid(row=15, column=2)
        done_button = Button(done_label_frame, text='Done', font='arial 20 bold', bg='lightsteelblue2', command=root.quit)
        done_button.pack()

    # Load dataset and train model
    dataset = pd.read_csv('datasets/ParisHousingClass.csv')
    dataset.drop(columns=['numPrevOwners', 'cityPartRange', 'attic'], inplace=True)
    x = dataset.iloc[:, :-1]
    y = dataset.iloc[:, -1]

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=0)
    model = DecisionTreeClassifier()
    model.fit(xtrain, ytrain)
    joblib.dump(model, 'paris_dump_data')
    model = joblib.load('paris_dump_data')

    def model_accuracy_rate():
        y_pred = model.predict(xtest)
        accuracy = accuracy_score(ytest, y_pred)
        messagebox.showinfo('Accuracy Score', f'Accuracy: {accuracy:.2f}')

    def exit_command():
        exit_value = messagebox.askquestion('Exit', 'Want To Exit')
        if exit_value == 'yes':
            root.quit()

    def ml_algorithm():
        messagebox.showinfo('ML Algorithm', "Using Decision Tree Classifier on ParisHousingClass.csv dataset.")

    def update():
        messagebox.showinfo('ML Model', 'There are currently no updates available.')

    def about_command():
        messagebox.showinfo('About', "Model by Dilpreet Singh.\nVersion: 3.0")

    # Menu
    main_menu = Menu(root, background='lightsteelblue3')

    model_menu = Menu(main_menu, tearoff=0, background='lightsteelblue3')
    model_menu.add_command(label='Model Accuracy Score', command=model_accuracy_rate, background='lightsteelblue3')
    main_menu.add_cascade(label='Model', menu=model_menu, background='lightsteelblue3')

    exit_menu = Menu(main_menu, tearoff=0, background='lightsteelblue3')
    exit_menu.add_command(label='Exit', command=exit_command, background='lightsteelblue3')
    main_menu.add_cascade(label='Exit', menu=exit_menu, background='lightsteelblue3')

    about_menu = Menu(main_menu, tearoff=0, background='lightsteelblue3')
    about_menu.add_command(label='ML Algorithm and Dataset', command=ml_algorithm, background='lightsteelblue3')
    about_menu.add_command(label='Check For Update...', command=update, background='lightsteelblue3')
    about_menu.add_separator(background='lightsteelblue3')
    about_menu.add_command(label='About', command=about_command, background='lightsteelblue3')
    main_menu.add_cascade(label='Help', menu=about_menu, background='lightsteelblue3')

    root.config(menu=main_menu, background='lightsteelblue3')

    # UI Elements
    image_label = Label(root, image=i, background='lightsteelblue4', bd=10)
    image_label.grid(row=0, column=0)

    la = Label(root, image=luxury_house_img, background='lightsteelblue4', bd=10)
    la.grid(row=0, column=2)

    arrow_img = Label(root, image=arrow_image, background='lightsteelblue4', bd=10)
    arrow_img.grid(row=15, column=1)

    heading_frame = LabelFrame(root, text='ML Model', font='arial 20 italic', bd=20, relief=GROOVE, bg='lightsteelblue3')
    heading_frame.grid(row=0, column=1)
    heading = Label(heading_frame, text='Basic Or Luxury Homes Prediction Model', font=('arial 30 italic'), bd=16, bg='lightsteelblue2')
    heading.pack()

    # Entry fields
    fields = [
        ('Square Meters', 1), ('Number Of Rooms', 2), ('Has yard (0,1)', 3),
        ('Has pool (0,1)', 4), ('Floors', 5), ('City Code', 6), ('Made In', 7),
        ('Is New Built (0,1)', 8), ('Has Storm Protector (0,1)', 9), ('Basement (0,1)', 10),
        ('Garage (0,1)', 11), ('Storage Room', 12), ('Guest Room', 13), ('Price', 14)
    ]
    entries = []
    for label_text, row in fields:
        label = Label(root, text=label_text + ':', font='arial 15 italic', bg='lightsteelblue3')
        label.grid(row=row, column=0)
        entry = Entry(root, background='grey')
        entry.grid(row=row, column=1)
        entries.append(entry)

    square_meter_entry, number_of_rooms_entry, has_yard_entry, has_pool_entry, floors_entry, city_code_entry, made_in_entry, is_new_build_entry, has_strome_protector_entry, basement_entry, garage_entry, storage_room_entry, guest_room_entry, price_entry = entries

    # Submit button
    button_label_frame = LabelFrame(root, text='', bd=17, background='lightsteelblue4')
    button_label_frame.grid(row=15, column=0)
    submit_button = Button(button_label_frame, text='Submit', font='sansserifPlain 20', background='lightsteelblue2', command=submit, bd=10)
    submit_button.pack()

first_page()
root.mainloop()
