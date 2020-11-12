import tkinter as tk

root = tk.Tk()
root.geometry("380x250")
root.title("Instagram Profile Info")

text = tk.StringVar()

def scrape():
    username = text.get()
    response = requests.get('https://instagram.com/' + username)
    soup = BeautifulSoup(response.text, 'html.parser')
    user_info = soup.find("meta", property="og:description")

    clean_user_info = user_info.attrs['content'].split('-')[0]
    print()
    print(clean_user_info)

welcome = tk.Label(root, text="Instagram Profile Info", font=("Helvetica", 20))
welcome.place(x = 50, y = 10)

textlabel = tk.Label(root, text="Enter Username", font=("Helvetica", 10))
textlabel.place(x = 40, y = 60)

textbox = tk.Entry(root, textvariable=text)
textbox.place(x = 200, y = 60)

submit = tk.Button(root, text= "Get Details", command = scrape, width= 10)
submit.place(x = 140, y = 90)

post = tk.Label(root, text="Posts:", font=("Helvetica", 10))
post.place(x = 80, y = 140)

posts = tk.Label(root, text="Enter Username", font=("Helvetica", 10))
posts.place(x = 180, y = 140)

foll = tk.Label(root, text="Following:", font=("Helvetica", 10))
foll.place(x = 80, y = 170)

folls = tk.Label(root, text="Enter Username", font=("Helvetica", 10))
folls.place(x = 180, y = 170)

follw = tk.Label(root, text="Followers:", font=("Helvetica", 10))
follw.place(x = 80, y = 200)

follws = tk.Label(root, text="Enter Username", font=("Helvetica", 10))
follws.place(x = 180, y = 200)

root.mainloop()