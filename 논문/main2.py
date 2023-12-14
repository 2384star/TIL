# try:
#     while True:
#         value = input(" A B C 중하나를 입력해주세요")

#         if len(value) ==1 and value not in "A-E":
#             raise ValueError("잘못된 입력")
        
#         print("선택된 옵션",value)
# except ValueError as e:
#     print(e)
for i in range(5,-5,-1):
    try:
        value/= i

    except NameError:
        print("value가 없어서 0으로 지정함")
        value=10

    except ZeroDivisionError:
        print("0으로 나눔, 넘어감")
    
    except Exception as e:
        print(type(e),e)
        raise e
    
    else:
        print(value)
    
    finally:
        print("step")