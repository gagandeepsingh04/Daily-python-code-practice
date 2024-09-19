def avgOfMarks(markslist, n):
    sum= 0 
    for i in markslist:
        sum+= float(i)
    number= sum/len(markslist)
    avgMarks= f"{number:.2f}"
    print(avgMarks)

def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avgOfMarks(student_marks[query_name], n)

if __name__ == '__main__':
    main()
    
