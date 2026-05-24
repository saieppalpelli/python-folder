import pdb

def cal_area(radius):
    pi = 3.14
    return pi * radius**2

def cal_circum(radius):
    pi = 3.14
    return pi * radius * 2

def main():
    radius = 4
    area = cal_area(radius)
    import pdb;pdb.set_trace()
    circumference = cal_circum(radius)
    print(f"area: {area}")
    print(f"circumference: {circumference}")

main()