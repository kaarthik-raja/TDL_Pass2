with open('./Test_public/names.txt','w') as f:
    for i in range(1,5001):
        f.write("./Test_public/png/bar_val_easy_%08d.png\n"%i)
        
with open('./Train/names.txt','w') as f:
    for i in range(1,50001):
        f.write("./Train/png/bar_train_%08d.png\n"%i)
        
with open('./Test_private/names.txt','w') as f:
    for i in range(5001,10001):
        f.write("./Test_private/png/bar_val_easy_%08d.png\n"%i)