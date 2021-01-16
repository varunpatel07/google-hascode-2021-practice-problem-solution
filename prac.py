inp_file=open(r"C:\Users\lenovo\Desktop\hashcode\e.in","r")
out_file=open(r"C:\Users\lenovo\Desktop\hashcode\e_out.txt","w")

result=inp_file.readlines()
pizza_delivered=0
output_list=[]
total_score=0
team_details=result[0].split()
total_pizza=main_total_pizza=int(team_details[0])
team_of_2=int(team_details[1])
team_of_3=int(team_details[2])
team_of_4=int(team_details[3])
#print(total_pizza)
pizza_list={}

for index,item in enumerate(result[1:]):
    pizza_list[index]=item.split()[1:]
#print(pizza_list)
pizza_list=sorted(pizza_list.items(),key=lambda x: len(x[1]),reverse=True)
#print(pizza_list)
#print(total_pizza//2)
while(total_pizza//2 and team_of_2):
    #print("yes")
    if(total_pizza-2>=0):
        total_pizza-=2
        index1,pizza_1=pizza_list[0][0],pizza_list[0][1]
        index2,pizza_2=pizza_list[1][0],pizza_list[1][1]
        pizza_1.extend(pizza_2)
        #print(pizza_1)
        del pizza_list[:2]
        total_ing=len(set(pizza_1))
        output_list.append((2,index1,index2))
        #print("2 {} {}".format(index1,index2))
        #print(total_ing)
        #print("score for team of 2={}".format(total_ing**2))
        total_score+=total_ing**2
        team_of_2-=1
        pizza_delivered+=1
        #print(len(pizza_list))
    else:
        break
#print(pizza_list)
while(total_pizza//3 and team_of_3):
    #print("yes")
    if(total_pizza-3>=0):
        total_pizza-=3
        index1,pizza_1=pizza_list[0][0],pizza_list[0][1]
        index2,pizza_2=pizza_list[1][0],pizza_list[1][1]
        index3,pizza_3=pizza_list[2][0],pizza_list[2][1]
        pizza_1.extend(pizza_2)
        pizza_1.extend(pizza_3)
        #print(pizza_1)
        #print(pizza_1)
        del pizza_list[:3]
        #print("3 {} {} {}".format(index1,index2,index3))
        total_ing=len(set(pizza_1))
        output_list.append((3,index1,index2,index3))
        #print(total_ing)
        #print("score for team of 3={}".format(total_ing**2))
        total_score+=total_ing**2
        pizza_delivered+=1
        team_of_3-=1
    else:
        break
while(total_pizza//4 and team_of_4):
    #print("yes")
    if(total_pizza-4>=0):
        total_pizza-=4
        index1,pizza_1=pizza_list[0][0],pizza_list[0][1]
        index2,pizza_2=pizza_list[1][0],pizza_list[1][1]
        index3,pizza_3=pizza_list[2][0],pizza_list[2][1]
        index4,pizza_4=pizza_list[3][0],pizza_list[3][1]
        pizza_1.extend(pizza_2)
        pizza_1.extend(pizza_3)
        pizza_1.extend(pizza_4)
        #print(pizza_1)
        #print(pizza_1)
        del pizza_list[:4]
        output_list.append((4,index1,index2,index3,index4))
        total_ing=len(set(pizza_1))
        #print(total_ing)
        #print("score for team of 4={}".format(total_ing**2))
        total_score+=total_ing**2
        pizza_delivered+=1
        team_of_4-=1
    else:
        break
#print(total_score)
print(pizza_delivered)
out_file.write("{}\n".format(pizza_delivered))
#print(len(output_list))
for item in output_list:
    if(item[0]==2):
        #print("{} {} {}".format(item[0],item[1],item[2]))
        out_file.write("{} {} {}\n".format(item[0],item[1],item[2]))
    elif(item[0]==3):
        #print("{} {} {} {}".format(item[0],item[1],item[2],item[3]))
        out_file.write("{} {} {} {}\n".format(item[0],item[1],item[2],item[3]))
    elif(item[0]==4):
        #print("{} {} {} {} {}".format(item[0],item[1],item[2],item[3],item[4]))
        out_file.write("{} {} {} {} {}\n".format(item[0],item[1],item[2],item[3],item[4]))

print("total pizza={}\npizza delivered={}\ntotal team who got pizzas={}\nscore={}".format(main_total_pizza,(main_total_pizza-total_pizza),pizza_delivered,total_score))
inp_file.close()
out_file.close()