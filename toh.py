def toh(n,src,hel,dest):
    if n==1:
        print(f"Moving disk {n} from {src} to {dest}")
        return

    toh(n-1,src,dest,hel)
    print(f"Moving disk {n} from {src} to {dest}")
    toh(n-1,hel,src,dest)

toh(3,'A','B','C')
