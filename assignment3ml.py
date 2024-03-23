import math

filepath = 'usnewshealth.txt'
with open(filepath, encoding="utf8") as fp:
   line = fp.readline()
   cnt = 1
   answer = []
   while line:
       next = line.strip()[50:]
       next = " ".join(filter(lambda x: x[:1] != '@', next.split()))
       next = " ".join(filter(lambda x: x[:4] != 'http', next.split()))
       next = ''.join(c for c in next if c not in ':#.?!')
       next = next.lower()
       line = fp.readline()
       answer.append(next)
       cnt += 1
   cnt -= 1
   print(cnt)
   k = int(input("Enter the value of k: ")) #int(math.sqrt(cnt/2))
   print(k)
   kcluster = []
   kclusternew = []
   clusternumbers = []
   clusternum = 0
   keepGoing = 1

   for i in range(k):
       kcluster.append(answer[i])
       kclusternew.append(answer[i])

   while keepGoing == 1:
        sse = 0
        clusternumbers = []
        clusternum = 0
        for i in range(cnt):
            mindist = 2
            for j in range(k):
                unionn = set(answer[i]).union(set(kcluster[j]))
                intersectionn = set(answer[i]).intersection(set(kcluster[j]))
                jac = (len(unionn) - len(intersectionn))/len(unionn)
                if (jac < mindist):
                    mindist = jac
                    clusternum = j
                    sseadd = jac
            clusternumbers.append(clusternum)
            sse = sse + math.pow(sseadd,2)

        # sort clusternumbers in ascending order along with the corresponding tweets
        clusternumbers, answer = zip(*sorted(zip(clusternumbers, answer)))

        # find centroid in each clusternumber
        numb = 0
        minidist = cnt
        i = 0
        clusternum = 0
        while numb < k and i < cnt and j < cnt:
            start = i
            minidist = cnt
            while i < cnt and j < cnt and clusternumbers[i] == numb:
                j = start
                dist = 0
                while j < cnt and clusternumbers[j] == numb:
                    unionn = set(answer[i]).union(set(answer[j]))
                    intersectionn = set(answer[i]).intersection(set(answer[j]))
                    jac = (len(unionn) - len(intersectionn))/len(unionn)
                    dist = dist + jac
                    j = j + 1
                if dist < minidist:
                    minidist = dist
                    clusternum = i
                i = i + 1
            kclusternew[numb] = answer[clusternum]
            numb = numb + 1
        if kclusternew == kcluster:
            keepGoing = 0
        else:
            kcluster = kclusternew.copy()
   for i in range(k):
        print(i+1,": ",clusternumbers.count(i))
   print("SSE = ", sse)


