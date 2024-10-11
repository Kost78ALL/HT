Stud={'Alex','Toha','Miha','Serg','Kolyan'}
print(Stud,'-Список студентов')
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
s=sorted(list(Stud))
res=[sum(grades[i])/len(grades[i]) for i in range(len(grades))]
Av_res={s[y]:res[y] for y in range(len(s))}
print(Av_res,'- Средние баллы')