

def load_data():
    f = open("inputs/day9.txt")
    disk = f.readline().strip()
    f.close()
    segments = []
    
    for i in range(0,len(disk),2):
        try:
            segments.append((int(i/2),int(disk[i]),int(disk[i+1])))
        except IndexError:
            segments.append((int(i/2),int(disk[i]),0))
    return segments

def get_checksum(segs:list):
    segments = segs.copy()
    pt0 = 0
    check_sum = 0
    pt_end = 0
    index_end = len(segments)-1
    for index,segment in enumerate(segments):
        pt_end = segment[2]
        check_sum += sum(range(pt0,pt0+segment[1]))*index
        pt0+=segment[1]
        while pt_end > 0:
            if index_end > index:
                segment2 = segments[index_end]
                if segment2[1]<=pt_end:
                    check_sum += sum(range(pt0,pt0+segment2[1]))*index_end
                    #print((pt0+segment2[1])*index_end-pt0*index_end)
                    pt0 += segment2[1]
                    pt_end = pt_end- segment2[1]
                    index_end -= 1
                else:
                    check_sum += sum(range(pt0,pt0+pt_end))*index_end
                    pt0 += pt_end
                    segment2 = (index_end,segment2[1]-pt_end,segment2[2])
                    segments[index_end] = segment2
                    pt_end = 0
            else:
                return check_sum
    return check_sum

def get_checksum2(segments:list):
    work_segments = segments.copy()
    current_index = len(segments)-1
    min_index = 0
    while current_index > 0:
        current_segment = work_segments[current_index]
        for index,segment in enumerate(work_segments):
            if current_index <= index:
                break
            if segment[2] >= current_segment[1]:
                current_index = work_segments.index(current_segment)
                work_segments.pop(current_index)
                
                new_segment = (-1,0,current_segment[1]+current_segment[2])
                #work_segments.pop(current_index-1)
                work_segments.insert(current_index,new_segment)
                current_index += 1
                
                
                work_segments.pop(index)
                new_segment = (segment[0],segment[1],0)
                work_segments.insert(index,new_segment)
                
                new_segment = (current_segment[0],current_segment[1],segment[2]-current_segment[1])
                work_segments.insert(index+1,new_segment)
                break
        current_index -= 1
    pt0 = 0
    check_sum = 0
    for _,segment in enumerate(work_segments):
        check_sum += sum(range(pt0,pt0+segment[1]))*segment[0]
        pt0+= segment[1] + segment[2]
    return check_sum , work_segments


        

if __name__=="__main__":
    segs = load_data()
    print(get_checksum(segs))
    cs2, segments = get_checksum2(segs)
    
    print(cs2)
    