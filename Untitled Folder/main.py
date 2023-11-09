
# import json
# obj= {
#     "id":3,
#     "소지물":[
#         "휴대폰",
#         4e-3,
#         12341324,
#         None,
#         []

#     ]
# }


# with open("output.json","w") as fd:
#     json.dump(obj,fd)

# import yaml
# with open("test.yaml","r") as fd:
#     data=yaml.load(fd,Loader=yaml.FullLoader)


# print(data)
# data["수정됨"] =123456

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-l","--left",type=int,default=20)
# parser.add_argument("-r","--right",type=int,default=20)
# parser.add_argument("--operation",dest=op,type=int,default=20)
# args=parser.parse_args()
    
# print(args)

# if args.op=='sum':
#     out =args.left + args.right
# elif args.op =='sub':
#     out = args.left - args.right

for i in range(-5,5):
    try:
        print(f"{i}뭔가하는중")
        print(10/i)
        print(f"{i}뭔가마무리중")
    except ZeroDivisionError:
        print("에러무시하고 진행")