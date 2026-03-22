import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from decoder import DataHandler
from scipy.optimize import curve_fit
#global df
df = None

def load_data():
    handler = DataHandler("./data")
    handler.open_data()
    handler.write_data_csv(handler.data_ts)
    messagebox.showinfo("Success", "File uploaded successfully!")
    print("Data loaded!")
    
def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))
    return "break"
    
def process_data(df, selected_str):
    df = df[df.columns.drop(list(df.filter(regex='^DAQ2')))]
    df.rename(columns=lambda x: x.replace('DAQ1_', ''), inplace=True)
#    df = df[df['TIMES. (1ms)'] > 0]
    df_HG = df[[col for col in df.columns if selected_str in col or 'TIMES. (1ms)' in col or 'TIMES. ABS. (10ns)' in col or 'TRIGGER COUNTS 1' in col]]
#    df_HG = df[[col for col in df.columns if selected_str in col ]]
    data = [
    # Your data list here..
    "pst_2_4_2 <= A_TRIG(0)",
    "pst_2_4_3 <= A_TRIG(1)",
    "pst_1_5_3 <= A_TRIG(2)",
    "pst_1_5_2 <= A_TRIG(3)",
    "pst_2_6_3 <= A_TRIG(4)",
    "pst_2_6_2 <= A_TRIG(5)",
    "pst_2_6_1 <= A_TRIG(6)",
    "pst_2_8_3 <= A_TRIG(7) ",
    "pst_2_8_2 <= A_TRIG(8)",
    "pst_2_8_1 <= A_TRIG(9)",
    "pst_1_7_3 <= A_TRIG(10)",
    "pst_1_7_2 <= A_TRIG(11)",
    "pst_1_1_3 <= A_TRIG(12)",
    "pst_1_1_2 <= A_TRIG(13)",
    "pst_1_3_2 <= A_TRIG(14)",
    "pst_1_3_3 <= A_TRIG(15)",
    "pst_2_2_1 <= A_TRIG(16)",
    "pst_2_2_2 <= A_TRIG(17)",
    "pst_2_2_3 <= A_TRIG(18)",
    "pst_2_4_1 <= A_TRIG(19)",
    "pst_1_5_1 <= A_TRIG(20)",
    "pst_1_3_1 <= A_TRIG(21)",
    "pst_1_1_1 <= A_TRIG(22)",
    "pst_1_7_1 <= A_TRIG(23)",
    "pst_4_8_2 <= B_TRIG(0)",
    "pst_4_8_3 <= B_TRIG(1)",
    "pst_3_7_1 <= B_TRIG(2)",
    "pst_3_7_2 <= B_TRIG(3)",
    "pst_3_7_3 <= B_TRIG(4)",
    "pst_4_6_2 <= B_TRIG(5)",
    "pst_4_6_3 <= B_TRIG(6)",
    "pst_3_5_1 <= B_TRIG(7)",
    "pst_3_5_2 <= B_TRIG(8)",
    "pst_3_5_3 <= B_TRIG(9)",
    "pst_3_3_3 <= B_TRIG(10)",
    "pst_4_4_3 <= B_TRIG(11)",
    "pst_4_8_1 <= B_TRIG(12)",
    "pst_4_6_1 <= B_TRIG(13)",
    "pst_4_4_1 <= B_TRIG(14)",
    "pst_4_2_1 <= B_TRIG(15)",
    "pst_4_2_2 <= B_TRIG(16)",
    "pst_4_2_3 <= B_TRIG(17)",
    "pst_3_3_2 <= B_TRIG(18)",
    "pst_3_3_1 <= B_TRIG(19)",
    "pst_4_4_2 <= B_TRIG(20)",
    "pst_3_1_3 <= B_TRIG(21)",
    "pst_3_1_2 <= B_TRIG(22)",
    "pst_3_1_1 <= B_TRIG(23)",
    "acs_11 <= B_TRIG(24)",
    "acs_12 <= B_TRIG(25)",
    "acs_21 <= B_TRIG(26)",
    "acs_22 <= B_TRIG(27)",
    "acs_31 <= B_TRIG(28)",
    "acs_32 <= B_TRIG(29)",
    "acs_41 <= B_TRIG(30)",
    "acs_42 <= B_TRIG(31) ",
    "acs_51 <= C_TRIG(0)",
    "acs_52 <= C_TRIG(1)",
    "calog_1_6x6 <= C_TRIG(2)",
    "calog_1_3x3 <= C_TRIG(3)",
    "calog_1_1x1 <= C_TRIG(4)",
    "calog_2_6x6 <= C_TRIG(5)",
    "calog_2_3x3 <= C_TRIG(6)",
    "calog_2_1x1 <= C_TRIG(7)",
    "calog_3_6x6 <= C_TRIG(8)",
    "calog_3_3x3 <= C_TRIG(9)",
    "calog_3_1x1 <= C_TRIG(10)",
    "calog_4_6x6 <= C_TRIG(11)",
    "calog_4_3x3 <= C_TRIG(12)",
    "calog_4_1x1 <= C_TRIG(13)",
    "calog_5_6x6 <= C_TRIG(14)",
    "calog_5_3x3 <= C_TRIG(15)",
    "calog_5_1x1 <= C_TRIG(16)",
    "calog_6_6x6 <= C_TRIG(17)",
    "calog_6_3x3 <= C_TRIG(18)",
    "calog_6_1x1 <= C_TRIG(19)",
    "calog_7_6x6 <= C_TRIG(20)",
    "calog_7_3x3 <= C_TRIG(21)",
    "calog_7_1x1 <= C_TRIG(22)",
    "calog_8_6x6 <= C_TRIG(23)",
    "calog_8_3x3 <= C_TRIG(24)",
    "calog_8_1x1 <= C_TRIG(25)"
    ]
    
    trans_dict = {"A": "0", "B": "1", "C": "2","D": "3"}
    data_dict = {}
    for item in data:
        key, value = item.split(' <= ')
        letter, number = value.split('(')
        number = number.rstrip(' )')
        letter = trans_dict[letter[0]]
        new_value = "Asic" + letter + "_CH" + number + selected_str
        data_dict[new_value] = key.strip()
    
    df_HG.rename(columns=data_dict, inplace=True)
    
    cols_to_drop = df_HG.columns[df_HG.columns.str.contains('Asic3')]
    df_HG.drop(columns=cols_to_drop, inplace=True)
    
    cols_to_drop = df_HG.columns[df_HG.columns.str.contains('Asic2')]
    df_HG.drop(columns=cols_to_drop, inplace=True)
    df = df_HG
    df.to_csv('my_data'+selected_str + '.csv', index=False)
    return df


def plot_acd_graph(df):
  #  new_window = tk.Toplevel(root)
    if df.empty:
        messagebox.showerror("Information", "Empty")
        return None

    acs_cols = [col for col in df.columns if 'acs' in col]

    if not acs_cols:
        messagebox.showerror("Information", "No columns with 'calo' in their name found in the DataFrame.")
        return None
    n = len(acs_cols)
    n_rows =  n // 2 + n % 2
    bins = np.linspace(0, 16000, 128)
    new_window = None
    fig, ax = None, None
    
    if dc == "_HG":
        for i, col in enumerate(acs_cols):
            if i % 2 == 0:  # if i is divisible by 2, create a new window and figure
                new_window = tk.Toplevel(root)
                fig, ax = plt.subplots(2, 1, figsize=(10, 6))  # create a 2x2 grid of subplots
                ax = ax.ravel()  # make the 2x2 grid a flat list

            df[col].hist(bins=bins, ax=ax[i%2],color = "blue")  # select the subplot
            ax[i%2].set_title(f'Histogram of {col}')
            ax[i%2].set_xlabel(col)
            ax[i%2].set_ylabel('Counts')
            ax[i%2].set_yscale('log')
            ax[i%2].grid(False)

            if i % 2 == 1 or i == len(acs_cols) - 1:  # if it's the last plot in the window or the last plot overall
                plt.tight_layout()
                canvas = FigureCanvasTkAgg(fig, master=new_window)
                toolbar = NavigationToolbar2Tk(canvas, new_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        root.update_idletasks()
    if dc == "_LG":
        for i, col in enumerate(acs_cols):
            if i % 2 == 0:  # if i is divisible by 2, create a new window and figure
                new_window = tk.Toplevel(root)
                fig, ax = plt.subplots(2, 1, figsize=(10, 6))  # create a 2x2 grid of subplots
                ax = ax.ravel()  # make the 2x2 grid a flat list

            df[col].hist(bins=bins, ax=ax[i%2], color = "red")  # select the subplot
            ax[i%2].set_title(f'Histogram of {col}')
            ax[i%2].set_xlabel(col)
            ax[i%2].set_yscale('log')
            ax[i%2].set_ylabel('Counts')
            ax[i%2].grid(False)

            if i % 2 == 1 or i == len(acs_cols) - 1:  # if it's the last plot in the window or the last plot overall
                plt.tight_layout()
                canvas = FigureCanvasTkAgg(fig, master=new_window)
                toolbar = NavigationToolbar2Tk(canvas, new_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        root.update_idletasks()


def plot_calo_graph(df):
  #  new_window = tk.Toplevel(root)
    if df.empty:
        messagebox.showerror("Information", "Empty")
        return None

    calo_cols = [col for col in df.columns if 'calo' in col]

    if not calo_cols:
        messagebox.showerror("Information", "No columns with 'calo' in their name found in the DataFrame.")
        return None
    n = len(calo_cols)
    n_rows =  n // 2 + n % 2
    bins = np.linspace(0, 10000, 128)
    new_window = None
    fig, ax = None, None
    if dc == "_HG":
        for i, col in enumerate(calo_cols):
            if i % 3 == 0:  # if i is divisible by 4, create a new window and figure
                new_window = tk.Toplevel(root)
                fig, ax = plt.subplots(3, 1, figsize=(10, 6))  # create a 2x2 grid of subplots
                ax = ax.ravel()  # make the 2x2 grid a flat list

            df[col].hist(bins=bins, ax=ax[i%3],color = "blue")  # select the subplot
            ax[i%3].set_title(f'Histogram of {col}')
            ax[i%3].set_xlabel(col)
            ax[i%3].set_yscale('log')
            ax[i%3].set_ylabel('Counts')
            ax[i%3].grid(False)

            if i % 3 == 2 or i == len(calo_cols) - 1:  # if it's the last plot in the window or the last plot overall
                plt.tight_layout()
                canvas = FigureCanvasTkAgg(fig, master=new_window)
                toolbar = NavigationToolbar2Tk(canvas, new_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        root.update_idletasks()
    if dc == "_LG":
        for i, col in enumerate(calo_cols):
            if i % 3 == 0:  # if i is divisible by 4, create a new window and figure
                new_window = tk.Toplevel(root)
                fig, ax = plt.subplots(3, 1, figsize=(10, 6))  # create a 2x2 grid of subplots
                ax = ax.ravel()  # make the 2x2 grid a flat list

            df[col].hist(bins=bins, ax=ax[i%3],color = "red")  # select the subplot
            ax[i%3].set_title(f'Histogram of {col}')
            ax[i%3].set_xlabel(col)
            ax[i%3].set_ylabel('Counts')
            ax[i%3].set_yscale('log')
            ax[i%3].grid(False)

            if i % 3 == 2 or i == len(calo_cols) - 1:  # if it's the last plot in the window or the last plot overall
                plt.tight_layout()
                canvas = FigureCanvasTkAgg(fig, master=new_window)
                toolbar = NavigationToolbar2Tk(canvas, new_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        root.update_idletasks()
        
def plot_pst_graph(df):
  #  new_window = tk.Toplevel(root)
    if df.empty:
        messagebox.showerror("Information", "Empty")
        return None

    calo_cols = [col for col in df.columns if 'pst' in col]

    if not calo_cols:
        messagebox.showerror("Information", "No columns with 'calo' in their name found in the DataFrame.")
        return None
    n = len(calo_cols)
    n_rows =  n // 2 + n % 2
    grouped_cols = {}
    for col in calo_cols:
        parts = col.split('_')
        key = parts[0] + '_' + '_'.join(parts[2:])  # First and last parts of the name
        if key not in grouped_cols:
            grouped_cols[key] = []
        grouped_cols[key].append(col)

    # Define colors for the 1/3 and 2/4 groups
    if dc == "_HG":
        colors = {'1': 'orange', '3': 'blue', '2': 'orange', '4': 'blue'}
    if dc == "_LG":
        colors = {'1': 'black', '3': 'red', '2': 'black', '4': 'red'}
    # Define the order of the keys for each file
    
    file_keys_order = [
        [['pst_4_1', 'pst_4_2', 'pst_4_3'], ['pst_3_1', 'pst_3_2', 'pst_3_3']],
        [['pst_1_1', 'pst_1_2', 'pst_1_3'], ['pst_2_1', 'pst_2_2', 'pst_2_3']],
        [['pst_5_1', 'pst_5_2', 'pst_5_3'], ['pst_6_1', 'pst_6_2', 'pst_6_3']],
        [['pst_7_1', 'pst_7_2', 'pst_7_3'], ['pst_8_1', 'pst_8_2', 'pst_8_3']],
        # Add more lists for other files
    ]
    
    bins = np.linspace(0, 10000, 128)
    new_window = None
    fig, ax = None, None

    for file_no, keys_order in enumerate(file_keys_order, start=1):
        # Create a new figure with a defined number of subplots
        new_window = tk.Toplevel(root)
        fig, ax = plt.subplots(len(keys_order), len(keys_order[0]), figsize=(10, 6*len(keys_order)))
        ax = ax.ravel()
        for i, key in enumerate(sum(keys_order, [])):  # Flatten keys_order
            cols = grouped_cols.get(key, [])
            for col in cols:
                #df[col][df[col]>5000].hist(bins=bins, ax=ax[i], alpha=0.5, label=col, color=colors[col.split('_')[1]], histtype='step')
                df[col].hist(bins=bins, ax=ax[i], alpha=0.5, label=col, color=colors[col.split('_')[1]], histtype='step')
            ax[i].set_title(f'Histogram of {key}')  # Set the title
           # ax[i].set_xlabel('Values')  # Set the x-label
            ax[i].set_ylabel('Counts')  # Set the y-label
            ax[i].set_yscale('log')
            ax[i].legend()  # Add a legend
            ax[i].grid(False)  # Remove grid
        plt.tight_layout()  # Auto adjust subplot params so that the subplot fits into the figure area
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        toolbar = NavigationToolbar2Tk(canvas, new_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.update_idletasks()
    
def import_csv_data(selected_str):
    global df
    global dc
    dc = selected_str
    file_path = filedialog.askopenfilename()
    if file_path == '':
        messagebox.showwarning("Warning", "No file selected!")
        print('No file selected')
        return False

    try:
        df = pd.read_csv(file_path, sep=";")
    except ValueError:
        messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        messagebox.showerror("Information", f"No such file as {file_path}")
        return None
    
    df = process_data(df, selected_str)
    
 #   df1 = df.sample(n=15).iloc[:, :50]  # Select only the first 10 columns
    df1 = df.iloc[:, :100]
    clear_data()
    tree["column"] = list(df1.columns)
    tree["show"] = "headings"
    
    for column in tree["columns"]:
        tree.heading(column, text=column)
        tree.column(column, minwidth=0, width=100, stretch=tk.NO)

    df_rows = df1.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)

    print('Data Loaded Successfully')
    return True
    
def clear_data():
    tree.delete(*tree.get_children())

def plot_button_clicked():
    if df is not None:
        plot_calo_graph(df)
    else:
        messagebox.showerror("Error", "Please load a CSV file first.")

def plot_button_clicked1():
    if df is not None:
        plot_acd_graph(df)
    else:
        messagebox.showerror("Error", "Please load a CSV file first.")

def plot_button_clicked2():
    if df is not None:
        plot_pst_graph(df)
    else:
        messagebox.showerror("Error", "Please load a CSV file first.")

def hg_button_clicked():
    if import_csv_data('_HG') is True:
        hg_button.destroy()
        lg_button.destroy()
        transform.destroy()
        create_plot_button()

def lg_button_clicked():
    if import_csv_data('_LG') is True:
        hg_button.destroy()
        lg_button.destroy()
        transform.destroy()
        create_plot_button()

def create_upload_buttons():
    root.update_idletasks()
    global hg_button, lg_button, transform
#    create_tree()
#    tree = ttk.Treeview(frame1, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
#    tree.pack(side="left", expand=True, fill='both')
    hg_button = tk.Button(root, text="Open CSV for _HG", command=hg_button_clicked)
    lg_button = tk.Button(root, text="Open CSV for _LG", command=lg_button_clicked)
    transform = tk.Button(root, text="Change bin into CSV", command=load_data)
    hg_button.pack(fill='x')
    lg_button.pack(fill='x')
    transform.pack(fill='x')
#    create_tree()
    
def create_tree():
    global tree
    x_scrollbar = ttk.Scrollbar(frame1, orient='horizontal')
    x_scrollbar.pack(side='bottom', fill='x')

    y_scrollbar = ttk.Scrollbar(frame1, orient='vertical')
    y_scrollbar.pack(side='right', fill='y')
    tree = ttk.Treeview(frame1, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
    tree.pack(side="left", expand=True, fill='both')

    x_scrollbar.config(command=tree.xview)
    y_scrollbar.config(command=tree.yview)

    
def create_plot_button():
    global plot_button1, plot_button2, plot_button,close_button, close_button1
    plot_button = tk.Button(root, text="Calo Graph", fg='red',command=plot_button_clicked)
    plot_button.pack(side='left')
    plot_button1 = tk.Button(root, text="ACS",fg='blue', command=plot_button_clicked1)
    plot_button1.pack(side='left')
    plot_button2 = tk.Button(root, text="PST",fg='orange', command=plot_button_clicked2)
    plot_button2.pack(side='left')
    close_button = tk.Button(root, text="Change CSV",fg='black', command=close_data_window)
    close_button.pack(side='left')
    close_button1 = tk.Button(root, text="Close",fg='brown', command=close_data_window1)
    close_button1.pack(side='left')

def close_data_window():
    plot_button.destroy()
    plot_button1.destroy()
    plot_button2.destroy()
    close_button.destroy()
    close_button1.destroy()
 #   tree.destroy()
    create_upload_buttons()
    
def close_data_window1():
   root.destroy()
    
def update_scrollregion():
    frame_tree.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

root = tk.Tk()
#root.attributes('-fullscreen', True)
root.state('zoomed')
frame1 = ttk.Frame(root)
frame1.pack(fill='both', expand=True)
#frame1.grid_columnconfigure(0, weight=1)
#frame1.grid_rowconfigure(0, weight=1)

x_scrollbar = ttk.Scrollbar(frame1, orient='horizontal')
x_scrollbar.pack(side='bottom', fill='x')

y_scrollbar = ttk.Scrollbar(frame1, orient='vertical')
y_scrollbar.pack(side='right', fill='y')

tree = ttk.Treeview(frame1, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
tree.pack(side="left", expand=True, fill='both')

x_scrollbar.config(command=tree.xview)
y_scrollbar.config(command=tree.yview)
#create_tree()
create_upload_buttons()
#hg_button = tk.Button(root, text="Open CSV for _HG", command=hg_button_clicked)
#lg_button = tk.Button(root, text="Open CSV for _LG", command=lg_button_clicked)

#hg_button.pack(fill='x')
#lg_button.pack(fill='x')


root.mainloop()

