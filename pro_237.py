with open("file.py","w+") as f:
    f.write(
        """
        import time
    
        print("What should I remin you about?")
        text= str(input())
        print("In how many minutes?")
        local_time= float(input())
        local_time= local_time*60
        time.sleep(local_time)
        print(text)
        
        """
    )
    

