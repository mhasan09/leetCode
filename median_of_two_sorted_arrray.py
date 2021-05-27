def median_of_two_sorted_array(nums1,nums2):
    c = nums1 + nums2
    c.sort()
    print(c)
    c_len = len(c)
    print(c_len)
    if c_len % 2 != 0:
        cc = c_len%2
        print(c[cc])
    else:
        cc = int(c_len/2)
        print((c[cc-1]+c[cc])/2)

    xxx = []
    print(len(xxx))

x = [1,3,4,2]
y = [6,5,8,7]
median_of_two_sorted_array(x,y)