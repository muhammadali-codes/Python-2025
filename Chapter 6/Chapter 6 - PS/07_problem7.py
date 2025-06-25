# Write a program to find out whether a given post is talking about “MuhammadAli” or not. 

# post = "MuhammadAli is a python developer.He is interested in Computer Science field."

post = input("Enter the post: ")

if("MuhammadAli".lower() in post.lower()):
    print("This post is talking about MuhammadAli")

else:
    print("This post is not talking about MuhammadAli")