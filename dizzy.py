dizzy_str ="T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"
dizzy_list = dizzy_str.split(' ')
result_list = [None] * len(dizzy_list)
for item in dizzy_list:
    object_ = item[0]
    index_ =  int(item[1:3])
    result_list[index_] = object_
result_str = ''.join(result_list)
print("\n=============\n",result_str,"\n=============\n")